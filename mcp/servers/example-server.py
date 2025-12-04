#!/usr/bin/env python3
"""
Example MCP Server for PM Co-Pilot
This is a template showing how to build custom MCP servers for PM workflows.
"""

import asyncio
import logging
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create server instance
server = Server("pm-copilot-example")

@server.list_tools()
async def list_tools() -> list[Tool]:
    """
    Define the tools this server provides.
    Each tool should have:
    - name: unique identifier
    - description: what the tool does (helps AI decide when to use it)
    - inputSchema: JSON schema defining parameters
    """
    return [
        Tool(
            name="fetch-backlog-stats",
            description="Get statistics about backlog items (count by priority, status, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "backlog_file": {
                        "type": "string",
                        "description": "Path to backlog file (relative to project root)"
                    }
                },
                "required": ["backlog_file"]
            }
        ),
        Tool(
            name="calculate-velocity",
            description="Calculate team velocity based on completed stories",
            inputSchema={
                "type": "object",
                "properties": {
                    "sprint_count": {
                        "type": "integer",
                        "description": "Number of past sprints to analyze"
                    },
                    "team": {
                        "type": "string",
                        "description": "Team name (optional)"
                    }
                }
            }
        ),
        Tool(
            name="summarize-metrics",
            description="Summarize key product metrics from a metrics file",
            inputSchema={
                "type": "object",
                "properties": {
                    "metrics_file": {
                        "type": "string",
                        "description": "Path to metrics file"
                    },
                    "timeframe": {
                        "type": "string",
                        "description": "Timeframe to analyze (e.g., 'last-week', 'last-month')"
                    }
                }
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """
    Execute a tool based on its name and provided arguments.
    Returns a list of TextContent objects that the AI can read.
    """
    logger.info(f"Tool called: {name} with arguments: {arguments}")
    
    try:
        if name == "fetch-backlog-stats":
            result = await fetch_backlog_stats(arguments["backlog_file"])
            return [TextContent(type="text", text=result)]
        
        elif name == "calculate-velocity":
            result = await calculate_velocity(
                arguments.get("sprint_count", 3),
                arguments.get("team", "all")
            )
            return [TextContent(type="text", text=result)]
        
        elif name == "summarize-metrics":
            result = await summarize_metrics(
                arguments["metrics_file"],
                arguments.get("timeframe", "last-week")
            )
            return [TextContent(type="text", text=result)]
        
        else:
            return [TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]
    
    except Exception as e:
        logger.error(f"Error executing tool {name}: {str(e)}")
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}\n\nPlease check the tool parameters and try again."
        )]

# Tool implementations

async def fetch_backlog_stats(backlog_file: str) -> str:
    """
    Example: Analyze a backlog file and return statistics.
    In a real implementation, you'd read the actual file and parse it.
    """
    # This is a mock implementation
    # In reality, you'd:
    # 1. Read the file from the workspace
    # 2. Parse the content (markdown, CSV, JSON, etc.)
    # 3. Calculate actual statistics
    
    return f"""
Backlog Statistics for {backlog_file}:

Total Items: 47
- P0 (Critical): 3
- P1 (High): 12
- P2 (Medium): 18
- P3 (Low): 14

By Status:
- Not Started: 32
- In Progress: 8
- Blocked: 3
- In Review: 4

Average Age: 12 days
Oldest Item: 45 days
Newest Item: 1 day

Recommendations:
- You have 3 P0 items - these should be addressed immediately
- 3 blocked items need attention
- 32 items are not started - consider prioritization session
"""

async def calculate_velocity(sprint_count: int, team: str) -> str:
    """
    Example: Calculate team velocity.
    In a real implementation, you'd fetch data from Jira, Linear, etc.
    """
    # Mock implementation
    # Real version would:
    # 1. Connect to project management tool
    # 2. Fetch completed stories for last N sprints
    # 3. Calculate actual velocity
    
    return f"""
Team Velocity Analysis (Last {sprint_count} sprints - {team}):

Sprint History:
- Sprint 10: 34 points
- Sprint 9: 28 points
- Sprint 8: 31 points

Average Velocity: 31 points per sprint
Trend: +18% vs previous 3 sprints

Predictive Capacity:
- Next sprint estimated capacity: 31-35 points
- Confidence level: High (low variance)

Notes:
- Velocity trending upward
- Team capacity stable
- Recommend planning for 32 points to account for holidays
"""

async def summarize_metrics(metrics_file: str, timeframe: str) -> str:
    """
    Example: Summarize metrics from a file.
    Real implementation would parse actual metrics data.
    """
    # Mock implementation
    # Real version would:
    # 1. Read metrics file
    # 2. Parse data (JSON, CSV, etc.)
    # 3. Calculate changes and trends
    
    return f"""
Metrics Summary ({metrics_file} - {timeframe}):

Key Metrics:
📈 Active Users: 12,450 (+8% vs previous period)
📊 Daily Active Users: 3,200 (+5%)
💰 Conversion Rate: 4.2% (-0.3%)
⭐ NPS Score: 42 (+2 points)

Engagement:
- Session Duration: 8.5 min (+12%)
- Feature Adoption (new feature): 23% of users
- Retention (Day 7): 62% (↔️ flat)

Top Performing Features:
1. Dashboard: 85% of users, +15% usage
2. Reports: 67% of users, +8% usage
3. Integrations: 45% of users, +22% usage

Areas Needing Attention:
⚠️ Conversion rate declined - investigate checkout flow
⚠️ Mobile app crashes up 15% - bug fix needed

Recommendations:
1. Investigate conversion rate drop (A/B test checkout changes?)
2. Prioritize mobile stability
3. Double down on Dashboard (high engagement)
4. Promote Integrations feature (high growth)
"""

# Server startup

async def main():
    """
    Main entry point for the MCP server.
    """
    logger.info("Starting PM Co-Pilot Example MCP Server...")
    logger.info("Server is ready to accept connections")
    
    # Run the server
    # The AI assistant will connect to this server and can call the tools
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server shutting down...")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        raise

