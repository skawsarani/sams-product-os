"""URL parser utility for Slack, Notion, and Linear URLs.

Parses URLs from multiple services into structured data for use with integrations.
Falls back to raw text with keyword extraction for non-URL input.
"""

import re
from dataclasses import dataclass, field
from typing import Literal
from urllib.parse import urlparse, parse_qs

InputType = Literal[
    "slack-thread",
    "notion-page",
    "linear-issue",
    "linear-project",
    "linear-initiative",
    "google-doc",
    "google-sheet",
    "google-slide",
    "raw-text",
]

# Common stop words to filter out during keyword extraction
STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he",
    "in", "is", "it", "its", "of", "on", "or", "that", "the", "to", "was", "were",
    "will", "with", "this", "they", "but", "have", "had", "what", "when", "where",
    "who", "which", "why", "how", "all", "each", "every", "both", "few", "more",
    "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same",
    "so", "than", "too", "very", "can", "just", "should", "now", "also", "into",
    "could", "would", "there", "their", "then", "these", "those", "been", "being",
    "do", "does", "did", "doing", "about", "after", "before", "between", "through",
}


@dataclass
class ParsedInput:
    """Parsed URL or text input with extracted components."""

    type: InputType
    original_input: str

    # Slack fields
    channel_id: str | None = None
    message_ts: str | None = None
    thread_ts: str | None = None
    team_domain: str | None = None

    # Notion fields
    notion_page_id: str | None = None
    notion_workspace: str | None = None

    # Linear fields
    linear_identifier: str | None = None  # e.g., "ENG-123"
    linear_project_id: str | None = None
    linear_initiative_id: str | None = None
    linear_workspace: str | None = None

    # Google fields
    google_file_id: str | None = None
    google_file_type: Literal["document", "spreadsheet", "presentation"] | None = None

    # Raw text fields
    raw_text: str | None = None
    keywords: list[str] = field(default_factory=list)


def parse_input(input_str: str) -> ParsedInput:
    """
    Parse an input string (URL or text) into structured data.

    Tries parsers in order: Slack → Notion → Linear → Raw text.

    Args:
        input_str: URL or text to parse.

    Returns:
        ParsedInput with extracted components.
    """
    input_str = input_str.strip()

    # Try each parser in order
    result = parse_slack_url(input_str)
    if result:
        return result

    result = parse_notion_url(input_str)
    if result:
        return result

    result = parse_linear_url(input_str)
    if result:
        return result

    result = parse_google_url(input_str)
    if result:
        return result

    # Fall back to raw text
    return ParsedInput(
        type="raw-text",
        original_input=input_str,
        raw_text=input_str,
        keywords=extract_keywords_from_text(input_str),
    )


def parse_slack_url(url: str) -> ParsedInput | None:
    """
    Parse a Slack message permalink.

    Handles URLs like:
    - https://team.slack.com/archives/C12345678/p1700000000000123
    - https://team.slack.com/archives/C12345678/p1700000000000123?thread_ts=1700000000.000123

    Args:
        url: URL to parse.

    Returns:
        ParsedInput with Slack components, or None if not a Slack URL.
    """
    try:
        parsed = urlparse(url)

        if not parsed.hostname or not parsed.hostname.endswith(".slack.com"):
            return None

        team_domain = parsed.hostname.replace(".slack.com", "")

        # Parse path: /archives/{channel_id}/p{message_id}
        path_parts = parsed.path.strip("/").split("/")
        if len(path_parts) < 3 or path_parts[0] != "archives":
            return None

        channel_id = path_parts[1]

        # Extract message ID from p{timestamp} format
        message_segment = path_parts[2]
        if not message_segment.startswith("p"):
            return None

        # Convert p1700000000000123 to 1700000000.000123
        message_id = message_segment[1:]
        if len(message_id) >= 10:
            message_ts = f"{message_id[:10]}.{message_id[10:]}" if len(message_id) > 10 else message_id
        else:
            message_ts = message_id

        # Check for thread_ts in query params
        query_params = parse_qs(parsed.query)
        thread_ts = query_params.get("thread_ts", [None])[0]

        return ParsedInput(
            type="slack-thread",
            original_input=url,
            channel_id=channel_id,
            message_ts=message_ts,
            thread_ts=thread_ts,
            team_domain=team_domain,
        )

    except Exception:
        return None


