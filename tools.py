# File: tools.py
import json
import httpx
from typing import Dict, Any, List, Optional
from mcp.types import TextContent

from config import LinkedInConfig

class LinkedInTools:
    """Tools for the LinkedIn MCP server"""
    
    def __init__(self):
        """Initialize the tools with the configuration"""
        self._base_url = LinkedInConfig.BASE_URL
        self._headers = LinkedInConfig.get_headers()
    
    def _format_response(self, data: Dict[str, Any]) -> Dict[str, List[TextContent]]:
        """Format the data for the MCP response"""
        return {
            "content": [
                TextContent(
                    type="text",
                    text=json.dumps(data, indent=4)
                )
            ]
        }
    
    async def _fetch_api_data(self, endpoint: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Helper method to fetch data from the API (GET requests)"""
        try:
            async with httpx.AsyncClient() as client:
                url = f"{self._base_url}{endpoint}"
                response = await client.get(
                    url,
                    params=params,
                    headers=self._headers,
                    timeout=30.0
                )
                
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            return {
                "success": False,
                "message": f"Error from RapidAPI: {e.response.status_code} - {e.response.text}",
                "data": None,
            }
        except httpx.RequestError as e:
            return {
                "success": False,
                "message": f"Error from connection: {str(e)}",
                "data": None,
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Unexpected error: {str(e)}",
                "data": None,
            }
    
    async def search_people(
        self, 
        keywords: Optional[str] = None,
        start: Optional[str] = "0",
        geo: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        company: Optional[str] = None,
        school_id: Optional[str] = None,
        keyword_school: Optional[str] = None,
        keyword_title: Optional[str] = None
    ) -> Dict[str, List[TextContent]]:
        """
        Search for people on LinkedIn with different filters
        
        Args:
            keywords: Keywords for the search
            start: Pagination start point (0, 10, 20, etc.)
            geo: Location ID (e.g: 103644278,101165590)
            first_name: First name
            last_name: Last name
            company: Company name
            school_id: School ID
            keyword_school: School keyword
            keyword_title: Title keyword
            
        Returns:
            Search results
        """
        params = {}
        if keywords:
            params["keywords"] = keywords
        if start:
            params["start"] = start
        if geo:
            params["geo"] = geo
        if first_name:
            params["firstName"] = first_name
        if last_name:
            params["lastName"] = last_name
        if company:
            params["company"] = company
        if school_id:
            params["schoolId"] = school_id
        if keyword_school:
            params["keywordSchool"] = keyword_school
        if keyword_title:
            params["keywordTitle"] = keyword_title
            
        data = await self._fetch_api_data("/search-people", params)
        return self._format_response(data)
    
    async def get_profile(self, username: str) -> Dict[str, List[TextContent]]:
        """
        Get the profile of a LinkedIn user by username
        
        Args:
            username: LinkedIn username
            
        Returns:
            Profile data
        """
        data = await self._fetch_api_data("/", {"username": username})
        return self._format_response(data)
    
    async def get_profile_posts(
        self, 
        username: str,
        start: Optional[str] = None,
        pagination_token: Optional[str] = None,
        posted_at: Optional[str] = None
    ) -> Dict[str, List[TextContent]]:
        """
        Get the posts of a LinkedIn profile
        
        Args:
            username: LinkedIn username
            start: Pagination start point (0, 50, 100, etc.)
            pagination_token: Pagination token for next pages
            posted_at: Filter by post date (e.g: 2024-01-01 00:00)
            
        Returns:
            Profile posts
        """
        params = {"username": username}
        if start:
            params["start"] = start
        if pagination_token:
            params["paginationToken"] = pagination_token
        if posted_at:
            params["postedAt"] = posted_at
            
        data = await self._fetch_api_data("/get-profile-posts", params)
        return self._format_response(data)
