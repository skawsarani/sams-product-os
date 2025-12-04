# MCP Servers

This directory contains MCP server implementations that extend your PM Co-Pilot with real-time data access.

## What's Here

- `example-server.py`: A template MCP server showing basic patterns
- Your custom servers go here

## Server Requirements

### Python Version
Python 3.10 or higher

### Dependencies

```bash
pip install mcp anthropic-mcp python-dotenv
```

Or use the requirements file:

```bash
pip install -r requirements.txt
```

## Creating a New Server

### 1. Start from Template

Copy `example-server.py` and rename:

```bash
cp example-server.py my-custom-server.py
```

### 2. Define Your Tools

```python
@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="your-tool-name",
            description="What your tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "What this param is for"
                    }
                },
                "required": ["param1"]
            }
        )
    ]
```

### 3. Implement Tool Logic

```python
@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "your-tool-name":
        # Your implementation
        result = do_something(arguments["param1"])
        return [TextContent(type="text", text=str(result))]
```

### 4. Configure in AI Assistant

Add to Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "my-custom-server": {
      "command": "python",
      "args": ["/absolute/path/to/mcp/servers/my-custom-server.py"]
    }
  }
}
```

## Example Servers

### Project Management Integration

**jira-server.py** (example):

```python
from mcp.server import Server
from mcp.types import Tool, TextContent
import os
from jira import JIRA

server = Server("jira-pm-tool")

jira = JIRA(
    server=os.getenv("JIRA_URL"),
    basic_auth=(os.getenv("JIRA_EMAIL"), os.getenv("JIRA_API_TOKEN"))
)

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="fetch-sprint-tickets",
            description="Fetch tickets for current sprint",
            inputSchema={
                "type": "object",
                "properties": {
                    "board_id": {"type": "string"}
                }
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "fetch-sprint-tickets":
        board_id = arguments["board_id"]
        sprint = jira.sprints(board_id, state="active")[0]
        issues = jira.search_issues(f'sprint={sprint.id}')
        
        result = []
        for issue in issues:
            result.append(f"{issue.key}: {issue.fields.summary}")
        
        return [TextContent(
            type="text",
            text="\n".join(result)
        )]
```

### Analytics Integration

**analytics-server.py** (example):

```python
from mcp.server import Server
from mcp.types import Tool, TextContent
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest
import os

server = Server("analytics-pm-tool")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get-key-metrics",
            description="Fetch key product metrics for a date range",
            inputSchema={
                "type": "object",
                "properties": {
                    "start_date": {"type": "string"},
                    "end_date": {"type": "string"}
                }
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get-key-metrics":
        client = BetaAnalyticsDataClient()
        property_id = os.getenv("GA_PROPERTY_ID")
        
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[{
                "start_date": arguments["start_date"],
                "end_date": arguments["end_date"]
            }],
            metrics=[
                {"name": "activeUsers"},
                {"name": "sessions"},
                {"name": "conversions"}
            ]
        )
        
        response = client.run_report(request)
        
        # Format response
        metrics_text = []
        for row in response.rows:
            metrics_text.append(
                f"Active Users: {row.metric_values[0].value}\n"
                f"Sessions: {row.metric_values[1].value}\n"
                f"Conversions: {row.metric_values[2].value}"
            )
        
        return [TextContent(type="text", text="\n".join(metrics_text))]
```

## Testing Your Server

### Command Line Test

```bash
python your-server.py
```

Should start without errors and wait for connections.

### MCP Inspector

Best way to test tools:

```bash
npx @modelcontextprotocol/inspector python your-server.py
```

Opens a web UI where you can:
- See available tools
- Test tool execution
- View responses
- Debug issues

### Integration Test

1. Add server to Claude/Cursor config
2. Restart AI assistant
3. Test with natural language:
   ```
   "Use the jira-pm-tool to fetch current sprint tickets for board 123"
   ```

## Environment Variables

Create a `.env` file in the MCP directory:

```bash
# Jira
JIRA_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@domain.com
JIRA_API_TOKEN=your_token_here

# Linear
LINEAR_API_KEY=your_linear_key

# Google Analytics
GA_PROPERTY_ID=your_property_id
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json

# Custom APIs
CUSTOM_API_URL=https://api.example.com
CUSTOM_API_KEY=your_key
```

Load in your server:

```python
from dotenv import load_dotenv
load_dotenv()  # Loads .env from current directory
```

## Error Handling

Always handle errors gracefully:

```python
@server.call_tool()
async def call_tool(name: str, arguments: dict):
    try:
        if name == "fetch-data":
            result = fetch_from_api(arguments)
            return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}\nPlease check your configuration."
        )]
```

## Logging

Add logging for debugging:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    logger.info(f"Calling tool: {name} with args: {arguments}")
    # ... tool logic
```

Logs will help you debug when the server is running in the background.

## Performance Tips

1. **Cache Results**: Cache API responses when appropriate
2. **Rate Limiting**: Respect API rate limits
3. **Async Operations**: Use async for I/O operations
4. **Timeout Handling**: Add timeouts to external calls

```python
import asyncio
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_api_call(key):
    # Expensive operation
    pass

async def call_with_timeout():
    try:
        result = await asyncio.wait_for(
            external_api_call(),
            timeout=5.0
        )
        return result
    except asyncio.TimeoutError:
        return "API call timed out"
```

## Common Patterns

### Pagination

```python
def fetch_all_pages(api_call, **kwargs):
    all_results = []
    page = 1
    while True:
        response = api_call(page=page, **kwargs)
        all_results.extend(response.items)
        if not response.has_next:
            break
        page += 1
    return all_results
```

### Authentication

```python
from requests.auth import HTTPBasicAuth
import requests

def make_authenticated_request(url):
    auth = HTTPBasicAuth(
        os.getenv("API_USER"),
        os.getenv("API_PASS")
    )
    response = requests.get(url, auth=auth)
    return response.json()
```

### Response Formatting

```python
def format_for_ai(data):
    """Format data in a way that's easy for AI to consume"""
    if isinstance(data, list):
        return "\n\n".join([format_item(item) for item in data])
    elif isinstance(data, dict):
        return "\n".join([f"{k}: {v}" for k, v in data.items()])
    else:
        return str(data)
```

## Server Lifecycle

### Initialization

```python
async def main():
    # Setup code
    logger.info("Starting server...")
    await server.run()
```

### Cleanup

```python
import signal

def signal_handler(signum, frame):
    logger.info("Shutting down gracefully...")
    # Cleanup code
    exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
```

## Troubleshooting

### Server Won't Start

- Check Python version: `python --version` (need 3.10+)
- Install dependencies: `pip install -r requirements.txt`
- Check for syntax errors: `python -m py_compile your-server.py`

### AI Can't Connect

- Verify absolute path in config
- Check file permissions: `chmod +x your-server.py`
- Look at AI assistant logs
- Test server manually first

### Tools Not Working

- Check tool name matches exactly
- Verify input schema is correct
- Add logging to see what's being called
- Test with MCP Inspector

## Resources

- [MCP Python SDK Docs](https://github.com/anthropics/mcp-python)
- [MCP Specification](https://github.com/anthropics/mcp)
- Example servers: [MCP Servers Repo](https://github.com/anthropics/mcp-servers)

