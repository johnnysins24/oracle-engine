"""
Thai Astrology API Router
Endpoints for Thai horoscope (โหราศาสตร์ไทย)
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.models.thai_astrology_models import (
    ThaiYearAnimal, ThaiBirthDay, ThaiLagna,
    ThaiReadingRequest, ThaiReadingResponse, NaksatResponse
)
from app.engines.thai_astrology import (
    get_thai_year_animal,
    get_thai_birth_day,
    calculate_thai_lagna,
    get_thai_reading,
    gregorian_to_thai_year,
    THAI_YEAR_ANIMALS,
    THAI_BIRTH_DAYS,
    THAI_LAGNA
)

router = APIRouter(prefix="/v1/thai", tags=["Thai Astrology"])


@router.get("/naksat", response_model=NaksatResponse, summary="Get ปีนักษัตร from birth year")
async def get_naksat(
    birth_year: int = Query(..., description="ปี ค.ศ. เช่น 1990, 2000", examples=[1990, 2000])
):
    """
    Get Thai zodiac year animal (ปีนักษัตร) from birth year.
    
    - **birth_year**: ปี ค.ศ. (Gregorian year) เช่น 1990
    
    Returns the zodiac animal, element, and personality traits.
    
    Example: 1990 = ปีมะเมีย (ม้า/Horse)
    """
    if birth_year < 1900 or birth_year > 2100:
        raise HTTPException(status_code=400, detail="Birth year must be between 1900 and 2100")
    
    year_animal = get_thai_year_animal(birth_year)
    thai_year = gregorian_to_thai_year(birth_year)
    
    message = f"ปี พ.ศ. {thai_year} (ค.ศ. {birth_year}) คือ{year_animal['name_th']} ปีนักษัตร{year_animal['animal_th']}"
    
    return NaksatResponse(
        birth_year=birth_year,
        thai_year=thai_year,
        year_animal=ThaiYearAnimal(**year_animal),
        message=message
    )


@router.get("/birth-day", response_model=ThaiBirthDay, summary="Get วันเกิด info")
async def get_birth_day_info(
    birth_date: str = Query(
        ..., 
        description="วันเกิด Format: YYYY-MM-DD เช่น 1990-05-15",
        examples=["1990-05-15", "2000-01-01"]
    )
):
    """
    Get Thai birth day information (วันเกิด).
    
    - **birth_date**: วันเกิด Format: **YYYY-MM-DD** เช่น 1990-05-15
    
    Returns the ruling planet, lucky color, and personality traits.
    """
    try:
        birth_day = get_thai_birth_day(birth_date)
        return ThaiBirthDay(**birth_day)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"รูปแบบวันที่ไม่ถูกต้อง กรุณาใส่ YYYY-MM-DD เช่น 1990-05-15")


@router.get("/lagna", response_model=ThaiLagna, summary="Get ลัคนา from birth time")
async def get_lagna(
    birth_time: str = Query(
        ..., 
        description="เวลาเกิด Format: HH:MM (24 ชั่วโมง) เช่น 14:30, 09:00",
        examples=["14:30", "09:00", "23:45"]
    )
):
    """
    Calculate Thai Lagna (ลัคนา) from birth time.
    
    - **birth_time**: เวลาเกิด Format: **HH:MM** (24 ชั่วโมง) เช่น 14:30
    
    Lagna is the rising sign at the time of birth, representing one's outer personality.
    """
    try:
        # Validate time format
        parts = birth_time.split(":")
        if len(parts) != 2:
            raise ValueError("Invalid time format")
        hour = int(parts[0])
        minute = int(parts[1])
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            raise ValueError("Invalid time values")
            
        lagna = calculate_thai_lagna(birth_time)
        return ThaiLagna(**lagna)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"รูปแบบเวลาไม่ถูกต้อง กรุณาใส่ HH:MM เช่น 14:30")


@router.post("/reading", response_model=ThaiReadingResponse, summary="Get full Thai horoscope reading")
async def get_full_thai_reading(request: ThaiReadingRequest):
    """
    Get complete Thai horoscope reading (ดูดวงแบบไทย).
    
    Combines:
    - ปีนักษัตร (Year Animal)
    - วันเกิด (Birth Day)
    - ลัคนา (Lagna - if birth time provided)
    
    Returns a comprehensive Thai horoscope summary.
    """
    try:
        reading = get_thai_reading(request.birth_date, request.birth_time)
        
        return ThaiReadingResponse(
            birth_date=reading["birth_date"],
            birth_time=reading["birth_time"],
            year_animal=ThaiYearAnimal(**reading["year_animal"]),
            birth_day=ThaiBirthDay(**reading["birth_day"]),
            lagna=ThaiLagna(**reading["lagna"]) if reading["lagna"] else None,
            summary_th=reading["summary_th"]
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input. Error: {str(e)}")


@router.get("/animals", summary="Get all 12 ปีนักษัตร")
async def get_all_animals():
    """
    Returns all 12 Thai zodiac year animals (ปีนักษัตร).
    
    Useful for building UI dropdowns or reference.
    """
    return {
        "total": 12,
        "animals": [ThaiYearAnimal(**animal) for animal in THAI_YEAR_ANIMALS]
    }


@router.get("/days", summary="Get all 7 วันเกิด")
async def get_all_days():
    """
    Returns all 7 Thai birth days with their attributes.
    """
    return {
        "total": 7,
        "days": [ThaiBirthDay(**day) for day in THAI_BIRTH_DAYS]
    }
