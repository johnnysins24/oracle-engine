"""
Thai Astrology Engine (โหราศาสตร์ไทย)
Implements Thai zodiac year animals (นักษัตร), birth days, and Lagna calculation
"""

from typing import Dict, List, Optional, Tuple
from datetime import datetime

# ============================================================================
# 12 ปีนักษัตร (Thai Zodiac Year Animals)
# ============================================================================

THAI_YEAR_ANIMALS: List[Dict] = [
    {
        "id": 0,
        "name_th": "ปีชวด",
        "animal_th": "หนู",
        "animal_en": "Rat",
        "element": "Water",
        "element_th": "ธาตุน้ำ",
        "characteristics": ["ฉลาด", "มีไหวพริบ", "ขยัน", "ประหยัด", "รอบคอบ"]
    },
    {
        "id": 1,
        "name_th": "ปีฉลู",
        "animal_th": "วัว",
        "animal_en": "Ox",
        "element": "Earth",
        "element_th": "ธาตุดิน",
        "characteristics": ["อดทน", "ซื่อสัตย์", "มุ่งมั่น", "ขยัน", "มั่นคง"]
    },
    {
        "id": 2,
        "name_th": "ปีขาล",
        "animal_th": "เสือ",
        "animal_en": "Tiger",
        "element": "Wood",
        "element_th": "ธาตุไม้",
        "characteristics": ["กล้าหาญ", "มีเสน่ห์", "เป็นผู้นำ", "มีพลัง", "ห้าวหาญ"]
    },
    {
        "id": 3,
        "name_th": "ปีเถาะ",
        "animal_th": "กระต่าย",
        "animal_en": "Rabbit",
        "element": "Wood",
        "element_th": "ธาตุไม้",
        "characteristics": ["อ่อนโยน", "สุภาพ", "รอบคอบ", "มีศิลปะ", "โชคดี"]
    },
    {
        "id": 4,
        "name_th": "ปีมะโรง",
        "animal_th": "งูใหญ่ (มังกร)",
        "animal_en": "Dragon",
        "element": "Earth",
        "element_th": "ธาตุดิน",
        "characteristics": ["มีอำนาจ", "โชคดี", "มีบารมี", "กล้าหาญ", "ทะเยอทะยาน"]
    },
    {
        "id": 5,
        "name_th": "ปีมะเส็ง",
        "animal_th": "งูเล็ก",
        "animal_en": "Snake",
        "element": "Fire",
        "element_th": "ธาตุไฟ",
        "characteristics": ["ฉลาด", "ลึกลับ", "มีเสน่ห์", "รอบคอบ", "มีไหวพริบ"]
    },
    {
        "id": 6,
        "name_th": "ปีมะเมีย",
        "animal_th": "ม้า",
        "animal_en": "Horse",
        "element": "Fire",
        "element_th": "ธาตุไฟ",
        "characteristics": ["กระตือรือร้น", "อิสระ", "มีพลัง", "ร่าเริง", "รักอิสระ"]
    },
    {
        "id": 7,
        "name_th": "ปีมะแม",
        "animal_th": "แพะ",
        "animal_en": "Goat",
        "element": "Earth",
        "element_th": "ธาตุดิน",
        "characteristics": ["อ่อนโยน", "มีศิลปะ", "ใจดี", "สงบ", "มีความคิดสร้างสรรค์"]
    },
    {
        "id": 8,
        "name_th": "ปีวอก",
        "animal_th": "ลิง",
        "animal_en": "Monkey",
        "element": "Metal",
        "element_th": "ธาตุทอง",
        "characteristics": ["ฉลาด", "ขี้เล่น", "มีไหวพริบ", "ช่างประดิษฐ์", "คล่องแคล่ว"]
    },
    {
        "id": 9,
        "name_th": "ปีระกา",
        "animal_th": "ไก่",
        "animal_en": "Rooster",
        "element": "Metal",
        "element_th": "ธาตุทอง",
        "characteristics": ["ขยัน", "ตรงไปตรงมา", "มั่นใจ", "กล้าแสดงออก", "รักความยุติธรรม"]
    },
    {
        "id": 10,
        "name_th": "ปีจอ",
        "animal_th": "หมา",
        "animal_en": "Dog",
        "element": "Earth",
        "element_th": "ธาตุดิน",
        "characteristics": ["ซื่อสัตย์", "จงรักภักดี", "ยุติธรรม", "เป็นมิตร", "ไว้ใจได้"]
    },
    {
        "id": 11,
        "name_th": "ปีกุน",
        "animal_th": "หมู",
        "animal_en": "Pig",
        "element": "Water",
        "element_th": "ธาตุน้ำ",
        "characteristics": ["ใจดี", "มีน้ำใจ", "อดทน", "สุภาพ", "โชคดีด้านการเงิน"]
    },
]

