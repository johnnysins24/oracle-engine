"""
The Oracle Engine - Universal AI Horoscope API
Main FastAPI Application Entry Point
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.core.config import settings
from app.routers import v1_tarot, v1_horoscope, v1_thai, v1_ai

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)

# Initialize FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_tags=[
        {
            "name": "AI Interpretation",
            "description": "ดูดวงด้วย AI - Tarot, Thai Fortune, Natal Chart"
        },
        {
            "name": "Thai Astrology",
            "description": "Thai horoscope endpoints (ปีนักษัตร, วันเกิด, ลัคนา)"
        },
        {
            "name": "Horoscope",
            "description": "Western natal chart and zodiac sign endpoints"
        },
        {
            "name": "Tarot Test",
            "description": "Test endpoints for Tarot card drawing"
        },
        {
            "name": "Health",
            "description": "API health and status"
        }
    ]
)

# Attach rate limiter to app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS middleware - whitelist only allowed origins
ALLOWED_ORIGINS = [
    "https://oracle-web-nine.vercel.app",
    "http://localhost:3000",  # Local development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

# Include routers
app.include_router(v1_ai.router)
app.include_router(v1_thai.router)
app.include_router(v1_horoscope.router)
app.include_router(v1_tarot.router)


@app.get("/", tags=["Health"])
async def root():
    """
    Health check endpoint.
    Returns API status and version information.
    """
    return {
        "status": "online",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "message": "🔮 The Oracle Engine is ready to divine your fate!"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Detailed health check for monitoring systems.
    """
    return {
        "status": "healthy",
        "components": {
            "tarot_engine": "operational",
            "western_astrology": "operational",
            "thai_astrology": "operational",
            "ai_interpreter": "pending",      # Phase 2
            "cache": "pending",               # Phase 4
            "database": "pending"             # Phase 4
        }
    }
