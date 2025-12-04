# MCP Client Configurations

This directory contains example configurations for connecting your AI assistants to MCP servers.

## Claude Desktop Configuration

### Location

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`  
**Linux**: `~/.config/Claude/claude_desktop_config.json`

### Basic Configuration

```json
{
  "mcpServers": {
    "pm-copilot": {
      "command": "python",
      "args": ["/absolute/path/to/pm-copilot/mcp/servers/example-server.py"]
    }
  }
}
```

### Multiple Servers

```json
{
  "mcpServers": {
    "pm-copilot-example": {
      "command": "python",
      "args": ["/absolute/path/to/pm-copilot/mcp/servers/example-server.py"]
    },
    "jira-integration": {
      "command": "python",
      "args": ["/absolute/path/to/pm-copilot/mcp/servers/jira-server.py"],
      "env": {
        "JIRA_URL": "https://your-domain.atlassian.net",
        "JIRA_EMAIL": "your-email@domain.com"
      }
    },
    "analytics": {
      "command": "python",
      "args": ["/absolute/path/to/pm-copilot/mcp/servers/analytics-server.py"]
    }
  }
}
```

### With Environment Variables

```json
{
  "mcpServers": {
    "pm-tools": {
      "command": "python",
      "args": ["/absolute/path/to/pm-copilot/mcp/servers/your-server.py"],
      "env": {
        "API_KEY": "your-api-key-here",
        "API_URL": "https://api.example.com",
        "LOG_LEVEL": "INFO"
      }
    }
  }
}
```

**Note**: For better security, use a .env file instead of hardcoding credentials in the config.

### Using a Virtual Environment

If you're using a Python virtual environment:

```json
{
  "mcpServers": {
    "pm-copilot": {
      "command": "/absolute/path/to/pm-copilot/venv/bin/python",
      "args": ["/absolute/path/to/pm-copilot/mcp/servers/example-server.py"]
    }
  }
}
```

## Cursor Configuration

Cursor supports MCP through similar configuration patterns.

### Config Location

Check Cursor's documentation for the exact location, typically:
- Cursor settings → MCP configuration
- Or a config file in Cursor's application directory

### Example Cursor Config

```json
{
  "mcp": {
    "servers": {
      "pm-copilot": {
        "command": "python",
        "args": ["/absolute/path/to/pm-copilot/mcp/servers/example-server.py"]
      }
    }
  }
}
```

## VS Code with Continue

If using Continue extension for VS Code:

### Config Location

`.continue/config.json` in your workspace or home directory

### Example Configuration

```json
{
  "mcpServers": [
    {
      "name": "pm-copilot",
      "command": "python",
      "args": ["/absolute/path/to/pm-copilot/mcp/servers/example-server.py"]
    }
  ]
}
```

## Testing Your Configuration

### 1. Verify Paths

Make sure all paths are absolute:

```bash
# macOS/Linux
which python  # Use this in "command"
pwd  # Get absolute path to your server

# Windows
where python
cd  # Get current directory
```

### 2. Test Server Manually

Before configuring your AI assistant, test the server:

```bash
cd /path/to/pm-copilot
python mcp/servers/example-server.py
```

Should start without errors.

### 3. Restart AI Assistant

After updating the config:
1. Completely quit the AI assistant
2. Restart it
3. The MCP servers should be loaded

### 4. Verify Connection

In Claude Desktop, you can check if servers are connected:
- Look for indicators in the UI
- Try asking: "What MCP tools do you have access to?"

### 5. Test Tool Execution

Ask the AI to use one of your tools:

```
"Use the pm-copilot server to fetch backlog stats for backlog/current-ideas.md"
```

## Troubleshooting

### Config Not Loading

**Check JSON Syntax**:
```bash
# macOS/Linux with jq
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json | jq .

# Or use an online JSON validator
```

**Common Issues**:
- Missing commas between entries
- Missing quotes around strings
- Trailing commas (not allowed in JSON)

### Server Not Starting

**Check Logs**:

Claude Desktop logs (macOS):
```bash
tail -f ~/Library/Logs/Claude/mcp*.log
```

**Verify Python Path**:
```bash
python --version  # Should be 3.10+
which python      # Should match "command" in config
```

**Check Dependencies**:
```bash
cd /path/to/pm-copilot
pip install -r mcp/servers/requirements.txt
```

### AI Can't Access Tools

1. **Restart AI Assistant**: Close completely and reopen
2. **Check Server Name**: Must match in config and server code
3. **Look at Logs**: Check AI assistant logs for connection errors
4. **Test Server Independently**: Use MCP inspector

```bash
npx @modelcontextprotocol/inspector python mcp/servers/example-server.py
```

### Permission Errors

**macOS/Linux**:
```bash
chmod +x mcp/servers/*.py
```

**Make sure Python can execute**:
```bash
ls -la mcp/servers/example-server.py
```

## Environment Variables Best Practices

### Don't Put Secrets in Config

❌ **Bad** (credentials in config):
```json
{
  "mcpServers": {
    "jira": {
      "env": {
        "JIRA_API_KEY": "my-secret-key-123"
      }
    }
  }
}
```

✅ **Good** (use .env file):

**In .env** (gitignored):
```bash
JIRA_API_KEY=my-secret-key-123
```

**In server code**:
```python
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("JIRA_API_KEY")
```

**In config**:
```json
{
  "mcpServers": {
    "jira": {
      "command": "python",
      "args": ["/path/to/jira-server.py"]
    }
  }
}
```

## Advanced Configuration

### Server with Additional Python Path

```json
{
  "mcpServers": {
    "pm-copilot": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "env": {
        "PYTHONPATH": "/path/to/custom/modules"
      }
    }
  }
}
```

### Server with Working Directory

```json
{
  "mcpServers": {
    "pm-copilot": {
      "command": "python",
      "args": ["/path/to/server.py"],
      "cwd": "/path/to/pm-copilot"
    }
  }
}
```

### Conditional Configuration

You can maintain different configs for different environments:

```bash
# Development
cp client-configs/claude-dev.json ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Production
cp client-configs/claude-prod.json ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

## Example Configs

See these example files:
- `claude-config-example.json` - Basic Claude Desktop setup
- `claude-config-multi-server.json` - Multiple servers
- `cursor-config-example.json` - Cursor setup

Copy and modify for your needs.

## Resources

- [Claude MCP Documentation](https://docs.anthropic.com/claude/docs/mcp)
- [MCP Specification](https://github.com/anthropics/mcp)
- [Cursor Documentation](https://cursor.sh/docs)
- [Continue Documentation](https://continue.dev/docs)