# ============================================================================
# 7 วันเกิด (Thai Birth Days)
# ============================================================================

THAI_BIRTH_DAYS: List[Dict] = [
    {
        "day_number": 0,
        "name_th": "วันอาทิตย์",
        "name_en": "Sunday",
        "ruling_planet_th": "พระอาทิตย์",
        "ruling_planet_en": "Sun",
        "color": "Red",
        "color_th": "สีแดง",
        "characteristics": ["มีความเป็นผู้นำ", "มีเกียรติ", "มีศักดิ์ศรี", "ทะเยอทะยาน", "มั่นใจในตัวเอง"]
    },
    {
        "day_number": 1,
        "name_th": "วันจันทร์",
        "name_en": "Monday",
        "ruling_planet_th": "พระจันทร์",
        "ruling_planet_en": "Moon",
        "color": "Yellow",
        "color_th": "สีเหลือง",
        "characteristics": ["อ่อนโยน", "มีเสน่ห์", "อารมณ์อ่อนไหว", "รักครอบครัว", "มีจินตนาการ"]
    },
    {
        "day_number": 2,
        "name_th": "วันอังคาร",
        "name_en": "Tuesday",
        "ruling_planet_th": "พระอังคาร",
        "ruling_planet_en": "Mars",
        "color": "Pink",
        "color_th": "สีชมพู",
        "characteristics": ["กล้าหาญ", "มีพลัง", "ตัดสินใจเร็ว", "ชอบการแข่งขัน", "มุ่งมั่น"]
    },
    {
        "day_number": 3,
        "name_th": "วันพุธ",
        "name_en": "Wednesday",
        "ruling_planet_th": "พระพุธ",
        "ruling_planet_en": "Mercury",
        "color": "Green",
        "color_th": "สีเขียว",
        "characteristics": ["ฉลาด", "พูดเก่ง", "มีไหวพริบ", "ปรับตัวเก่ง", "ช่างคิด"]
    },
    {
        "day_number": 4,
        "name_th": "วันพฤหัสบดี",
        "name_en": "Thursday",
        "ruling_planet_th": "พระพฤหัสบดี",
        "ruling_planet_en": "Jupiter",
        "color": "Orange",
        "color_th": "สีส้ม",
        "characteristics": ["มีบุญวาสนา", "โชคดี", "ใจกว้าง", "มีคุณธรรม", "เป็นที่เคารพ"]
    },
    {
        "day_number": 5,
        "name_th": "วันศุกร์",
        "name_en": "Friday",
        "ruling_planet_th": "พระศุกร์",
        "ruling_planet_en": "Venus",
        "color": "Blue",
        "color_th": "สีฟ้า",
        "characteristics": ["รักสวยรักงาม", "มีศิลปะ", "โรแมนติก", "รักความสงบ", "มีเสน่ห์"]
    },
    {
        "day_number": 6,
        "name_th": "วันเสาร์",
        "name_en": "Saturday",
        "ruling_planet_th": "พระเสาร์",
        "ruling_planet_en": "Saturn",
        "color": "Purple",
        "color_th": "สีม่วง",
        "characteristics": ["รอบคอบ", "มีระเบียบ", "อดทน", "จริงจัง", "รับผิดชอบ"]
    },
]

