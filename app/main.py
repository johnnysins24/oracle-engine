"""
The Oracle Engine - Universal AI Horoscope API
Main FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.routers import v1_tarot, v1_horoscope, v1_thai, v1_ai

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

# CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
