"""
Western Astrology Engine
Natal chart calculations using pure Python (no external dependencies)
"""

from typing import List, Dict, Tuple, Optional
from datetime import datetime
import math

# ============================================================================
# ZODIAC SIGNS DATA (12 Signs)
# ============================================================================

ZODIAC_SIGNS: List[Dict] = [
    {
        "id": 0,
        "name_en": "Aries",
        "name_th": "ราศีเมษ",
        "symbol": "♈",
        "element": "Fire",
        "element_th": "ธาตุไฟ",
        "modality": "Cardinal",
        "ruling_planet": "Mars",
        "date_range": "Mar 21 - Apr 19"
    },
    {
        "id": 1,
        "name_en": "Taurus",
        "name_th": "ราศีพฤษภ",
        "symbol": "♉",
        "element": "Earth",
        "element_th": "ธาตุดิน",
        "modality": "Fixed",
        "ruling_planet": "Venus",
        "date_range": "Apr 20 - May 20"
    },
    {
        "id": 2,
        "name_en": "Gemini",
        "name_th": "ราศีเมถุน",
        "symbol": "♊",
        "element": "Air",
        "element_th": "ธาตุลม",
        "modality": "Mutable",
        "ruling_planet": "Mercury",
        "date_range": "May 21 - Jun 20"
    },
    {
        "id": 3,
        "name_en": "Cancer",
        "name_th": "ราศีกรกฎ",
        "symbol": "♋",
        "element": "Water",
        "element_th": "ธาตุน้ำ",
        "modality": "Cardinal",
        "ruling_planet": "Moon",
        "date_range": "Jun 21 - Jul 22"
    },
    {
        "id": 4,
        "name_en": "Leo",
        "name_th": "ราศีสิงห์",
        "symbol": "♌",
        "element": "Fire",
        "element_th": "ธาตุไฟ",
        "modality": "Fixed",
        "ruling_planet": "Sun",
        "date_range": "Jul 23 - Aug 22"
    },
    {
        "id": 5,
        "name_en": "Virgo",
        "name_th": "ราศีกันย์",
        "symbol": "♍",
        "element": "Earth",
        "element_th": "ธาตุดิน",
        "modality": "Mutable",
        "ruling_planet": "Mercury",
        "date_range": "Aug 23 - Sep 22"
    },
    {
        "id": 6,
        "name_en": "Libra",
        "name_th": "ราศีตุลย์",
        "symbol": "♎",
        "element": "Air",
        "element_th": "ธาตุลม",
        "modality": "Cardinal",
        "ruling_planet": "Venus",
        "date_range": "Sep 23 - Oct 22"
    },
    {
        "id": 7,
        "name_en": "Scorpio",
        "name_th": "ราศีพิจิก",
        "symbol": "♏",
        "element": "Water",
        "element_th": "ธาตุน้ำ",
        "modality": "Fixed",
        "ruling_planet": "Pluto/Mars",
        "date_range": "Oct 23 - Nov 21"
    },
    {
        "id": 8,
        "name_en": "Sagittarius",
        "name_th": "ราศีธนู",
        "symbol": "♐",
        "element": "Fire",
        "element_th": "ธาตุไฟ",
        "modality": "Mutable",
        "ruling_planet": "Jupiter",
        "date_range": "Nov 22 - Dec 21"
    },
    {
        "id": 9,
        "name_en": "Capricorn",
        "name_th": "ราศีมังกร",
        "symbol": "♑",
        "element": "Earth",
        "element_th": "ธาตุดิน",
        "modality": "Cardinal",
        "ruling_planet": "Saturn",
        "date_range": "Dec 22 - Jan 19"
    },
    {
        "id": 10,
        "name_en": "Aquarius",
        "name_th": "ราศีกุมภ์",
        "symbol": "♒",
        "element": "Air",
        "element_th": "ธาตุลม",
        "modality": "Fixed",
        "ruling_planet": "Uranus/Saturn",
        "date_range": "Jan 20 - Feb 18"
    },
    {
        "id": 11,
        "name_en": "Pisces",
        "name_th": "ราศีมีน",
        "symbol": "♓",
        "element": "Water",
        "element_th": "ธาตุน้ำ",
        "modality": "Mutable",
        "ruling_planet": "Neptune/Jupiter",
        "date_range": "Feb 19 - Mar 20"
    },
]

# ============================================================================
# PLANET DATA
# ============================================================================