# ============================================================================
# 12 ลัคนาราศี (Thai Lagna / Rising Signs)
# ============================================================================

THAI_LAGNA: List[Dict] = [
    {
        "lagna_id": 0,
        "name_th": "ลัคนาราศีเมษ",
        "rasi_th": "ราศีเมษ",
        "rasi_en": "Aries",
        "meaning": "เป็นผู้นำ กล้าหาญ มีพลังขับเคลื่อน ชอบริเริ่มสิ่งใหม่"
    },
    {
        "lagna_id": 1,
        "name_th": "ลัคนาราศีพฤษภ",
        "rasi_th": "ราศีพฤษภ",
        "rasi_en": "Taurus",
        "meaning": "มั่นคง อดทน รักความสวยงาม มีรสนิยมดี"
    },
    {
        "lagna_id": 2,
        "name_th": "ลัคนาราศีเมถุน",
        "rasi_th": "ราศีเมถุน",
        "rasi_en": "Gemini",
        "meaning": "ฉลาด ช่างพูด ปรับตัวเก่ง สนใจหลายสิ่ง"
    },
    {
        "lagna_id": 3,
        "name_th": "ลัคนาราศีกรกฎ",
        "rasi_th": "ราศีกรกฎ",
        "rasi_en": "Cancer",
        "meaning": "อ่อนโยน รักครอบครัว มีสัญชาตญาณปกป้อง"
    },
    {
        "lagna_id": 4,
        "name_th": "ลัคนาราศีสิงห์",
        "rasi_th": "ราศีสิงห์",
        "rasi_en": "Leo",
        "meaning": "มีเสน่ห์ รักเกียรติ เป็นจุดสนใจ มีความมั่นใจ"
    },
    {
        "lagna_id": 5,
        "name_th": "ลัคนาราศีกันย์",
        "rasi_th": "ราศีกันย์",
        "rasi_en": "Virgo",
        "meaning": "ละเอียดรอบคอบ วิเคราะห์เก่ง ชอบความสมบูรณ์แบบ"
    },
    {
        "lagna_id": 6,
        "name_th": "ลัคนาราศีตุลย์",
        "rasi_th": "ราศีตุลย์",
        "rasi_en": "Libra",
        "meaning": "รักความยุติธรรม มีศิลปะ รักสันติภาพ ประนีประนอม"
    },
    {
        "lagna_id": 7,
        "name_th": "ลัคนาราศีพิจิก",
        "rasi_th": "ราศีพิจิก",
        "rasi_en": "Scorpio",
        "meaning": "ลึกลับ เข้มแข็ง มีพลังภายใน เจาะลึก"
    },
    {
        "lagna_id": 8,
        "name_th": "ลัคนาราศีธนู",
        "rasi_th": "ราศีธนู",
        "rasi_en": "Sagittarius",
        "meaning": "รักอิสระ ชอบผจญภัย มองโลกกว้าง ใฝ่รู้"
    },
    {
        "lagna_id": 9,
        "name_th": "ลัคนาราศีมังกร",
        "rasi_th": "ราศีมังกร",
        "rasi_en": "Capricorn",
        "meaning": "ทะเยอทะยาน มุ่งมั่น รับผิดชอบ ประสบความสำเร็จ"
    },
    {
        "lagna_id": 10,
        "name_th": "ลัคนาราศีกุมภ์",
        "rasi_th": "ราศีกุมภ์",
        "rasi_en": "Aquarius",
        "meaning": "มีความคิดสร้างสรรค์ เป็นตัวของตัวเอง รักเพื่อนมนุษย์"
    },
    {
        "lagna_id": 11,
        "name_th": "ลัคนาราศีมีน",
        "rasi_th": "ราศีมีน",
        "rasi_en": "Pisces",
        "meaning": "มีจินตนาการ อ่อนไหว เข้าใจคนอื่น มีศิลปะ"
    },
]


# ============================================================================
# CALCULATION FUNCTIONS
# ============================================================================