def parse_notion_url(url: str) -> ParsedInput | None:
    """
    Parse a Notion page URL.

    Handles URLs like:
    - https://www.notion.so/workspace/Page-Title-abc123def456...
    - https://notion.so/abc123def456...
    - https://www.notion.so/abc123def456...?v=...

    Args:
        url: URL to parse.

    Returns:
        ParsedInput with Notion components, or None if not a Notion URL.
    """
    try:
        parsed = urlparse(url)

        if not parsed.hostname:
            return None

        # Check for notion.so domain
        if not (parsed.hostname == "notion.so" or parsed.hostname.endswith(".notion.so")):
            return None

        path_parts = [p for p in parsed.path.strip("/").split("/") if p]
        if not path_parts:
            return None

        workspace = None
        page_id = None

        # Notion page IDs are 32 hex characters (no dashes) at the end of the URL
        # They can be at the end of a slug like "Page-Title-abc123..." or standalone
        page_id_pattern = re.compile(r"[a-f0-9]{32}$", re.IGNORECASE)

        for part in reversed(path_parts):
            # Check if the part ends with a page ID
            match = page_id_pattern.search(part.replace("-", ""))
            if match:
                # Extract the 32-char ID
                clean_part = part.replace("-", "")
                page_id = clean_part[-32:]
                break

        if not page_id:
            return None

        # First path segment might be workspace name
        if len(path_parts) > 1:
            workspace = path_parts[0]

        return ParsedInput(
            type="notion-page",
            original_input=url,
            notion_page_id=page_id,
            notion_workspace=workspace,
        )

    except Exception:
        return None


def parse_linear_url(url: str) -> ParsedInput | None:
    """
    Parse a Linear URL (issue, project, or initiative).

    Handles URLs like:
    - https://linear.app/workspace/issue/ENG-123
    - https://linear.app/workspace/project/project-slug-abc123...
    - https://linear.app/workspace/initiative/initiative-slug-abc123...

    Args:
        url: URL to parse.

    Returns:
        ParsedInput with Linear components, or None if not a Linear URL.
    """
    try:
        parsed = urlparse(url)

        if parsed.hostname != "linear.app":
            return None

        path_parts = [p for p in parsed.path.strip("/").split("/") if p]
        if len(path_parts) < 3:
            return None

        workspace = path_parts[0]
        resource_type = path_parts[1]
        resource_id = path_parts[2]

        # UUID pattern for projects/initiatives
        uuid_pattern = re.compile(r"[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$", re.IGNORECASE)

        if resource_type == "issue":
            # Issue identifiers are like ENG-123
            return ParsedInput(
                type="linear-issue",
                original_input=url,
                linear_identifier=resource_id.upper(),
                linear_workspace=workspace,
            )

        elif resource_type == "project":
            # Project URLs: /workspace/project/slug-uuid
            # Extract UUID from end of slug
            uuid_match = uuid_pattern.search(resource_id)
            project_id = uuid_match.group() if uuid_match else resource_id

            return ParsedInput(
                type="linear-project",
                original_input=url,
                linear_project_id=project_id,
                linear_workspace=workspace,
            )

        elif resource_type == "initiative":
            # Initiative URLs: /workspace/initiative/slug-uuid
            uuid_match = uuid_pattern.search(resource_id)
            initiative_id = uuid_match.group() if uuid_match else resource_id

            return ParsedInput(
                type="linear-initiative",
                original_input=url,
                linear_initiative_id=initiative_id,
                linear_workspace=workspace,
            )

        return None

    except Exception:
        return None


