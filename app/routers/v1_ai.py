"""
AI Interpretation API Router
Endpoints for AI-powered fortune interpretation
"""

from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.core.ai_client import generate_interpretation
from app.core.prompts import (
    TAROT_GYPSY_PROMPT,
    THAI_FORTUNE_PROMPT,
    WESTERN_ASTROLOGER_PROMPT,
    build_tarot_prompt,
    build_thai_prompt,
    build_natal_prompt
)
from app.engines.tarot import draw_single, draw_three, draw_celtic_cross
from app.engines.thai_astrology import get_thai_reading
from app.engines.astrology import calculate_natal_chart

router = APIRouter(prefix="/v1/ai", tags=["AI Interpretation"])

# Rate limiter - 10 requests per minute for AI endpoints
limiter = Limiter(key_func=get_remote_address)


# ============================================================================
# REQUEST/RESPONSE MODELS
# ============================================================================

class TarotInterpretRequest(BaseModel):
    """Request for AI tarot interpretation"""
    count: int = Field(1, ge=1, le=10, description="Number of cards (1, 3, or 10)")
    question: Optional[str] = Field(None, description="คำถามที่ต้องการถาม เช่น 'ความรัก' 'การงาน'", examples=["ความรัก", "การเงิน"])
    lang: str = Field("th", description="Response language: 'th' or 'en'")

    class Config:
        json_schema_extra = {
            "example": {
                "count": 3,
                "question": "ความรักของฉันในปีหน้าจะเป็นอย่างไร",
                "lang": "th"
            }
        }


class ThaiInterpretRequest(BaseModel):
    """Request for AI Thai fortune interpretation"""
    birth_date: str = Field(..., description="วันเกิด Format: YYYY-MM-DD", examples=["1990-05-15"])
    birth_time: Optional[str] = Field(None, description="เวลาเกิด Format: HH:MM", examples=["14:30"])
    question: Optional[str] = Field(None, description="คำถามที่ต้องการถาม", examples=["ดวงการเงินปีหน้า"])

    class Config:
        json_schema_extra = {
            "example": {
                "birth_date": "1990-05-15",
                "birth_time": "14:30",
                "question": "ดวงการเงินปีหน้าจะเป็นอย่างไร"
            }
        }


class NatalInterpretRequest(BaseModel):
    """Request for AI natal chart interpretation"""
    birth_date: str = Field(..., description="Format: YYYY-MM-DD")
    birth_time: str = Field(..., description="Format: HH:MM")
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    timezone_offset: str = Field("+00:00")
    question: Optional[str] = Field(None)
    lang: str = Field("th")


class InterpretResponse(BaseModel):
    """AI interpretation response"""
    interpretation: str = Field(..., description="AI generated interpretation")
    data: Dict = Field(..., description="Raw calculation data used")


# ============================================================================
# ENDPOINTS
# ============================================================================

@router.post("/tarot", response_model=InterpretResponse, summary="AI Tarot Reading 🔮")
@limiter.limit("10/minute")
async def interpret_tarot(request: Request, body: TarotInterpretRequest):
    """
    Draw tarot cards and get AI interpretation.
    
    - **count**: 1 = guidance, 3 = past/present/future, 10 = celtic cross
    - **question**: Optional question in Thai or English
    - **lang**: Response language ('th' or 'en')
    
    Uses the "แม่หมอยิปซี" (Gypsy Fortune Teller) persona for Thai readings.
    """
    # Draw cards based on count - functions return tuple (cards, spread_type, positions)
    if body.count == 1:
        card, spread_type, positions = draw_single()
        cards = [card]  # Single card needs to be wrapped in list
    elif body.count == 3:
        cards, spread_type, positions = draw_three()
    elif body.count == 10:
        cards, spread_type, positions = draw_celtic_cross()
    else:
        card, spread_type, positions = draw_single()
        cards = [card]
    
    # Build prompt
    prompt = build_tarot_prompt(cards, body.question, spread_type, body.lang)
    
    # Get AI interpretation
    system_prompt = TAROT_GYPSY_PROMPT
    interpretation = await generate_interpretation(prompt, system_instruction=system_prompt)
    
    return InterpretResponse(
        interpretation=interpretation,
        data={
            "cards": [{"name_th": c["name_th"], "name_en": c["name_en"]} for c in cards],
            "spread_type": spread_type,
            "positions": positions
        }
    )


@router.post("/thai", response_model=InterpretResponse, summary="AI Thai Fortune 🇹🇭")
@limiter.limit("10/minute")
async def interpret_thai(request: Request, body: ThaiInterpretRequest):
    """
    Get AI Thai fortune reading based on birth data.
    
    Uses the "อาจารย์หมอดู" (Thai Astrologer) persona.
    
    Includes: ปีนักษัตร, วันเกิด, ลัคนา (if birth time provided)
    """
    try:
        # Get Thai reading data
        reading = get_thai_reading(body.birth_date, body.birth_time)
        
        # Build prompt
        prompt = build_thai_prompt(reading, body.question)
        
        # Get AI interpretation
        interpretation = await generate_interpretation(prompt, system_instruction=THAI_FORTUNE_PROMPT)
        
        return InterpretResponse(
            interpretation=interpretation,
            data={
                "year_animal": reading["year_animal"]["name_th"],
                "birth_day": reading["birth_day"]["name_th"],
                "lagna": reading["lagna"]["name_th"] if reading["lagna"] else None
            }
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")


@router.post("/natal", response_model=InterpretResponse, summary="AI Natal Chart Reading ⭐")
@limiter.limit("10/minute")
async def interpret_natal(request: Request, body: NatalInterpretRequest):
    """
    Get AI interpretation of Western natal chart.
    
    Requires birth date, time, and location for accurate calculation.
    """
    try:
        # Calculate natal chart
        chart = calculate_natal_chart(
            body.birth_date,
            body.birth_time,
            body.latitude,
            body.longitude,
            body.timezone_offset
        )
        
        # Build prompt
        prompt = build_natal_prompt(chart, body.question, body.lang)
        
        # Get AI interpretation
        system_prompt = THAI_FORTUNE_PROMPT if body.lang == "th" else WESTERN_ASTROLOGER_PROMPT
        interpretation = await generate_interpretation(prompt, system_instruction=system_prompt)
        
        return InterpretResponse(
            interpretation=interpretation,
            data={
                "sun_sign": chart["sun_sign"]["name_th"] if body.lang == "th" else chart["sun_sign"]["name_en"],
                "moon_sign": chart["moon_sign"]["name_th"] if body.lang == "th" else chart["moon_sign"]["name_en"],
                "ascendant": chart["ascendant"]["name_th"] if body.lang == "th" else chart["ascendant"]["name_en"]
            }
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Chart calculation error: {str(e)}")