PLANETS: Dict[str, Dict] = {
    "Sun": {"name_en": "Sun", "name_th": "อาทิตย์", "symbol": "☉"},
    "Moon": {"name_en": "Moon", "name_th": "จันทร์", "symbol": "☽"},
    "Mercury": {"name_en": "Mercury", "name_th": "พุธ", "symbol": "☿"},
    "Venus": {"name_en": "Venus", "name_th": "ศุกร์", "symbol": "♀"},
    "Mars": {"name_en": "Mars", "name_th": "อังคาร", "symbol": "♂"},
    "Jupiter": {"name_en": "Jupiter", "name_th": "พฤหัสบดี", "symbol": "♃"},
    "Saturn": {"name_en": "Saturn", "name_th": "เสาร์", "symbol": "♄"},
}


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_sign_by_name(sign_name: str) -> Dict:
    """Get zodiac sign data by English name."""
    for sign in ZODIAC_SIGNS:
        if sign["name_en"].lower() == sign_name.lower():
            return sign
    return ZODIAC_SIGNS[0]


def get_sign_by_id(sign_id: int) -> Dict:
    """Get zodiac sign data by ID (0-11)."""
    return ZODIAC_SIGNS[sign_id % 12]


def get_all_zodiac_signs() -> List[Dict]:
    """Get all 12 zodiac signs."""
    return ZODIAC_SIGNS.copy()


