"""
Thai Astrology Pydantic Models
Request and Response schemas for Thai Horoscope API
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class ThaiYearAnimal(BaseModel):
    """Thai zodiac year animal (ปีนักษัตร)"""
    id: int = Field(..., ge=0, le=11, description="นักษัตร ID (0-11)")
    name_th: str = Field(..., description="Thai name (e.g., ปีชวด)")
    animal_th: str = Field(..., description="Animal name in Thai (e.g., หนู)")
    animal_en: str = Field(..., description="Animal name in English (e.g., Rat)")
    element: str = Field(..., description="Element (Water/Wood/Fire/Earth/Metal)")
    element_th: str = Field(..., description="Element in Thai")
    characteristics: List[str] = Field(..., description="Personality traits")


class ThaiBirthDay(BaseModel):
    """Thai birth day information (วันเกิด)"""
    day_number: int = Field(..., ge=0, le=6, description="Day number (0=Sunday)")
    name_th: str = Field(..., description="Thai day name")
    name_en: str = Field(..., description="English day name")
    ruling_planet_th: str = Field(..., description="Ruling planet in Thai")
    ruling_planet_en: str = Field(..., description="Ruling planet in English")
    color: str = Field(..., description="Lucky color")
    color_th: str = Field(..., description="Lucky color in Thai")
    characteristics: List[str] = Field(..., description="Personality traits")


class ThaiLagna(BaseModel):
    """Thai Lagna (ลัคนา) information"""
    lagna_id: int = Field(..., ge=0, le=11, description="Lagna ID (0-11)")
    name_th: str = Field(..., description="Thai name (e.g., ลัคนาราศีเมษ)")
    rasi_th: str = Field(..., description="Rasi name in Thai")
    rasi_en: str = Field(..., description="Rasi name in English")
    meaning: str = Field(..., description="Meaning and influence")


class ThaiReadingRequest(BaseModel):
    """Request for Thai horoscope reading"""
    birth_date: str = Field(
        ..., 
        description="วันเกิด (Birth date)",
        json_schema_extra={"format": "YYYY-MM-DD", "example": "1990-05-15", "placeholder": "1990-05-15"}
    )
    birth_time: Optional[str] = Field(
        None, 
        description="เวลาเกิด (Birth time) - optional",
        json_schema_extra={"format": "HH:MM", "example": "14:30", "placeholder": "14:30"}
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "birth_date": "1990-05-15",
                "birth_time": "14:30"
            }
        }


class ThaiReadingResponse(BaseModel):
    """Full Thai horoscope reading response"""
    birth_date: str
    birth_time: Optional[str]
    
    year_animal: ThaiYearAnimal = Field(..., description="ปีนักษัตร")
    birth_day: ThaiBirthDay = Field(..., description="วันเกิด")
    lagna: Optional[ThaiLagna] = Field(None, description="ลัคนา (if birth time provided)")
    
    summary_th: str = Field(..., description="Summary in Thai")


class NaksatResponse(BaseModel):
    """Simple นักษัตร lookup response"""
    birth_year: int
    thai_year: int = Field(..., description="Buddhist Era year (พ.ศ.)")
    year_animal: ThaiYearAnimal
    message: str
