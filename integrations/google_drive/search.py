"""Google Drive Search operations."""

from typing import Any

from .client import get_service
from .files import DEFAULT_FIELDS


def search(
    query: str,
    page_size: int = 100,
    page_token: str | None = None,
    order_by: str = "modifiedTime desc",
    fields: str = DEFAULT_FIELDS,
    include_trashed: bool = False,
) -> dict[str, Any]:
    """
    Search for files and folders in Google Drive.

    Args:
        query: Search query using Drive query syntax.
        page_size: Number of results per page (max 1000).
        page_token: Pagination token.
        order_by: Sort order.
        fields: Fields to return for each file.
        include_trashed: Include trashed files in results.

    Returns:
        Dict with 'files' list and pagination info.

    Query examples:
        - name contains 'report'
        - mimeType = 'application/pdf'
        - modifiedTime > '2026-01-01'
        - 'folder_id' in parents
        - fullText contains 'quarterly'
        - name contains 'budget' and mimeType = 'application/vnd.google-apps.spreadsheet'

    Example:
        # Search for PDFs containing "report"
        search(query="name contains 'report' and mimeType = 'application/pdf'")

        # Full text search
        search(query="fullText contains 'quarterly budget'")
    """
    full_query = query
    if not include_trashed:
        full_query = f"({query}) and trashed = false"

    params: dict[str, Any] = {
        "q": full_query,
        "pageSize": page_size,
        "orderBy": order_by,
        "fields": f"nextPageToken, files({fields})",
    }

    if page_token:
        params["pageToken"] = page_token

    result = get_service().files().list(**params).execute()

    return {
        "files": result.get("files", []),
        "nextPageToken": result.get("nextPageToken"),
    }