def degree_to_sign(degree: float) -> Tuple[Dict, float]:
    """Convert ecliptic longitude to zodiac sign and degree within sign."""
    degree = degree % 360
    sign_id = int(degree // 30)
    degree_in_sign = degree % 30
    return ZODIAC_SIGNS[sign_id], round(degree_in_sign, 2)


# ============================================================================
# ASTRONOMICAL CALCULATIONS (Simplified)
# ============================================================================

def julian_day(year: int, month: int, day: int, hour: float = 12.0) -> float:
    """Calculate Julian Day number."""
    if month <= 2:
        year -= 1
        month += 12
    
    A = int(year / 100)
    B = 2 - A + int(A / 4)
    
    jd = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + hour/24.0 + B - 1524.5
    return jd


def sun_longitude(jd: float) -> float:
    """Calculate Sun's ecliptic longitude (simplified)."""
    # Days since J2000.0
    T = (jd - 2451545.0) / 36525.0
    
    # Mean longitude of the Sun
    L0 = 280.46646 + 36000.76983 * T + 0.0003032 * T * T
    L0 = L0 % 360
    
    # Mean anomaly of the Sun
    M = 357.52911 + 35999.05029 * T - 0.0001537 * T * T
    M = math.radians(M % 360)
    
    # Equation of center
    C = (1.914602 - 0.004817 * T - 0.000014 * T * T) * math.sin(M)
    C += (0.019993 - 0.000101 * T) * math.sin(2 * M)
    C += 0.000289 * math.sin(3 * M)
    
    # Sun's true longitude
    sun_lon = L0 + C
    return sun_lon % 360


def moon_longitude(jd: float) -> float:
    """Calculate Moon's ecliptic longitude (simplified)."""
    T = (jd - 2451545.0) / 36525.0
    
    # Moon's mean longitude
    L = 218.3164477 + 481267.88123421 * T - 0.0015786 * T * T
    
    # Moon's mean elongation
    D = 297.8501921 + 445267.1114034 * T - 0.0018819 * T * T
    
    # Moon's mean anomaly
    M = 134.9633964 + 477198.8675055 * T + 0.0087414 * T * T
    
    # Simplified correction
    L = L + 6.289 * math.sin(math.radians(M))
    
    return L % 360


def calculate_ascendant(jd: float, latitude: float, longitude: float) -> float:
    """Calculate Ascendant (Rising Sign) - simplified."""
    # Local Sidereal Time
    T = (jd - 2451545.0) / 36525.0
    
    # Greenwich Mean Sidereal Time
    GMST = 280.46061837 + 360.98564736629 * (jd - 2451545.0)
    GMST = GMST + 0.000387933 * T * T - T * T * T / 38710000.0
    
    # Local Sidereal Time
    LST = (GMST + longitude) % 360
    
    # Obliquity of the ecliptic
    epsilon = 23.4393 - 0.0000004 * (jd - 2451545.0)
    
    # Calculate Ascendant
    lat_rad = math.radians(latitude)
    eps_rad = math.radians(epsilon)
    lst_rad = math.radians(LST)
    
    # Ascendant formula
    y = -math.cos(lst_rad)
    x = math.sin(lst_rad) * math.cos(eps_rad) + math.tan(lat_rad) * math.sin(eps_rad)
    
    asc = math.degrees(math.atan2(y, x))
    asc = (asc + 180) % 360
    
    return asc


def approximate_planet_longitude(planet: str, jd: float) -> float:
    """Approximate planet longitude (very simplified for demo)."""
    T = (jd - 2451545.0) / 36525.0
    
    # Simplified mean longitudes (rough approximations)
    if planet == "Mercury":
        L = 252.2509 + 149472.6746 * T
    elif planet == "Venus":
        L = 181.9798 + 58517.8156 * T
    elif planet == "Mars":
        L = 355.4330 + 19140.2993 * T
    elif planet == "Jupiter":
        L = 34.3515 + 3034.9057 * T
    elif planet == "Saturn":
        L = 50.0774 + 1222.1138 * T
    else:
        L = 0
    
    return L % 360


# ============================================================================
# NATAL CHART CALCULATION
# ============================================================================

def calculate_natal_chart(
    birth_date: str,
    birth_time: str,
    latitude: float,
    longitude: float,
    timezone_offset: str = "+00:00"
) -> Dict:
    """
    Calculate a natal chart using pure Python.
    
    Args:
        birth_date: Date in YYYY-MM-DD format
        birth_time: Time in HH:MM format (24-hour)
        latitude: Birth location latitude
        longitude: Birth location longitude
        timezone_offset: UTC offset (e.g., "+07:00")
        
    Returns:
        Dict containing sun_sign, moon_sign, ascendant, planets, houses
    """
    # Parse date and time
    date_parts = birth_date.split("-")
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    
    time_parts = birth_time.split(":")
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    
    # Parse timezone offset
    tz_sign = 1 if timezone_offset.startswith("+") else -1
    tz_parts = timezone_offset[1:].split(":")
    tz_hours = int(tz_parts[0])
    tz_minutes = int(tz_parts[1]) if len(tz_parts) > 1 else 0
    tz_offset = tz_sign * (tz_hours + tz_minutes / 60)
    
    # Convert to UT
    decimal_hour = hour + minute / 60.0 - tz_offset
    
    # Calculate Julian Day
    jd = julian_day(year, month, day, decimal_hour)
    
    # Calculate Sun position
    sun_lon = sun_longitude(jd)
    sun_sign, sun_deg = degree_to_sign(sun_lon)
    
    # Calculate Moon position
    moon_lon = moon_longitude(jd)
    moon_sign, moon_deg = degree_to_sign(moon_lon)
    
    # Calculate Ascendant
    asc_lon = calculate_ascendant(jd, latitude, longitude)
    asc_sign, asc_deg = degree_to_sign(asc_lon)
    
    # Build planet positions
    planets = []
    
    # Sun
    planets.append({
        "planet_en": "Sun",
        "planet_th": "อาทิตย์",
        "sign_en": sun_sign["name_en"],
        "sign_th": sun_sign["name_th"],
        "degree": sun_deg,
        "full_degree": round(sun_lon, 2),
        "house": None,
        "retrograde": False
    })
    
    # Moon
    planets.append({
        "planet_en": "Moon",
        "planet_th": "จันทร์",
        "sign_en": moon_sign["name_en"],
        "sign_th": moon_sign["name_th"],
        "degree": moon_deg,
        "full_degree": round(moon_lon, 2),
        "house": None,
        "retrograde": False
    })
    
    # Other planets
    for planet_name in ["Mercury", "Venus", "Mars", "Jupiter", "Saturn"]:
        planet_lon = approximate_planet_longitude(planet_name, jd)
        planet_sign, planet_deg = degree_to_sign(planet_lon)
        planet_data = PLANETS[planet_name]
        
        planets.append({
            "planet_en": planet_data["name_en"],
            "planet_th": planet_data["name_th"],
            "sign_en": planet_sign["name_en"],
            "sign_th": planet_sign["name_th"],
            "degree": planet_deg,
            "full_degree": round(planet_lon, 2),
            "house": None,
            "retrograde": False
        })
    
    # Build house data (simplified - equal house system from Ascendant)
    houses = []
    for i in range(12):
        house_lon = (asc_lon + i * 30) % 360
        house_sign, house_deg = degree_to_sign(house_lon)
        houses.append({
            "house_number": i + 1,
            "sign_en": house_sign["name_en"],
            "sign_th": house_sign["name_th"],
            "degree": house_deg
        })
    
    return {
        "sun_sign": sun_sign,
        "moon_sign": moon_sign,
        "ascendant": asc_sign,
        "planets": planets,
        "houses": houses
    }


def get_sun_sign_from_date(birth_date: str) -> Dict:
    """
    Get sun sign from birth date only.
    
    Args:
        birth_date: Date in YYYY-MM-DD format
        
    Returns:
        Zodiac sign data
    """
    date = datetime.strptime(birth_date, "%Y-%m-%d")
    month = date.month
    day = date.day
    
    # Zodiac date ranges
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return ZODIAC_SIGNS[0]  # Aries
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return ZODIAC_SIGNS[1]  # Taurus
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return ZODIAC_SIGNS[2]  # Gemini
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return ZODIAC_SIGNS[3]  # Cancer
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return ZODIAC_SIGNS[4]  # Leo
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return ZODIAC_SIGNS[5]  # Virgo
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return ZODIAC_SIGNS[6]  # Libra
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return ZODIAC_SIGNS[7]  # Scorpio
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return ZODIAC_SIGNS[8]  # Sagittarius
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return ZODIAC_SIGNS[9]  # Capricorn
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return ZODIAC_SIGNS[10]  # Aquarius
    else:
        return ZODIAC_SIGNS[11]  # Pisces