def get_thai_year_animal(birth_year: int) -> Dict:
    """
    Get Thai zodiac year animal (ปีนักษัตร) from birth year.
    
    Thai zodiac cycle:
    - Base year: 1900 = ปีชวด (Rat, id=0)
    - Cycle repeats every 12 years
    
    Args:
        birth_year: Gregorian year (e.g., 1990)
        
    Returns:
        Thai year animal data
    """
    # 1900 = Rat (id=0), so offset accordingly
    # 1900 % 12 = 4, and we want 1900 to be Rat (0)
    # So: (year - 1900) % 12 maps to the animal id
    # But Thai system: 1900 = Rat, 1901 = Ox, etc.
    
    # More accurate: (year - 4) % 12 gives:
    # 1900: (1900-4) % 12 = 0 (Rat) ✓
    # 1990: (1990-4) % 12 = 6 (Horse) ✓
    
    animal_id = (birth_year - 4) % 12
    return THAI_YEAR_ANIMALS[animal_id]


def get_thai_birth_day(birth_date: str) -> Dict:
    """
    Get Thai birth day information from date.
    
    Args:
        birth_date: Date in YYYY-MM-DD format
        
    Returns:
        Thai birth day data
    """
    date = datetime.strptime(birth_date, "%Y-%m-%d")
    # weekday(): Monday=0, Sunday=6
    # We want: Sunday=0, Monday=1, ..., Saturday=6
    day_number = (date.weekday() + 1) % 7
    return THAI_BIRTH_DAYS[day_number]


def calculate_thai_lagna(birth_time: str) -> Dict:
    """
    Calculate Thai Lagna (ลัคนา) from birth time.
    
    Simplified calculation:
    - Each Lagna (Rasi) rules approximately 2 hours
    - Starting from 6:00 AM = Aries rising
    
    Args:
        birth_time: Time in HH:MM format (24-hour)
        
    Returns:
        Thai Lagna data
    """
    time_parts = birth_time.split(":")
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    
    # Convert to decimal hours
    decimal_time = hour + minute / 60.0
    
    # Simplified Lagna calculation:
    # 6:00 AM (6.0) = Aries (0) rising
    # Each sign = 2 hours
    # Adjusted from 6 AM
    
    adjusted_time = decimal_time - 6.0
    if adjusted_time < 0:
        adjusted_time += 24.0
    
    # Each sign spans 2 hours (24 hours / 12 signs)
    lagna_id = int(adjusted_time / 2) % 12
    
    return THAI_LAGNA[lagna_id]


def gregorian_to_thai_year(year: int) -> int:
    """Convert Gregorian year to Thai Buddhist Era (พ.ศ.)"""
    return year + 543


def get_thai_reading(birth_date: str, birth_time: Optional[str] = None) -> Dict:
    """
    Get complete Thai horoscope reading.
    
    Args:
        birth_date: Date in YYYY-MM-DD format
        birth_time: Optional time in HH:MM format
        
    Returns:
        Complete Thai reading data
    """
    date = datetime.strptime(birth_date, "%Y-%m-%d")
    year = date.year
    
    year_animal = get_thai_year_animal(year)
    birth_day = get_thai_birth_day(birth_date)
    lagna = calculate_thai_lagna(birth_time) if birth_time else None
    
    # Generate summary
    summary_parts = [
        f"คุณเกิด{year_animal['name_th']} ({year_animal['animal_th']})",
        f"ตรงกับ{birth_day['name_th']}",
        f"มีดาวประจำวันคือ{birth_day['ruling_planet_th']}",
        f"สีประจำวันคือ{birth_day['color_th']}"
    ]
    
    if lagna:
        summary_parts.append(f"มี{lagna['name_th']}")
    
    summary_th = " ".join(summary_parts)
    
    return {
        "birth_date": birth_date,
        "birth_time": birth_time,
        "year_animal": year_animal,
        "birth_day": birth_day,
        "lagna": lagna,
        "summary_th": summary_th
    }