def parse_google_url(url: str) -> ParsedInput | None:
    """
    Parse a Google Docs, Sheets, or Slides URL.

    Handles URLs like:
    - https://docs.google.com/document/d/{file_id}/edit
    - https://docs.google.com/spreadsheets/d/{file_id}/edit
    - https://docs.google.com/presentation/d/{file_id}/edit

    Args:
        url: URL to parse.

    Returns:
        ParsedInput with Google components, or None if not a Google URL.
    """
    try:
        parsed = urlparse(url)

        if parsed.hostname != "docs.google.com":
            return None

        path_parts = [p for p in parsed.path.strip("/").split("/") if p]
        if len(path_parts) < 3 or path_parts[1] != "d":
            return None

        doc_type = path_parts[0]
        file_id = path_parts[2]

        # Map URL path to file type and InputType
        type_mapping: dict[str, tuple[InputType, Literal["document", "spreadsheet", "presentation"]]] = {
            "document": ("google-doc", "document"),
            "spreadsheets": ("google-sheet", "spreadsheet"),
            "presentation": ("google-slide", "presentation"),
        }

        if doc_type not in type_mapping:
            return None

        input_type, file_type = type_mapping[doc_type]

        return ParsedInput(
            type=input_type,
            original_input=url,
            google_file_id=file_id,
            google_file_type=file_type,
        )

    except Exception:
        return None


def build_url(parsed: ParsedInput) -> str | None:
    """
    Reconstruct a URL from parsed components.

    Args:
        parsed: ParsedInput with components.

    Returns:
        Reconstructed URL, or None if not possible.
    """
    if parsed.type == "slack-thread":
        if not all([parsed.team_domain, parsed.channel_id, parsed.message_ts]):
            return None
        message_id = "p" + parsed.message_ts.replace(".", "")
        url = f"https://{parsed.team_domain}.slack.com/archives/{parsed.channel_id}/{message_id}"
        if parsed.thread_ts:
            url += f"?thread_ts={parsed.thread_ts}&cid={parsed.channel_id}"
        return url

    elif parsed.type == "notion-page":
        if not parsed.notion_page_id:
            return None
        # Format as hyphenated UUID style
        page_id = parsed.notion_page_id
        formatted_id = f"{page_id[:8]}-{page_id[8:12]}-{page_id[12:16]}-{page_id[16:20]}-{page_id[20:]}"
        if parsed.notion_workspace:
            return f"https://www.notion.so/{parsed.notion_workspace}/{formatted_id}"
        return f"https://www.notion.so/{formatted_id}"

    elif parsed.type == "linear-issue":
        if not all([parsed.linear_workspace, parsed.linear_identifier]):
            return None
        return f"https://linear.app/{parsed.linear_workspace}/issue/{parsed.linear_identifier}"

    elif parsed.type == "linear-project":
        if not all([parsed.linear_workspace, parsed.linear_project_id]):
            return None
        return f"https://linear.app/{parsed.linear_workspace}/project/{parsed.linear_project_id}"

    elif parsed.type == "linear-initiative":
        if not all([parsed.linear_workspace, parsed.linear_initiative_id]):
            return None
        return f"https://linear.app/{parsed.linear_workspace}/initiative/{parsed.linear_initiative_id}"

    elif parsed.type in ("google-doc", "google-sheet", "google-slide"):
        if not parsed.google_file_id or not parsed.google_file_type:
            return None
        type_to_path = {
            "document": "document",
            "spreadsheet": "spreadsheets",
            "presentation": "presentation",
        }
        path_segment = type_to_path[parsed.google_file_type]
        return f"https://docs.google.com/{path_segment}/d/{parsed.google_file_id}/edit"

    return None


def extract_keywords_from_text(text: str) -> list[str]:
    """
    Extract keywords from text, filtering stop words and URLs.

    Args:
        text: Text to extract keywords from.

    Returns:
        List of unique keywords (max 20), sorted by frequency.
    """
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)

    # Extract words (alphanumeric, 3+ chars)
    words = re.findall(r"\b[a-zA-Z0-9]{3,}\b", text.lower())

    # Filter stop words
    filtered = [w for w in words if w not in STOP_WORDS]

    # Count frequency
    freq: dict[str, int] = {}
    for word in filtered:
        freq[word] = freq.get(word, 0) + 1

    # Sort by frequency and return top 20
    sorted_words = sorted(freq.keys(), key=lambda w: freq[w], reverse=True)
    return sorted_words[:20]


def is_url(text: str) -> bool:
    """Check if text looks like a URL."""
    return text.strip().startswith(("http://", "https://"))
