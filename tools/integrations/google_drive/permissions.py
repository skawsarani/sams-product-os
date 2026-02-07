"""Google Drive Permissions read operations."""

from typing import Any

from .client import get_service


def list_permissions(
    file_id: str,
    page_size: int = 100,
    page_token: str | None = None,
) -> dict[str, Any]:
    """
    List permissions on a file or folder.

    Args:
        file_id: File or folder ID.
        page_size: Number of permissions per page.
        page_token: Pagination token.

    Returns:
        Dict with 'permissions' list and pagination info.
    """
    params: dict[str, Any] = {
        "fileId": file_id,
        "pageSize": page_size,
        "fields": "nextPageToken, permissions(id, type, role, emailAddress, domain)",
    }

    if page_token:
        params["pageToken"] = page_token

    result = get_service().permissions().list(**params).execute()

    return {
        "permissions": result.get("permissions", []),
        "nextPageToken": result.get("nextPageToken"),
    }
