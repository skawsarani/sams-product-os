"""CLI interface for common utilities (URL parser).

Usage:
    uv run python -m integrations.common <command> [options]

Commands:
    parse-url           Parse a URL or text input
"""

import argparse
import json
import sys
from dataclasses import asdict

from .url_parser import parse_input, build_url


def cmd_parse_url(args: argparse.Namespace) -> None:
    """Parse a URL or text input."""
    parsed = parse_input(args.input)
    result = asdict(parsed)

    # Add reconstructed URL if possible
    reconstructed = build_url(parsed)
    if reconstructed:
        result["reconstructed_url"] = reconstructed

    print(json.dumps(result, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Common utilities CLI (URL parsing)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported URL types:
  - Slack threads: {workspace}.slack.com/archives/{channel}/p{timestamp}
  - Linear issues: linear.app/{workspace}/issue/{identifier}
  - Linear projects: linear.app/{workspace}/project/{slug}
  - Linear initiatives: linear.app/{workspace}/initiative/{slug}
  - Avoma meetings: app.avoma.com/meeting/{uuid}
  - Google Docs: docs.google.com/document/d/{id}/edit
  - Google Sheets: docs.google.com/spreadsheets/d/{id}/edit
  - Google Slides: docs.google.com/presentation/d/{id}/edit
  - Notion pages: notion.so/{workspace}/{page-id}
  - Raw text: any non-URL input (extracts keywords)
""",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # parse-url
    p_parse = subparsers.add_parser("parse-url", help="Parse a URL or text input")
    p_parse.add_argument("input", help="URL or text to parse")
    p_parse.set_defaults(func=cmd_parse_url)

    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
