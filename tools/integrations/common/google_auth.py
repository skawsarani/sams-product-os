"""Google OAuth authentication for Google APIs."""

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build, Resource

from .config import get_google_oauth_client_file, get_google_token_file

# Read-only scopes for Calendar and Drive access
SCOPES = [
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]


def get_credentials() -> Credentials:
    """
    Get or refresh OAuth credentials.

    On first run, opens a browser window for user authentication.
    Subsequent runs use the stored refresh token.

    Returns:
        Authenticated credentials object.

    Raises:
        FileNotFoundError: If client_secret.json is not found.
    """
    creds = None
    token_path = get_google_token_file()
    client_secrets_path = get_google_oauth_client_file()

    # Load existing token if available
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)

    # If no valid credentials, refresh or run auth flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh expired token
            creds.refresh(Request())
        else:
            # Run OAuth flow (opens browser)
            if not client_secrets_path.exists():
                raise FileNotFoundError(
                    f"Google OAuth client secrets file not found: {client_secrets_path}\n"
                    "Download from Google Cloud Console: APIs & Services > Credentials > OAuth 2.0 Client IDs\n"
                    "Set GOOGLE_OAUTH_CLIENT_FILE in .env or place client_secret.json in project root."
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                str(client_secrets_path), SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save token for next run
        with open(token_path, "w") as f:
            f.write(creds.to_json())

    return creds


def build_calendar_service() -> Resource:
    """
    Build Google Calendar API service.

    Returns:
        Google Calendar API service resource.
    """
    credentials = get_credentials()
    return build("calendar", "v3", credentials=credentials)


def build_drive_service() -> Resource:
    """
    Build Google Drive API service.

    Returns:
        Google Drive API service resource.
    """
    credentials = get_credentials()
    return build("drive", "v3", credentials=credentials)
