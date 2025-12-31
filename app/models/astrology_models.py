"""
Astrology Pydantic Models
Request and Response schemas for Horoscope/Natal Chart API
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class NatalChartRequest(BaseModel):
    """Request for natal chart calculation"""
    birth_date: str = Field(
        ..., 
        description="วันเกิด (Birth date) - Format: YYYY-MM-DD เช่น 1990-05-15",
        examples=["1990-05-15"]
    )
    birth_time: str = Field(
        ..., 
        description="เวลาเกิด (Birth time) - Format: HH:MM (24-hour) เช่น 14:30",
        examples=["14:30"]
    )
    latitude: float = Field(..., ge=-90, le=90, description="Birth location latitude", examples=[13.7563])
    longitude: float = Field(..., ge=-180, le=180, description="Birth location longitude", examples=[100.5018])
    timezone_offset: str = Field("+00:00", description="UTC offset (e.g., +07:00 for Bangkok)", examples=["+07:00"])
    lang: str = Field("th", description="Response language: 'th' or 'en'", examples=["th"])

    class Config:
        json_schema_extra = {
            "example": {
                "birth_date": "1990-05-15",
                "birth_time": "14:30",
                "latitude": 13.7563,
                "longitude": 100.5018,
                "timezone_offset": "+07:00",
                "lang": "th"
            }
        }


class PlanetPosition(BaseModel):
    """Position of a celestial body"""
    planet_en: str = Field(..., description="Planet name in English")
    planet_th: str = Field(..., description="Planet name in Thai")
    sign_en: str = Field(..., description="Zodiac sign in English")
    sign_th: str = Field(..., description="Zodiac sign in Thai")
    degree: float = Field(..., description="Degree within the sign (0-30)")
    full_degree: float = Field(..., description="Absolute degree (0-360)")
    house: Optional[int] = Field(None, description="House placement (1-12)")
    retrograde: bool = Field(False, description="Whether planet is retrograde")


class HouseData(BaseModel):
    """Astrological house cusp data"""
    house_number: int = Field(..., ge=1, le=12, description="House number (1-12)")
    sign_en: str = Field(..., description="Sign on the cusp in English")
    sign_th: str = Field(..., description="Sign on the cusp in Thai")
    degree: float = Field(..., description="Degree of the cusp")


class ZodiacSign(BaseModel):
    """Zodiac sign information"""
    id: int = Field(..., ge=0, le=11, description="Sign ID (0-11)")
    name_en: str = Field(..., description="English name")
    name_th: str = Field(..., description="Thai name")
    symbol: str = Field(..., description="Zodiac symbol/emoji")
    element: str = Field(..., description="Element (Fire/Earth/Air/Water)")
    element_th: str = Field(..., description="Element in Thai")
    modality: str = Field(..., description="Modality (Cardinal/Fixed/Mutable)")
    ruling_planet: str = Field(..., description="Ruling planet")
    date_range: str = Field(..., description="Approximate date range")


class NatalChartResponse(BaseModel):
    """Complete natal chart response"""
    birth_data: dict = Field(..., description="Input birth data echoed back")
    
    # Main signs
    sun_sign: ZodiacSign = Field(..., description="Sun sign (core personality)")
    moon_sign: ZodiacSign = Field(..., description="Moon sign (emotions)")
    ascendant: ZodiacSign = Field(..., description="Rising sign (outer self)")
    
    # All planets
    planets: List[PlanetPosition] = Field(..., description="All planet positions")
    
    # Houses
    houses: List[HouseData] = Field(..., description="12 house cusps")


class SunSignRequest(BaseModel):
    """Simple request for sun sign lookup"""
    birth_date: str = Field(..., description="Birth date in YYYY-MM-DD format")
    lang: str = Field("th", description="Response language: 'th' or 'en'")


class SunSignResponse(BaseModel):
    """Simple sun sign response"""
    birth_date: str
    sun_sign: ZodiacSign
    message: str = Field(..., description="Personalized message about the sign")
