# LinkedIn MCP Server

A MCP server to access the LinkedIn API through RapidAPI, based on the FastMCP framework.

## Features

- Search for LinkedIn profiles
- Get detailed information about profiles
- Get recent posts from profiles

## Requirements

- Python 3.12 or higher
- A RapidAPI API key for [LinkedIn Data API](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8)
- UV (fast Python installer)

## Installation

### Install UV

If you don't have UV installed, you can install it with the following command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Install the MCP server

1. Clone this repository and navigate to the folder:
   ```bash
   git clone https://github.com/fcojaviergon/linkedin-mcp.git
   cd linkedin-mcp
   ```

2. Install dependencies using UV:
   ```bash
   uv pip install -e .
   ```

3. Create a `.env` file with your API key:
   ```
   RAPIDAPI_KEY=your_rapidapi_key_here
   ```

## Usage

### Run the server directly

To run the server manually:

```bash
uv run mcp run server.py
```

### Configure with Claude Desktop

Add this configuration to your MCP configuration file:

- For Claude Desktop: `/path/to/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "LinkedIn MCP Server": {
      "command": "/path/to/uv/.local/bin/uv",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/path/to/projects/rapidapi-linkedin-mcp/server.py"
      ]
    }
  }
}
```

Make sure to replace `/path/to/uv/.local/bin/uv` with the actual path to your UV installation and `/path/to/projects/rapidapi-linkedin-mcp/server.py` with the full path to the `server.py` file.

## Tools available

### search_people

Search for LinkedIn profiles with various filters.

Parameters:
- `keywords` (optional): Keywords for the search
- `start` (optional): Pagination start point (0, 10, 20, etc.)
- `geo` (optional): Location ID
- `first_name` (optional): First name
- `last_name` (optional): Last name
- `company` (optional): Company name
- `school_id` (optional): School ID
- `keyword_school` (optional): School keyword
- `keyword_title` (optional): Title keyword

### get_profile

Get detailed information about a LinkedIn profile.

Parameters:
- `username` (required): LinkedIn username

### get_profile_posts

Get recent posts from a LinkedIn profile.

Parameters:
- `username` (required): LinkedIn username
- `start` (optional): Pagination start point (0, 10, 20, etc.)
- `pagination_token` (optional): Pagination token
- `posted_at` (optional): Filter by post date

## Prompts available

- `search_people_prompt`: To search for profiles
- `profile_prompt`: To get information about profiles
- `profile_posts_prompt`: To get recent posts from profiles

## Examples of usage from an agent

```python
from mcp.client import MCPClient

# Connect to the server
client = MCPClient("http://localhost:8000")

# Search for profiles
result = await client.invoke_tool("search_people", {
    "keywords": "developer",
    "company": "Google"
})

# Get profile
profile = await client.invoke_tool("get_profile", {
    "username": "satyanadella"
})

# Get recent posts
posts = await client.invoke_tool("get_profile_posts", {
    "username": "billgates"
})
```

## Troubleshooting

- If you receive an authentication error, verify that your API key in the `.env` file is correct
- Make sure you have an active subscription to the LinkedIn endpoint in RapidAPI
- If you have issues with UV, you can use pip directly: `pip install -e .`
