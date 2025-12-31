"""
AI Prompt Templates
Personas and prompt builders for fortune interpretation
"""

from typing import List, Optional, Dict

# ============================================================================
# PERSONA PROMPTS
# ============================================================================

TAROT_GYPSY_PROMPT = """คุณเป็นผู้เชี่ยวชาญด้านไพ่ทาโรต์ที่มีประสบการณ์สูง

หลักการตอบ:
- ใช้ภาษาไทยที่เข้าใจง่าย ตรงประเด็น
- ไม่ใช้คำเรียกแทนตัวเอง ไม่ใช้ emoji
- อธิบายความหมายของไพ่แต่ละใบอย่างกระชับ
- เชื่อมโยงความหมายของไพ่เข้ากับคำถาม
- สรุปคำทำนายให้ชัดเจน พร้อมคำแนะนำที่นำไปใช้ได้จริง
- ความยาวพอเหมาะ ไม่เยิ่นเย้อ"""

THAI_FORTUNE_PROMPT = """คุณเป็นผู้เชี่ยวชาญด้านโหราศาสตร์ไทย

หลักการตอบ:
- ใช้ภาษาไทยที่สุภาพ เข้าใจง่าย ตรงประเด็น
- ไม่ใช้คำเรียกแทนตัวเอง ไม่ใช้ emoji
- วิเคราะห์ดวงตามปีนักษัตร วันเกิด และลัคนา
- ทำนายครอบคลุม: การงาน การเงิน ความรัก สุขภาพ
- ให้คำแนะนำที่ปฏิบัติได้จริง
- กระชับ ไม่ยาวเกินไป"""

WESTERN_ASTROLOGER_PROMPT = """You are an experienced Western astrologer.

Guidelines:
- Use clear, accessible language
- Do not use self-referential terms or emojis
- Analyze Sun, Moon, and Ascendant signs concisely
- Focus on personality insights and practical advice
- Keep responses focused and not overly long"""


# ============================================================================
# PROMPT BUILDERS
# ============================================================================

def build_tarot_prompt(
    cards: List[Dict],
    question: Optional[str] = None,
    spread_type: str = "single",
    lang: str = "th"
) -> str:
    """Build prompt for tarot interpretation."""
    
    # Build card descriptions
    card_text = ""
    for i, card in enumerate(cards):
        name = card.get("name_th") or card.get("name_en", "Unknown")
        keywords = ", ".join(card.get("keywords", [])[:3])
        position = ""
        
        if spread_type == "three" and i < 3:
            positions = ["อดีต", "ปัจจุบัน", "อนาคต"] if lang == "th" else ["Past", "Present", "Future"]
            position = f"[{positions[i]}] "
        
        card_text += f"- {position}ไพ่ {name}: {keywords}\n"
    
    # Build prompt
    if lang == "th":
        prompt = f"""กรุณาทำนายไพ่ทาโรต์ให้กับเจ้าของดวง

ไพ่ที่จั่วได้:
{card_text}

รูปแบบการดู: {spread_type}
"""
        if question:
            prompt += f"\nคำถามของเจ้าของดวง: {question}"
    else:
        prompt = f"""Please interpret these tarot cards:

Cards drawn:
{card_text}

Spread type: {spread_type}
"""
        if question:
            prompt += f"\nQuerent's question: {question}"
    
    return prompt


def build_thai_prompt(
    birth_data: Dict,
    question: Optional[str] = None
) -> str:
    """Build prompt for Thai fortune reading."""
    
    year_animal = birth_data.get("year_animal", {})
    birth_day = birth_data.get("birth_day", {})
    lagna = birth_data.get("lagna", {})
    
    prompt = f"""กรุณาทำนายดวงชะตาให้กับเจ้าของดวง

ข้อมูลดวงชะตา:
- ปีนักษัตร: {year_animal.get('name_th', 'ไม่ทราบ')} ({year_animal.get('animal_th', '')})
- ธาตุประจำตัว: {year_animal.get('element_th', '')}
- วันเกิด: {birth_day.get('name_th', 'ไม่ทราบ')}
- ดาวประจำวัน: {birth_day.get('ruling_planet_th', '')}
- สีประจำวัน: {birth_day.get('color_th', '')}
"""
    
    if lagna:
        prompt += f"- ลัคนา: {lagna.get('name_th', '')}\n"
        prompt += f"- ความหมายลัคนา: {lagna.get('meaning', '')}\n"
    
    if question:
        prompt += f"\nคำถามของเจ้าของดวง: {question}"
    else:
        prompt += "\nกรุณาทำนายในภาพรวม: การงาน การเงิน ความรัก สุขภาพ"
    
    return prompt


def build_natal_prompt(
    natal_data: Dict,
    question: Optional[str] = None,
    lang: str = "en"
) -> str:
    """Build prompt for natal chart interpretation."""
    
    sun = natal_data.get("sun_sign", {})
    moon = natal_data.get("moon_sign", {})
    asc = natal_data.get("ascendant", {})
    
    if lang == "th":
        prompt = f"""กรุณาวิเคราะห์ดวงชะตาตามหลักโหราศาสตร์สากล

ข้อมูลดวงชะตา:
- ดวงอาทิตย์อยู่ราศี: {sun.get('name_th', '')} ({sun.get('element_th', '')})
- ดวงจันทร์อยู่ราศี: {moon.get('name_th', '')} ({moon.get('element_th', '')})
- ลัคนา (Ascendant): {asc.get('name_th', '')} ({asc.get('element_th', '')})
"""
    else:
        prompt = f"""Please analyze this natal chart:

Chart data:
- Sun in {sun.get('name_en', 'Unknown')} ({sun.get('element', '')})
- Moon in {moon.get('name_en', 'Unknown')} ({moon.get('element', '')})
- Ascendant in {asc.get('name_en', 'Unknown')} ({asc.get('element', '')})
"""
    
    if question:
        prompt += f"\nQuestion: {question}"
    
    return prompt
