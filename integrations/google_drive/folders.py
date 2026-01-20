"""Google Drive Folders read operations."""

from typing import Any

from .client import get_service
from .files import DEFAULT_FIELDS

FOLDER_MIME_TYPE = "application/vnd.google-apps.folder"


def get_folder(folder_id: str, fields: str = DEFAULT_FIELDS) -> dict[str, Any] | None:
    """
    Get folder metadata.

    Args:
        folder_id: Folder ID.
        fields: Fields to return.

    Returns:
        Folder metadata or None if not found.
    """
    try:
        result = get_service().files().get(fileId=folder_id, fields=fields).execute()
        if result.get("mimeType") == FOLDER_MIME_TYPE:
            return result
        return None
    except Exception:
        return None


def list_folders(
    parent_id: str | None = None,
    page_size: int = 100,
    page_token: str | None = None,
    order_by: str = "name",
    fields: str = DEFAULT_FIELDS,
) -> dict[str, Any]:
    """
    List folders in Drive or within a specific folder.

    Args:
        parent_id: Parent folder ID (None for root level).
        page_size: Number of folders per page.
        page_token: Pagination token.
        order_by: Sort order.
        fields: Fields to return for each folder.

    Returns:
        Dict with 'folders' list and pagination info.
    """
    query_parts = [f"mimeType = '{FOLDER_MIME_TYPE}'", "trashed = false"]

    if parent_id:
        query_parts.append(f"'{parent_id}' in parents")

    params: dict[str, Any] = {
        "q": " and ".join(query_parts),
        "pageSize": page_size,
        "orderBy": order_by,
        "fields": f"nextPageToken, files({fields})",
    }

    if page_token:
        params["pageToken"] = page_token

    result = get_service().files().list(**params).execute()

    return {
        "folders": result.get("files", []),
        "nextPageToken": result.get("nextPageToken"),
    }
