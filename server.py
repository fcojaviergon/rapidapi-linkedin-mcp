# File: server.py
import os
from mcp.server.fastmcp import FastMCP

import tools
import prompts
from config import LinkedInConfig

class LinkedInMCPServerHelper:
    """Class to configure the MCP server for LinkedIn API"""

    def __init__(self, name: str = "LinkedIn MCP Server"):
        """
        Initialize the MCP server
        
        Args:
            name: Server name
        """
        # Validate that the API key is configured
        if not LinkedInConfig.RAPIDAPI_KEY:
            print("WARNING: RAPIDAPI_KEY not configured. Add it to the .env file to use the server")
        
        self.name = name
        self.tools_instance = tools.LinkedInTools()
        self.prompts_instance = prompts.LinkedInPrompts()

    def configure_server(self, mcp_instance: FastMCP) -> None:
        """
        Configure an MCP server with all tools and prompts
        
        Args:
            mcp_instance: FastMCP instance to configure
        """
        # Register tools
        mcp_instance.tool()(self.tools_instance.search_people)
        mcp_instance.tool()(self.tools_instance.get_profile)
        mcp_instance.tool()(self.tools_instance.get_profile_posts)
        
        # Register prompts
        mcp_instance.prompt()(self.prompts_instance.search_people_prompt)
        mcp_instance.prompt()(self.prompts_instance.profile_prompt)
        mcp_instance.prompt()(self.prompts_instance.profile_posts_prompt)

# Create the main FastMCP instance - IMPORTANT: This is the object that MCP CLI searches for
mcp = FastMCP("LinkedIn MCP Server")

# Configure the server
helper = LinkedInMCPServerHelper()
helper.configure_server(mcp)

# Main entry point if run directly
if __name__ == "__main__":
    print(f"Starting LinkedIn MCP server...")
    print(f"API host: {LinkedInConfig.RAPIDAPI_HOST}")
    
    # Determine the transport from environment variable if available
    transport = os.environ.get("MCP_TRANSPORT", "http")
    print(f"Using transport: {transport}")
    
    # Get port from environment variable (for services like Render, Heroku, etc.)
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    
    # Run the server with the appropriate parameters for production environment
    if transport == "http":
        print(f"Server listening on {host}:{port}")
        mcp.run(transport=transport, host=host, port=port)
    else:
        mcp.run(transport=transport)