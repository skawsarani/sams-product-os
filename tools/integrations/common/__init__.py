"""Shared utilities for integrations."""

from .config import get_linear_api_key, get_slack_token, get_notion_token
from .utils import paginate, format_output, APIError
from .google_auth import build_calendar_service, build_drive_service
from .url_parser import (
    parse_input,
    parse_slack_url,
    parse_notion_url,
    parse_linear_url,
    parse_google_url,
    build_url,
    extract_keywords_from_text,
    is_url,
    ParsedInput,
    InputType,
)
__all__ = [
    # Config
    "get_linear_api_key",
    "get_slack_token",
    "get_notion_token",
    # Utils
    "paginate",
    "format_output",
    "APIError",
    # Google auth
    "build_calendar_service",
    "build_drive_service",
    # URL parser
    "parse_input",
    "parse_slack_url",
    "parse_notion_url",
    "parse_linear_url",
    "parse_google_url",
    "build_url",
    "extract_keywords_from_text",
    "is_url",
    "ParsedInput",
    "InputType",
]
