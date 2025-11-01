# GeeksHacking MCP - TODO Management Server

A Model Context Protocol (MCP) server for managing and tracking #TODO comments from source code files.

## Overview

GeeksHacking MCP is an MCP server that provides tools and resources for tracking TODO comments scattered across your codebase. It stores TODO items with their source file location and line numbers, making it easy to manage and query pending tasks directly from your development environment.

## Features

- **Add TODOs**: Register TODO comments from any source file with line number tracking
- **Query TODOs**: Retrieve all TODO items for a specific file
- **Persistent Storage**: Stores TODO items in a JSON database
- **MCP Integration**: Works seamlessly with MCP-compatible clients (like Claude Desktop, Cline, etc.)

## Installation

### Prerequisites

- Python 3.13 or higher
- `uv` package manager (recommended) or `pip`

### Install via uv

```bash
uvx --from git+https://github.com/JiaweiLin/geekshacking-mcp.git todo_mcp
```

### Install from source

```bash
# Clone the repository
git clone https://github.com/JiaweiLin/geekshacking-mcp.git
cd geekshacking-mcp

# Install dependencies
uv sync

# Run the server
uv run todo_mcp
```

## Usage

### As an MCP Server

Add the following configuration to your MCP client configuration file (e.g., Claude Desktop's config):

```json
{
  "mcpServers": {
    "todo_mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/JiaweiLin/geekshacking-mcp.git",
        "todo_mcp"
      ]
    }
  }
}
```

Or if installed locally:

```json
{
  "mcpServers": {
    "todo_mcp": {
      "command": "uv",
      "args": ["run", "todo_mcp"],
      "cwd": "/path/to/geekshacking-mcp"
    }
  }
}
```

### Available Tools

#### `tool_add_todo`

Add a single #TODO text from a source file.

**Parameters:**
- `filename` (string): Source file containing the #TODO
- `line_num` (integer): Line number of the #TODO
- `text` (string): #TODO text to add

**Example:**
```json
{
  "filename": "src/main.py",
  "line_num": 42,
  "text": "Refactor this function for better performance"
}
```

### Available Resources

#### `resource_get_todos_for_file`

Get all #TODO texts for a source file.

**URI Pattern:** `todo://{filename}/todos`

**Parameters:**
- `filename` (string): Source file containing the #TODO

**Returns:** Array of TODO text strings (empty array if no TODOs exist for the file)

**Example URI:** `todo://src/main.py/todos`

## Database

TODO items are stored in a JSON file at:
```
src/todo_mcp/todo_db.json
```

The database structure:
```json
{
  "filename.ext": {
    "_10": "TODO text at line 10",
    "_20": "TODO text at line 20"
  }
}
```

## Development

### Project Structure

```
geekshacking-mcp/
├── src/
│   └── todo_mcp/
│       ├── __init__.py
│       ├── todo_mcp.py      # MCP server implementation
│       └── todo_db.py        # Database management
├── pyproject.toml            # Project configuration
├── uv.lock                   # Dependency lock file
└── README.md
```

### Setting up for Development

```bash
# Install development dependencies
uv sync

# Run the server locally
uv run todo_mcp

# Run tests (if available)
uv run pytest
```

### Dependencies

- `fastmcp>=2.13.0.2` - FastMCP framework for building MCP servers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Links

- [Model Context Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/JiaweiLin/geekshacking-mcp).
