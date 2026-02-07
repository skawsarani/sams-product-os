"""Slack URL parsing utilities."""

import re
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs


@dataclass
class SlackMessageLink:
    """Parsed Slack message/thread link."""

    channel_id: str
    message_ts: str
    thread_ts: str | None
    team_domain: str


def parse_slack_message_link(url: str) -> SlackMessageLink | None:
    """
    Parse a Slack message permalink into its components.

    Handles URLs like:
    - https://team.slack.com/archives/C12345678/p1700000000000123
    - https://team.slack.com/archives/C12345678/p1700000000000123?thread_ts=1700000000.000123&cid=C12345678

    Args:
        url: Slack message permalink.

    Returns:
        SlackMessageLink with parsed components, or None if not a valid Slack URL.
    """
    try:
        parsed = urlparse(url)

        # Check if it's a Slack URL
        if not parsed.hostname or not parsed.hostname.endswith(".slack.com"):
            return None

        # Extract team domain (everything before .slack.com)
        team_domain = parsed.hostname.replace(".slack.com", "")

        # Parse the path: /archives/{channel_id}/p{message_id}
        path_parts = parsed.path.strip("/").split("/")
        if len(path_parts) < 3 or path_parts[0] != "archives":
            return None

        channel_id = path_parts[1]

        # Extract message ID from p{timestamp} format
        message_segment = path_parts[2]
        if not message_segment.startswith("p"):
            return None

        # Convert p1700000000000123 to 1700000000.000123 format
        message_id = message_segment[1:]  # Remove 'p' prefix
        if len(message_id) >= 10:
            # Insert decimal point: first 10 digits are seconds, rest are microseconds
            message_ts = f"{message_id[:10]}.{message_id[10:]}" if len(message_id) > 10 else message_id
        else:
            message_ts = message_id

        # Check for thread_ts in query params
        query_params = parse_qs(parsed.query)
        thread_ts = query_params.get("thread_ts", [None])[0]

        return SlackMessageLink(
            channel_id=channel_id,
            message_ts=message_ts,
            thread_ts=thread_ts,
            team_domain=team_domain,
        )

    except Exception:
        return None


def build_slack_message_url(
    team_domain: str,
    channel_id: str,
    message_ts: str,
    thread_ts: str | None = None,
) -> str:
    """
    Build a Slack message permalink from components.

    Args:
        team_domain: Slack workspace domain (e.g., 'mycompany').
        channel_id: Channel ID (e.g., 'C12345678').
        message_ts: Message timestamp (e.g., '1700000000.000123').
        thread_ts: Optional thread timestamp for thread replies.

    Returns:
        Slack message permalink URL.
    """
    # Convert timestamp to URL format: 1700000000.000123 -> p1700000000000123
    message_id = "p" + message_ts.replace(".", "")

    url = f"https://{team_domain}.slack.com/archives/{channel_id}/{message_id}"

    if thread_ts:
        url += f"?thread_ts={thread_ts}&cid={channel_id}"

    return url


def is_slack_url(url: str) -> bool:
    """
    Check if a URL is a Slack URL.

    Args:
        url: URL to check.

    Returns:
        True if the URL is a Slack URL.
    """
    try:
        parsed = urlparse(url)
        return bool(parsed.hostname and parsed.hostname.endswith(".slack.com"))
    except Exception:
        return False
