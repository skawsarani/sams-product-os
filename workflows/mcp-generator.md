## MCP Server Generator Expert

Expert workflow for generating MCP (Model Context Protocol) servers from API documentation, SDKs, or tool specifications. Creates Python MCP server code, tool definitions, and .env configuration templates.

---

### Generate MCP Server from API Docs

```
Generate MCP server for [API/service name] using [API docs/SDK]
```

**What it does**:
- Analyzes API documentation or SDK
- Generates Python MCP server code
- Creates tool definitions for API endpoints
- Generates .env template with required variables
- Provides setup and configuration instructions

**When to use**: Creating MCP servers to integrate external APIs or tools

**Detailed Steps**:

1. **Analyze API Documentation**
   - Review API documentation or SDK
   - Identify key endpoints and operations
   - Understand authentication methods (API keys, OAuth, etc.)
   - Note required parameters and response formats
   - Identify rate limits and constraints

2. **Design Tool Definitions**
   - Map API endpoints to MCP tools
   - Group related operations
   - Define input schemas based on API parameters
   - Create descriptive tool names and descriptions
   - Consider tool granularity (one endpoint per tool vs grouped operations)

3. **Generate Server Code**
   - Use `mcp/servers/example-server.py` as template
   - Create tool definitions in `list_tools()`
   - Implement tool handlers in `call_tool()`
   - Add error handling and validation
   - Include logging and debugging support

4. **Create .env Template**
   - Identify all required environment variables
   - Document each variable's purpose
   - Provide example values (without secrets)
   - Note where to obtain credentials
   - Include optional configuration variables

5. **Generate Setup Instructions**
   - Installation steps
   - Environment variable setup
   - Authentication configuration
   - Testing instructions
   - Integration with Claude/Cursor

---

### Create MCP Server from SDK

```
Create MCP server from [SDK/library] for [purpose]
```

**What it does**:
- Analyzes SDK or library documentation
- Generates MCP tools wrapping SDK functions
- Creates server code with proper SDK integration
- Generates .env for SDK configuration

**When to use**: Wrapping existing SDKs as MCP servers

**Detailed Steps**:

1. **Review SDK Documentation**
   - Understand SDK structure and methods
   - Identify key functions to expose
   - Note initialization requirements
   - Understand error handling patterns

2. **Map SDK Functions to Tools**
   - Group related SDK methods
   - Create intuitive tool names
   - Define input schemas matching SDK parameters
   - Handle SDK-specific types and objects

3. **Generate Integration Code**
   - Import and initialize SDK
   - Wrap SDK calls in tool handlers
   - Convert SDK responses to MCP format
   - Handle SDK errors appropriately

4. **Create Configuration**
   - Document SDK initialization requirements
   - Create .env template for SDK config
   - Include authentication setup
   - Note any SDK-specific requirements

---

### Generate .env Template

```
Generate .env template for MCP server [server-name]
```

**What it does**:
- Creates .env.example file with all required variables
- Documents each variable's purpose
- Provides example values
- Includes instructions for obtaining credentials

**When to use**: Setting up environment variables for MCP servers

**Detailed Steps**:

1. **Identify Required Variables**
   - API keys and tokens
   - Base URLs and endpoints
   - Authentication credentials
   - Optional configuration

2. **Create Template File**
   - Use `.env.example` naming convention
   - Group related variables
   - Add comments explaining each variable
   - Include example values (non-sensitive)

3. **Document Credential Sources**
   - Where to obtain API keys
   - How to create OAuth credentials
   - Account setup requirements
   - Security best practices

4. **Add to Documentation**
   - Update `mcp/README.md` with server-specific setup
   - Include .env setup in server documentation
   - Add troubleshooting section for common issues

---

### Update MCP Server Documentation

```
Update MCP documentation for [server-name]
```

**What it does**:
- Adds server documentation to `mcp/README.md`
- Creates server-specific README if needed
- Documents available tools and capabilities
- Includes usage examples

