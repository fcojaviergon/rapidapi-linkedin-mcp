# File: config.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LinkedInConfig:
    """Configuration for the LinkedIn MCP server"""
    
    # RapidAPI configuration
    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")
    RAPIDAPI_HOST = "linkedin-data-api.p.rapidapi.com"
    BASE_URL = "https://linkedin-data-api.p.rapidapi.com"
    
    @classmethod
    def get_headers(cls):
        """Returns the headers for requests to RapidAPI"""
        return {
            "X-RapidAPI-Key": cls.RAPIDAPI_KEY,
            "X-RapidAPI-Host": cls.RAPIDAPI_HOST,
        }
