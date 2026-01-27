"""CLI interface for Google Drive integration.

Usage:
    uv run python -m integrations.google_drive <command> [options]

Commands:
    search              Search files and folders
    get-file            Get file metadata by ID
    export-file         Export Google Docs file to a format
    list-files          List files in a folder
"""

import argparse
import json
import sys

from .search import search
from .files import get_file, export_file, list_files


def cmd_search(args: argparse.Namespace) -> None:
    """Search files and folders."""
    result = search(
        query=args.query,
        page_size=args.page_size,
        page_token=args.page_token,
        include_trashed=args.include_trashed,
    )
    print(json.dumps(result, indent=2, default=str))


def cmd_get_file(args: argparse.Namespace) -> None:
    """Get file metadata by ID."""
    result = get_file(args.id)
    print(json.dumps(result, indent=2, default=str))


def cmd_export_file(args: argparse.Namespace) -> None:
    """Export Google Docs file to a format."""
    result = export_file(
        file_id=args.id,
        mime_type=args.mime_type,
    )
    # Export returns bytes, so we output as string or indicate binary
    if isinstance(result, bytes):
        try:
            print(result.decode("utf-8"))
        except UnicodeDecodeError:
            print(f"[Binary content, {len(result)} bytes]")
    else:
        print(json.dumps(result, indent=2, default=str))


def cmd_list_files(args: argparse.Namespace) -> None:
    """List files in a folder."""
    result = list_files(
        folder_id=args.folder_id,
        page_size=args.page_size,
        page_token=args.page_token,
    )
    print(json.dumps(result, indent=2, default=str))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Google Drive integration CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Query syntax examples:
  name contains 'report'
  mimeType = 'application/pdf'
  fullText contains 'quarterly budget'
  modifiedTime > '2026-01-01'
  'folder_id' in parents
""",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search
    p_search = subparsers.add_parser("search", help="Search files and folders")
    p_search.add_argument("--query", "-q", required=True, help="Drive query (e.g., \"fullText contains 'budget'\")")
    p_search.add_argument("--page-size", "-l", type=int, default=100, help="Results per page (max 1000)")
    p_search.add_argument("--page-token", help="Pagination token")
    p_search.add_argument("--include-trashed", action="store_true", help="Include trashed files")
    p_search.set_defaults(func=cmd_search)

    # get-file
    p_get = subparsers.add_parser("get-file", help="Get file metadata by ID")
    p_get.add_argument("--id", required=True, help="File ID")
    p_get.set_defaults(func=cmd_get_file)

    # export-file
    p_export = subparsers.add_parser("export-file", help="Export Google Docs file")
    p_export.add_argument("--id", required=True, help="File ID")
    p_export.add_argument("--mime-type", "-m", default="text/plain",
                          help="Export format (text/plain, text/html, application/pdf, etc.)")
    p_export.set_defaults(func=cmd_export_file)

    # list-files
    p_list = subparsers.add_parser("list-files", help="List files in a folder")
    p_list.add_argument("--folder-id", help="Folder ID (default: root)")
    p_list.add_argument("--page-size", "-l", type=int, default=100, help="Results per page")
    p_list.add_argument("--page-token", help="Pagination token")
    p_list.set_defaults(func=cmd_list_files)

    args = parser.parse_args()

    try:
        args.func(args)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
