"""
Oracle Engine Configuration
Environment variable management
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    """Application settings from environment variables"""
    
    # API Settings
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    
    # App Metadata
    APP_NAME: str = "The Oracle Engine"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "Universal AI Horoscope API - Thai, Western & Tarot"
    
    # Google Gemini AI
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Future: Database
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    
    # Future: Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "")


settings = Settings()
