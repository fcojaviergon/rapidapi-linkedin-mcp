# File: prompts.py
from mcp.server.fastmcp.prompts import base
from typing import List, Optional

class LinkedInPrompts:
    """Prompts for the LinkedIn MCP server"""
    
    @staticmethod
    def search_people_prompt(keywords: Optional[str] = None) -> List[base.Message]:
        """
        Creates a prompt to search for people on LinkedIn
        
        Args:
            keywords: Optional keywords to include in the prompt
        
        Returns:
            List of messages for the prompt
        """
        messages = [
            base.UserMessage("I want to search for profiles on LinkedIn.")
        ]
        
        if keywords:
            messages.append(base.UserMessage(f"Search for profiles related to: {keywords}"))
        
        messages.append(base.AssistantMessage(
            "I will help you search for profiles on LinkedIn. I can search by keywords, "
            "location, name, last name, company and other filters. What type of profiles "
            "are you looking for?"
        ))
        
        return messages
    
    @staticmethod
    def profile_prompt(username: Optional[str] = None) -> List[base.Message]:
        """
        Creates a prompt to get information from a LinkedIn profile
        
        Args:
            username: Optional username to include in the prompt
        
        Returns:
            List of messages for the prompt
        """
        messages = [
            base.UserMessage("I want to get information from a LinkedIn profile.")
        ]
        
        if username:
            messages.append(base.UserMessage(f"Get information from the profile of: {username}"))
        
        messages.append(base.AssistantMessage(
            "I will help you get information from a LinkedIn profile. I need the username "
            "to search for the specific profile."
        ))
        
        return messages
    
    @staticmethod
    def profile_posts_prompt(username: Optional[str] = None) -> List[base.Message]:
        """
        Creates a prompt to get recent posts from a LinkedIn profile
        
        Args:
            username: Optional username to include in the prompt
        
        Returns:
            List of messages for the prompt
        """
        messages = [
            base.UserMessage("I want to see recent posts from a LinkedIn profile.")
        ]
        
        if username:
            messages.append(base.UserMessage(f"Get recent posts from the profile of: {username}"))
        
        messages.append(base.AssistantMessage(
            "I will help you get recent posts from a LinkedIn profile. I need the username "
            "to search for the specific profile."
        ))
        
        return messages