**When to use**: After creating a new MCP server

**Detailed Steps**:

1. **Document Server Capabilities**
   - List all available tools
   - Describe what each tool does
   - Include example use cases

2. **Add Setup Instructions**
   - Installation steps
   - Environment variable configuration
   - Authentication setup
   - Testing the server

3. **Include Usage Examples**
   - Example tool calls
   - Expected responses
   - Common workflows
   - Integration examples

4. **Update Main README**
   - Add server to available integrations list
   - Link to server documentation
   - Include in quick start guide

---

### Analyze API and Suggest Tools

```
Analyze [API docs] and suggest MCP tools
```

**What it does**:
- Reviews API documentation
- Suggests logical tool groupings
- Recommends tool names and descriptions
- Identifies authentication requirements
- Flags potential issues or complexities

**When to use**: Planning MCP server before implementation

**Detailed Steps**:

1. **Review API Structure**
   - Identify main resources/entities
   - Group related endpoints
   - Understand data flow
   - Note authentication needs

2. **Suggest Tool Organization**
   - Logical grouping of operations
   - Tool naming conventions
   - Input/output schemas
   - Error handling approach

3. **Identify Requirements**
   - Authentication method
   - Required environment variables
   - Dependencies and libraries
   - Rate limits and constraints

4. **Provide Recommendations**
   - Tool design suggestions
   - Implementation approach
   - Potential challenges
   - Best practices

---

### Create MCP Server from OpenAPI/Swagger

```
Generate MCP server from OpenAPI spec [file/URL]
```

**What it does**:
- Parses OpenAPI/Swagger specification
- Generates MCP server with tools for each endpoint
- Creates proper request/response handling
- Generates .env for API configuration

**When to use**: When OpenAPI/Swagger spec is available

**Detailed Steps**:

1. **Parse OpenAPI Spec**
   - Read specification file
   - Extract endpoints and schemas
   - Understand authentication schemes
   - Identify request/response models

2. **Generate Tool Definitions**
   - Create tool for each endpoint
   - Map OpenAPI parameters to tool inputs
   - Use OpenAPI schemas for validation
   - Generate response handling

3. **Create Server Implementation**
   - Generate HTTP client code
   - Implement authentication
   - Handle request/response conversion
   - Add error handling

4. **Generate Configuration**
   - Extract base URL and endpoints
   - Document authentication requirements
   - Create .env template
   - Include setup instructions

---

### Best Practices

**Tool Design**:
- Keep tools focused and single-purpose
- Use descriptive names that indicate what they do
- Group related operations when it makes sense
- Design input schemas to be intuitive
- Include helpful descriptions for AI to understand when to use each tool

**Error Handling**:
- Catch and handle API errors gracefully
- Return clear error messages
- Log errors for debugging
- Handle rate limits appropriately
- Validate inputs before API calls

**Security**:
- Never hardcode credentials
- Use environment variables for all secrets
- Document security best practices
- Include .gitignore for .env files
- Use secure credential storage

**Documentation**:
- Document all tools and their purposes
- Include setup instructions
- Provide usage examples
- Document authentication flow
- Include troubleshooting guide

**Code Quality**:
- Follow Python best practices
- Use type hints where possible
- Add logging for debugging
- Include error handling
- Write clear, maintainable code

---

### Example Workflow

**User**: "Generate MCP server for Linear API"

**Steps**:
1. Analyze Linear API documentation
2. Identify key operations (get issues, create issue, update issue, etc.)
3. Design tools: `get-linear-issues`, `create-linear-issue`, `update-linear-issue`, etc.
4. Generate Python server code with Linear API client integration
5. Create .env template with `LINEAR_API_KEY` variable
6. Document setup: "Get API key from Linear Settings → API"
7. Update `mcp/README.md` with Linear server documentation
8. Provide testing instructions

**Output**:
- `mcp/servers/linear-server.py`
- `mcp/.env.example` (or `.env/linear.example`)
- Updated `mcp/README.md` with Linear integration section
