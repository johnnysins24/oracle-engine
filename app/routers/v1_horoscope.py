"""
Horoscope API Router
Endpoints for natal charts and zodiac information
"""

from fastapi import APIRouter, HTTPException
from typing import Optional

from app.models.astrology_models import (
    NatalChartRequest, NatalChartResponse,
    SunSignRequest, SunSignResponse,
    ZodiacSign, PlanetPosition, HouseData
)
from app.engines.astrology import (
    calculate_natal_chart,
    get_sun_sign_from_date,
    get_all_zodiac_signs,
    get_sign_by_id,
    ZODIAC_SIGNS
)

router = APIRouter(tags=["Horoscope"])


@router.post("/v1/horoscope/natal", response_model=NatalChartResponse, summary="Calculate natal chart")
async def create_natal_chart(request: NatalChartRequest):
    """
    Calculate a complete natal chart based on birth data.
    
    Requires:
    - **birth_date**: YYYY-MM-DD format
    - **birth_time**: HH:MM format (24-hour)
    - **latitude/longitude**: Birth location coordinates
    - **timezone_offset**: UTC offset (e.g., +07:00 for Bangkok)
    
    Returns sun sign, moon sign, ascendant, planet positions, and house cusps.
    """
    try:
        chart_data = calculate_natal_chart(
            birth_date=request.birth_date,
            birth_time=request.birth_time,
            latitude=request.latitude,
            longitude=request.longitude,
            timezone_offset=request.timezone_offset
        )
        
        return NatalChartResponse(
            birth_data={
                "date": request.birth_date,
                "time": request.birth_time,
                "latitude": request.latitude,
                "longitude": request.longitude,
                "timezone": request.timezone_offset
            },
            sun_sign=ZodiacSign(**chart_data["sun_sign"]),
            moon_sign=ZodiacSign(**chart_data["moon_sign"]),
            ascendant=ZodiacSign(**chart_data["ascendant"]),
            planets=[PlanetPosition(**p) for p in chart_data["planets"]],
            houses=[HouseData(**h) for h in chart_data["houses"]]
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Chart calculation error: {str(e)}")


@router.get("/v1/horoscope/sun-sign", response_model=SunSignResponse, summary="Get sun sign from birth date")
async def get_sun_sign(birth_date: str, lang: str = "th"):
    """
    Get sun sign from birth date only.
    
    Simple lookup - no birth time or location needed.
    
    - **birth_date**: YYYY-MM-DD format
    - **lang**: Response language ('th' or 'en')
    """
    try:
        sign_data = get_sun_sign_from_date(birth_date)
        
        # Create personalized message
        if lang == "th":
            message = f"คุณเกิดในราศี{sign_data['name_th']} ({sign_data['symbol']}) ซึ่งเป็น{sign_data['element_th']}"
        else:
            message = f"You were born under {sign_data['name_en']} ({sign_data['symbol']}), a {sign_data['element']} sign"
        
        return SunSignResponse(
            birth_date=birth_date,
            sun_sign=ZodiacSign(**sign_data),
            message=message
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format. Use YYYY-MM-DD. Error: {str(e)}")


@router.get("/test/zodiac", summary="Get all zodiac signs")
async def get_zodiac_signs():
    """
    Returns all 12 zodiac signs with Thai translations.
    
    Useful for building UI dropdowns or reference.
    """
    return {
        "total_signs": 12,
        "signs": [ZodiacSign(**sign) for sign in ZODIAC_SIGNS]
    }


@router.get("/test/zodiac/{sign_id}", summary="Get zodiac sign by ID")
async def get_zodiac_by_id(sign_id: int):
    """
    Get a specific zodiac sign by ID (0-11).
    
    - 0: Aries, 1: Taurus, 2: Gemini, 3: Cancer
    - 4: Leo, 5: Virgo, 6: Libra, 7: Scorpio
    - 8: Sagittarius, 9: Capricorn, 10: Aquarius, 11: Pisces
    """
    if sign_id < 0 or sign_id > 11:
        raise HTTPException(status_code=400, detail="Sign ID must be between 0 and 11")
    
    sign = get_sign_by_id(sign_id)
    return ZodiacSign(**sign)
