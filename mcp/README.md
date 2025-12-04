# MCP (Model Context Protocol) Integration

This directory contains MCP server and client configurations for extending your PM Co-Pilot with real-time data integrations and custom tools.

## What is MCP?

Model Context Protocol (MCP) is a standard for connecting AI assistants to external data sources and tools. It allows your AI assistant to:

- Fetch real-time data from APIs (Jira, Linear, Analytics, etc.)
- Execute custom tools and scripts
- Access databases and external systems
- Provide up-to-date context beyond static files

## Directory Structure

```
mcp/
├── servers/           # MCP server implementations
│   ├── example-server.py
│   └── README.md
├── clients/           # Client configurations
│   ├── claude-config.json
│   ├── cursor-config.json
│   └── README.md
└── README.md         # This file
```

## Quick Start

### 1. For Claude Desktop

Add MCP server configuration to your Claude Desktop config:

**Location**: 
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

**Example config**:
```json
{
  "mcpServers": {
    "pm-tools": {
      "command": "python",
      "args": ["/path/to/pm-copilot/mcp/servers/pm-tools-server.py"]
    }
  }
}
```

### 2. For Cursor

Cursor supports MCP through similar configuration. See `clients/cursor-config.json` for examples.

### 3. Test Your Server

```bash
# Test the server directly
python mcp/servers/example-server.py
```

## Available Integrations

### Built-in Examples

1. **example-server.py**: Template server showing basic MCP implementation
   - File reading
   - Data fetching
   - Tool execution

### Custom Servers You Can Build

**Project Management Tools**:
- Jira ticket fetching
- Linear issue sync
- Asana task integration

**Analytics & Metrics**:
- Google Analytics data
- Mixpanel events
- Custom dashboards

**Communication**:
- Slack message search
- Email summaries
- Meeting transcript access

**Documentation**:
- Confluence page access
- Notion database queries
- Google Docs integration

## Creating Your Own MCP Server

### Basic Server Template

See `servers/example-server.py` for a complete example.

```python
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("my-pm-tool")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="fetch-metrics",
            description="Fetch key product metrics",
            inputSchema={
                "type": "object",
                "properties": {
                    "metric": {"type": "string"},
                    "timeframe": {"type": "string"}
                }
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "fetch-metrics":
        # Your logic here
        return [TextContent(type="text", text="Metrics data...")]
```

### Common Use Cases

**1. Fetch Jira Tickets**
```python
@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "fetch-jira-tickets":
        project = arguments.get("project")
        # Use Jira API to fetch tickets
        tickets = fetch_from_jira(project)
        return format_response(tickets)
```

**2. Get Analytics Data**
```python
if name == "get-analytics":
    metric = arguments.get("metric")
    # Fetch from your analytics platform
    data = analytics_client.get_metric(metric)
    return format_response(data)
```

**3. Search Documentation**
```python
if name == "search-docs":
    query = arguments.get("query")
    # Search Confluence, Notion, etc.
    results = doc_search(query)
    return format_response(results)
```

## Security Best Practices

### Environment Variables

Never commit credentials. Use environment variables:

```python
import os

API_KEY = os.getenv("JIRA_API_KEY")
API_URL = os.getenv("JIRA_URL")
```

### .env File

Create a `.env` file (gitignored):

```bash
JIRA_API_KEY=your_key_here
JIRA_URL=https://your-domain.atlassian.net
LINEAR_API_KEY=your_linear_key
GOOGLE_ANALYTICS_ID=your_ga_id
```

Load with python-dotenv:

```python
from dotenv import load_dotenv
load_dotenv()
```

## Testing Your Server

### Manual Testing

```bash
# Run the server
python mcp/servers/your-server.py

# In another terminal, test with MCP inspector
npx @modelcontextprotocol/inspector python mcp/servers/your-server.py
```

### Integration Testing

Test with your AI assistant:
1. Configure the server in Claude/Cursor
2. Restart the AI assistant
3. Ask it to use your tool: "Fetch my Jira tickets"

## Common Issues

### Server Won't Start
- Check Python version (3.10+ required)
- Install dependencies: `pip install mcp anthropic-mcp`
- Verify file permissions

### AI Can't Access Server
- Check config file location
- Verify JSON syntax in config
- Restart AI assistant after config changes
- Check server logs for errors

### Authentication Errors
- Verify API keys in environment variables
- Check API permissions
- Test API access with curl/Postman first

## Examples by Use Case

### For Sprint Planning

**Server capabilities**:
- Fetch backlog from project management tool
- Get velocity data
- Check team capacity
- Pull in blockers

**Sample command to AI**:
```
"Fetch our backlog for the mobile team and help me plan next sprint"
```

### For Stakeholder Updates

**Server capabilities**:
- Fetch latest metrics from analytics
- Get ticket completion status
- Pull recent customer feedback

**Sample command to AI**:
```
"Get the latest metrics and draft an exec update"
```

### For Research Synthesis

**Server capabilities**:
- Search interview transcripts
- Fetch user feedback from support tool
- Get NPS scores and comments

**Sample command to AI**:
```
"Search all interviews about checkout flow and synthesize findings"
```

## Resources

### Official Documentation
- [MCP Specification](https://github.com/anthropics/mcp)
- [MCP Python SDK](https://github.com/anthropics/mcp-python)
- [Claude MCP Documentation](https://docs.anthropic.com/claude/docs/mcp)

### Example Servers
- [MCP Servers Repository](https://github.com/anthropics/mcp-servers)
- Community examples on GitHub

### Getting Help
- MCP Discord community
- GitHub issues on MCP repos
- This repo's issues

## Contribution

Built a useful MCP server for PM workflows? Consider:
1. Adding it to `servers/` with documentation
2. Sharing configuration in `clients/`
3. Adding to this README

## License

Same as main project (MIT)

