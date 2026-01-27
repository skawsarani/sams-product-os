"""Environment configuration for API integrations."""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root (two levels up from this file)
_project_root = Path(__file__).parent.parent.parent
_env_path = _project_root / ".env"
load_dotenv(_env_path)


def get_linear_api_key() -> str:
    """Get Linear API key from environment."""
    key = os.getenv("LINEAR_API_KEY")
    if not key:
        raise ValueError("LINEAR_API_KEY not set in environment")
    return key


def get_slack_token() -> str:
    """Get Slack user token from environment."""
    token = os.getenv("SLACK_USER_TOKEN")
    if not token:
        raise ValueError("SLACK_USER_TOKEN not set in environment")
    return token


def get_notion_token() -> str:
    """Get Notion integration token from environment."""
    token = os.getenv("NOTION_TOKEN")
    if not token:
        raise ValueError("NOTION_TOKEN not set in environment")
    return token


def get_avoma_api_key() -> str:
    """Get Avoma API key from environment."""
    key = os.getenv("AVOMA_API_KEY")
    if not key:
        raise ValueError("AVOMA_API_KEY not set in environment")
    return key


def get_google_oauth_client_file() -> Path:
    """
    Get the path to the Google OAuth client secrets file.

    Returns:
        Path to the client_secret.json file.

    Note:
        Download this file from Google Cloud Console:
        APIs & Services > Credentials > OAuth 2.0 Client IDs
    """
    file_path = os.getenv("GOOGLE_OAUTH_CLIENT_FILE", "./.secrets/client_secret.json")

    # If relative path, resolve from project root
    path = Path(file_path)
    if not path.is_absolute():
        path = _project_root / file_path

    return path


def get_google_token_file() -> Path:
    """
    Get the path to the Google OAuth token file.

    This file is auto-generated after the first successful OAuth flow
    and stores refresh tokens for seamless re-authentication.

    Returns:
        Path to the token file.
    """
    file_path = os.getenv("GOOGLE_TOKEN_FILE", "./.secrets/google_token.json")

    # If relative path, resolve from project root
    path = Path(file_path)
    if not path.is_absolute():
        path = _project_root / file_path

    return path


def get_hubspot_access_token() -> str:
    """Get HubSpot Private App access token from environment."""
    token = os.getenv("HUBSPOT_ACCESS_TOKEN")
    if not token:
        raise ValueError("HUBSPOT_ACCESS_TOKEN not set in environment")
    return token
