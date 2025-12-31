"""
Tarot Card Pydantic Models
Request and Response schemas for Tarot API
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class TarotCard(BaseModel):
    """Single Tarot Card representation"""
    id: int = Field(..., description="Unique card identifier (0-77)")
    name_en: str = Field(..., description="English card name")
    name_th: str = Field(..., description="Thai card name")
    arcana: str = Field(..., description="major or minor")
    suit: Optional[str] = Field(None, description="Suit for minor arcana (wands/cups/swords/pentacles)")
    keywords: List[str] = Field(..., description="Meaning keywords")
    image_url: str = Field(..., description="Card image URL")
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 0,
                "name_en": "The Fool",
                "name_th": "เดอะฟูล (คนโง่)",
                "arcana": "major",
                "suit": None,
                "keywords": ["new beginnings", "innocence", "adventure", "free spirit"],
                "image_url": "/assets/tarot/major/00-fool.jpg"
            }
        }


class DrawRequest(BaseModel):
    """Request for drawing tarot cards"""
    count: int = Field(1, ge=1, le=10, description="Number of cards to draw (1, 3, or 10)")
    spread_type: Optional[str] = Field(None, description="Spread type: single, past_present_future, celtic_cross")


class TarotDrawResponse(BaseModel):
    """Response containing drawn tarot cards"""
    spread_type: str = Field(..., description="Type of spread used")
    cards: List[TarotCard] = Field(..., description="List of drawn cards")
    positions: Optional[List[str]] = Field(None, description="Position meanings for each card")
    
    class Config:
        json_schema_extra = {
            "example": {
                "spread_type": "past_present_future",
                "cards": [],
                "positions": ["Past", "Present", "Future"]
            }
        }
