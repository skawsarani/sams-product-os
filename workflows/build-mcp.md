---
allowed-tools: Skill, Read, Write, Glob, Bash(npm:*), Bash(python:*), Bash(uv:*)
argument-hint: [MCP server name or description]
description: Create an MCP server with guided workflow
---

## Context

MCP (Model Context Protocol) servers enable Claude to interact with external services through well-designed tools.

The mcp-builder skill provides expert guidance for building high-quality MCP servers in Python (FastMCP) or Node/TypeScript (MCP SDK).

## Your task

Guide the user through creating a new MCP server or enhancing an existing one.

User input: $ARGUMENTS

**Steps:**

1. **Invoke mcp-builder**: Use the Skill tool to launch the mcp-builder skill

2. **Pass user context**: Include $ARGUMENTS to provide context about what MCP server they want to create

**Example invocation:**
- `/build-mcp notion integration` → Create an MCP server for Notion API
- `/build-mcp` → Interactive workflow to design a new MCP server
- `/build-mcp enhance task-manager-mcp` → Update existing task-manager-mcp

**Important:**
- The mcp-builder will handle the full workflow (language selection, tool design, implementation, etc.)
- MCP servers can be in Python (FastMCP) or Node/TypeScript (MCP SDK)
- MCP servers expose tools that Claude can invoke during conversations
