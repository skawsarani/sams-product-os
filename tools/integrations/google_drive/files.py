"""Google Drive Files read operations."""

from typing import Any
import io

from googleapiclient.http import MediaIoBaseDownload

from .client import get_service

# Common file fields to return
DEFAULT_FIELDS = "id, name, mimeType, size, createdTime, modifiedTime, parents, webViewLink"


def get_file(file_id: str, fields: str = DEFAULT_FIELDS) -> dict[str, Any] | None:
    """
    Get file metadata.

    Args:
        file_id: File ID.
        fields: Fields to return (comma-separated).

    Returns:
        File metadata or None if not found.
    """
    try:
        return get_service().files().get(fileId=file_id, fields=fields).execute()
    except Exception:
        return None


def list_files(
    folder_id: str | None = None,
    page_size: int = 100,
    page_token: str | None = None,
    order_by: str = "modifiedTime desc",
    fields: str = DEFAULT_FIELDS,
) -> dict[str, Any]:
    """
    List files in Drive or a specific folder.

    Args:
        folder_id: Parent folder ID (None for all accessible files).
        page_size: Number of files per page (max 1000).
        page_token: Pagination token.
        order_by: Sort order (e.g., 'name', 'modifiedTime desc').
        fields: Fields to return for each file.

    Returns:
        Dict with 'files' list and pagination info.
    """
    params: dict[str, Any] = {
        "pageSize": page_size,
        "orderBy": order_by,
        "fields": f"nextPageToken, files({fields})",
    }

    if folder_id:
        params["q"] = f"'{folder_id}' in parents and trashed = false"
    else:
        params["q"] = "trashed = false"

    if page_token:
        params["pageToken"] = page_token

    result = get_service().files().list(**params).execute()

    return {
        "files": result.get("files", []),
        "nextPageToken": result.get("nextPageToken"),
    }


def download_file(file_id: str) -> bytes:
    """
    Download a file's content.

    Args:
        file_id: File ID to download.

    Returns:
        File content as bytes.

    Note:
        For Google Docs/Sheets/Slides, use export_file instead.
    """
    request = get_service().files().get_media(fileId=file_id)
    buffer = io.BytesIO()
    downloader = MediaIoBaseDownload(buffer, request)

    done = False
    while not done:
        _, done = downloader.next_chunk()

    return buffer.getvalue()


def export_file(file_id: str, mime_type: str = "text/markdown") -> bytes:
    """
    Export a Google Docs/Sheets/Slides file to a specific format.

    Args:
        file_id: File ID to export.
        mime_type: Target format.

    Returns:
        File content as bytes.

    Recommended formats:
        - Google Docs: 'text/markdown'
        - Google Sheets: 'text/csv'
        - Google Slides: 'application/pdf'
    """
    return get_service().files().export(fileId=file_id, mimeType=mime_type).execute()
