"""
Tarot Engine - Complete 78 Card Rider-Waite Deck
Contains all Major and Minor Arcana cards with Thai translations and keywords
"""

import random
from typing import List, Dict, Tuple

# ============================================================================
# MAJOR ARCANA (0-21) - 22 Cards
# ============================================================================

MAJOR_ARCANA: List[Dict] = [
    {
        "id": 0,
        "name_en": "The Fool",
        "name_th": "เดอะฟูล (คนโง่)",
        "arcana": "major",
        "suit": None,
        "keywords": ["new beginnings", "innocence", "adventure", "free spirit", "spontaneity"],
        "image_url": "/assets/tarot/major/00-fool.jpg"
    },
    {
        "id": 1,
        "name_en": "The Magician",
        "name_th": "เดอะแมจิเชี่ยน (นักมายากล)",
        "arcana": "major",
        "suit": None,
        "keywords": ["manifestation", "resourcefulness", "power", "inspired action", "skill"],
        "image_url": "/assets/tarot/major/01-magician.jpg"
    },
    {
        "id": 2,
        "name_en": "The High Priestess",
        "name_th": "เดอะไฮพรีสเตส (นักบวชหญิงชั้นสูง)",
        "arcana": "major",
        "suit": None,
        "keywords": ["intuition", "sacred knowledge", "divine feminine", "subconscious mind", "mystery"],
        "image_url": "/assets/tarot/major/02-high-priestess.jpg"
    },
    {
        "id": 3,
        "name_en": "The Empress",
        "name_th": "เดอะเอมเพรส (จักรพรรดินี)",
        "arcana": "major",
        "suit": None,
        "keywords": ["femininity", "beauty", "nature", "nurturing", "abundance", "fertility"],
        "image_url": "/assets/tarot/major/03-empress.jpg"
    },
    {
        "id": 4,
        "name_en": "The Emperor",
        "name_th": "เดอะเอมเพอเรอร์ (จักรพรรดิ)",
        "arcana": "major",
        "suit": None,
        "keywords": ["authority", "structure", "control", "fatherhood", "leadership", "stability"],
        "image_url": "/assets/tarot/major/04-emperor.jpg"
    },
    {
        "id": 5,
        "name_en": "The Hierophant",
        "name_th": "เดอะไฮโรแฟนท์ (พระสันตะปาปา)",
        "arcana": "major",
        "suit": None,
        "keywords": ["spiritual wisdom", "tradition", "conformity", "morality", "ethics"],
        "image_url": "/assets/tarot/major/05-hierophant.jpg"
    },
    {
        "id": 6,
        "name_en": "The Lovers",
        "name_th": "เดอะเลิฟเวอร์ส (คู่รัก)",
        "arcana": "major",
        "suit": None,
        "keywords": ["love", "harmony", "relationships", "values alignment", "choices"],
        "image_url": "/assets/tarot/major/06-lovers.jpg"
    },
    {
        "id": 7,
        "name_en": "The Chariot",
        "name_th": "เดอะแชริออท (รถศึก)",
        "arcana": "major",
        "suit": None,
        "keywords": ["control", "willpower", "success", "determination", "victory"],
        "image_url": "/assets/tarot/major/07-chariot.jpg"
    },
    {
        "id": 8,
        "name_en": "Strength",
        "name_th": "สเตร็งท์ (พลัง)",
        "arcana": "major",
        "suit": None,
        "keywords": ["courage", "persuasion", "influence", "compassion", "inner strength"],
        "image_url": "/assets/tarot/major/08-strength.jpg"
    },
    {
        "id": 9,
        "name_en": "The Hermit",
        "name_th": "เดอะเฮอร์มิท (ฤๅษี)",
        "arcana": "major",
        "suit": None,
        "keywords": ["soul-searching", "introspection", "solitude", "inner guidance", "wisdom"],
        "image_url": "/assets/tarot/major/09-hermit.jpg"
    },
    {
        "id": 10,
        "name_en": "Wheel of Fortune",
        "name_th": "วีลออฟฟอร์จูน (กงล้อแห่งโชคชะตา)",
        "arcana": "major",
        "suit": None,
        "keywords": ["good luck", "karma", "life cycles", "destiny", "turning point"],
        "image_url": "/assets/tarot/major/10-wheel-of-fortune.jpg"
    },
    {
        "id": 11,
        "name_en": "Justice",
        "name_th": "จัสทิส (ความยุติธรรม)",
        "arcana": "major",
        "suit": None,
        "keywords": ["justice", "fairness", "truth", "cause and effect", "law"],
        "image_url": "/assets/tarot/major/11-justice.jpg"
    },
    {
        "id": 12,
        "name_en": "The Hanged Man",
        "name_th": "เดอะแฮงค์แมน (ชายถูกแขวน)",
        "arcana": "major",
        "suit": None,
        "keywords": ["pause", "surrender", "letting go", "new perspectives", "sacrifice"],
        "image_url": "/assets/tarot/major/12-hanged-man.jpg"
    },
    {
        "id": 13,
        "name_en": "Death",
        "name_th": "เดธ (ความตาย)",
        "arcana": "major",
        "suit": None,
        "keywords": ["endings", "change", "transformation", "transition", "rebirth"],
        "image_url": "/assets/tarot/major/13-death.jpg"
    },
    {
        "id": 14,
        "name_en": "Temperance",
        "name_th": "เทมเพอแรนซ์ (การประสาน)",
        "arcana": "major",
        "suit": None,
        "keywords": ["balance", "moderation", "patience", "purpose", "meaning"],
        "image_url": "/assets/tarot/major/14-temperance.jpg"
    },
    {
        "id": 15,
        "name_en": "The Devil",
        "name_th": "เดอะเดวิล (ปีศาจ)",
        "arcana": "major",
        "suit": None,
        "keywords": ["shadow self", "attachment", "addiction", "restriction", "materialism"],
        "image_url": "/assets/tarot/major/15-devil.jpg"
    },
    {
        "id": 16,
        "name_en": "The Tower",
        "name_th": "เดอะทาวเวอร์ (หอคอย)",
        "arcana": "major",
        "suit": None,
        "keywords": ["sudden change", "upheaval", "chaos", "revelation", "awakening"],
        "image_url": "/assets/tarot/major/16-tower.jpg"
    },
    {
        "id": 17,
        "name_en": "The Star",
        "name_th": "เดอะสตาร์ (ดวงดาว)",
        "arcana": "major",
        "suit": None,
        "keywords": ["hope", "faith", "purpose", "renewal", "spirituality", "inspiration"],
        "image_url": "/assets/tarot/major/17-star.jpg"
    },
    {
        "id": 18,
        "name_en": "The Moon",
        "name_th": "เดอะมูน (ดวงจันทร์)",
        "arcana": "major",
        "suit": None,
        "keywords": ["illusion", "fear", "anxiety", "subconscious", "intuition"],
        "image_url": "/assets/tarot/major/18-moon.jpg"
    },
    {
        "id": 19,
        "name_en": "The Sun",
        "name_th": "เดอะซัน (ดวงอาทิตย์)",
        "arcana": "major",
        "suit": None,
        "keywords": ["positivity", "fun", "warmth", "success", "vitality", "joy"],
        "image_url": "/assets/tarot/major/19-sun.jpg"
    },
    {
        "id": 20,
        "name_en": "Judgement",
        "name_th": "จัดจ์เมนท์ (การพิพากษา)",
        "arcana": "major",
        "suit": None,
        "keywords": ["judgement", "rebirth", "inner calling", "absolution", "reflection"],
        "image_url": "/assets/tarot/major/20-judgement.jpg"
    },
    {
        "id": 21,
        "name_en": "The World",
        "name_th": "เดอะเวิลด์ (โลก)",
        "arcana": "major",
        "suit": None,
        "keywords": ["completion", "integration", "accomplishment", "travel", "fulfillment"],
        "image_url": "/assets/tarot/major/21-world.jpg"
    },
]

# ============================================================================
# MINOR ARCANA - WANDS (22-35) - 14 Cards
# ============================================================================

WANDS: List[Dict] = [
    {
        "id": 22,
        "name_en": "Ace of Wands",
        "name_th": "เอซแห่งไม้เท้า",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["inspiration", "new opportunities", "growth", "potential", "creativity"],
        "image_url": "/assets/tarot/wands/ace.jpg"
    },
    {
        "id": 23,
        "name_en": "Two of Wands",
        "name_th": "ไม้เท้าสอง",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["future planning", "progress", "decisions", "discovery", "personal power"],
        "image_url": "/assets/tarot/wands/02.jpg"
    },
    {
        "id": 24,
        "name_en": "Three of Wands",
        "name_th": "ไม้เท้าสาม",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["expansion", "foresight", "overseas opportunities", "long-term success"],
        "image_url": "/assets/tarot/wands/03.jpg"
    },
    {
        "id": 25,
        "name_en": "Four of Wands",
        "name_th": "ไม้เท้าสี่",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["celebration", "joy", "harmony", "relaxation", "homecoming"],
        "image_url": "/assets/tarot/wands/04.jpg"
    },
    {
        "id": 26,
        "name_en": "Five of Wands",
        "name_th": "ไม้เท้าห้า",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["conflict", "disagreements", "competition", "tension", "diversity"],
        "image_url": "/assets/tarot/wands/05.jpg"
    },
    {
        "id": 27,
        "name_en": "Six of Wands",
        "name_th": "ไม้เท้าหก",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["success", "public recognition", "progress", "self-confidence", "victory"],
        "image_url": "/assets/tarot/wands/06.jpg"
    },
    {
        "id": 28,
        "name_en": "Seven of Wands",
        "name_th": "ไม้เท้าเจ็ด",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["challenge", "competition", "protection", "perseverance", "defense"],
        "image_url": "/assets/tarot/wands/07.jpg"
    },
    {
        "id": 29,
        "name_en": "Eight of Wands",
        "name_th": "ไม้เท้าแปด",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["movement", "fast paced change", "action", "alignment", "air travel"],
        "image_url": "/assets/tarot/wands/08.jpg"
    },
    {
        "id": 30,
        "name_en": "Nine of Wands",
        "name_th": "ไม้เท้าเก้า",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["resilience", "courage", "persistence", "test of faith", "boundaries"],
        "image_url": "/assets/tarot/wands/09.jpg"
    },
    {
        "id": 31,
        "name_en": "Ten of Wands",
        "name_th": "ไม้เท้าสิบ",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["burden", "extra responsibility", "hard work", "completion", "overload"],
        "image_url": "/assets/tarot/wands/10.jpg"
    },
    {
        "id": 32,
        "name_en": "Page of Wands",
        "name_th": "เพจแห่งไม้เท้า",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["exploration", "excitement", "freedom", "discovery", "enthusiasm"],
        "image_url": "/assets/tarot/wands/page.jpg"
    },
    {
        "id": 33,
        "name_en": "Knight of Wands",
        "name_th": "อัศวินแห่งไม้เท้า",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["energy", "passion", "adventure", "impulsiveness", "action"],
        "image_url": "/assets/tarot/wands/knight.jpg"
    },
    {
        "id": 34,
        "name_en": "Queen of Wands",
        "name_th": "ราชินีแห่งไม้เท้า",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["courage", "confidence", "independence", "social butterfly", "determination"],
        "image_url": "/assets/tarot/wands/queen.jpg"
    },
    {
        "id": 35,
        "name_en": "King of Wands",
        "name_th": "ราชาแห่งไม้เท้า",
        "arcana": "minor",
        "suit": "wands",
        "keywords": ["natural leader", "vision", "entrepreneur", "honor", "charisma"],
        "image_url": "/assets/tarot/wands/king.jpg"
    },
]

# ============================================================================
# MINOR ARCANA - CUPS (36-49) - 14 Cards
# ============================================================================

CUPS: List[Dict] = [
    {
        "id": 36,
        "name_en": "Ace of Cups",
        "name_th": "เอซแห่งถ้วย",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["love", "new relationships", "compassion", "creativity", "emotional fulfillment"],
        "image_url": "/assets/tarot/cups/ace.jpg"
    },
    {
        "id": 37,
        "name_en": "Two of Cups",
        "name_th": "ถ้วยสอง",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["unified love", "partnership", "mutual attraction", "connection", "harmony"],
        "image_url": "/assets/tarot/cups/02.jpg"
    },
    {
        "id": 38,
        "name_en": "Three of Cups",
        "name_th": "ถ้วยสาม",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["celebration", "friendship", "creativity", "collaborations", "community"],
        "image_url": "/assets/tarot/cups/03.jpg"
    },
    {
        "id": 39,
        "name_en": "Four of Cups",
        "name_th": "ถ้วยสี่",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["meditation", "contemplation", "apathy", "reevaluation", "discontent"],
        "image_url": "/assets/tarot/cups/04.jpg"
    },
    {
        "id": 40,
        "name_en": "Five of Cups",
        "name_th": "ถ้วยห้า",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["regret", "failure", "disappointment", "pessimism", "grief"],
        "image_url": "/assets/tarot/cups/05.jpg"
    },
    {
        "id": 41,
        "name_en": "Six of Cups",
        "name_th": "ถ้วยหก",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["revisiting the past", "childhood memories", "innocence", "joy", "nostalgia"],
        "image_url": "/assets/tarot/cups/06.jpg"
    },
    {
        "id": 42,
        "name_en": "Seven of Cups",
        "name_th": "ถ้วยเจ็ด",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["opportunities", "choices", "wishful thinking", "illusion", "fantasy"],
        "image_url": "/assets/tarot/cups/07.jpg"
    },
    {
        "id": 43,
        "name_en": "Eight of Cups",
        "name_th": "ถ้วยแปด",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["disappointment", "abandonment", "withdrawal", "escapism", "searching"],
        "image_url": "/assets/tarot/cups/08.jpg"
    },
    {
        "id": 44,
        "name_en": "Nine of Cups",
        "name_th": "ถ้วยเก้า",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["contentment", "satisfaction", "gratitude", "wish come true", "luxury"],
        "image_url": "/assets/tarot/cups/09.jpg"
    },
    {
        "id": 45,
        "name_en": "Ten of Cups",
        "name_th": "ถ้วยสิบ",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["divine love", "blissful relationships", "harmony", "alignment", "family"],
        "image_url": "/assets/tarot/cups/10.jpg"
    },
    {
        "id": 46,
        "name_en": "Page of Cups",
        "name_th": "เพจแห่งถ้วย",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["creative opportunities", "intuitive messages", "curiosity", "dreamer"],
        "image_url": "/assets/tarot/cups/page.jpg"
    },
    {
        "id": 47,
        "name_en": "Knight of Cups",
        "name_th": "อัศวินแห่งถ้วย",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["creativity", "romance", "charm", "imagination", "beauty"],
        "image_url": "/assets/tarot/cups/knight.jpg"
    },
    {
        "id": 48,
        "name_en": "Queen of Cups",
        "name_th": "ราชินีแห่งถ้วย",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["compassionate", "caring", "emotionally stable", "intuitive", "in flow"],
        "image_url": "/assets/tarot/cups/queen.jpg"
    },
    {
        "id": 49,
        "name_en": "King of Cups",
        "name_th": "ราชาแห่งถ้วย",
        "arcana": "minor",
        "suit": "cups",
        "keywords": ["emotionally balanced", "compassionate", "diplomatic", "wise", "advisor"],
        "image_url": "/assets/tarot/cups/king.jpg"
    },
]

# ============================================================================
# MINOR ARCANA - SWORDS (50-63) - 14 Cards
# ============================================================================

SWORDS: List[Dict] = [
    {
        "id": 50,
        "name_en": "Ace of Swords",
        "name_th": "เอซแห่งดาบ",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["breakthrough", "clarity", "sharp mind", "truth", "new ideas"],
        "image_url": "/assets/tarot/swords/ace.jpg"
    },
    {
        "id": 51,
        "name_en": "Two of Swords",
        "name_th": "ดาบสอง",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["difficult decisions", "weighing options", "stalemate", "blocked emotions"],
        "image_url": "/assets/tarot/swords/02.jpg"
    },
    {
        "id": 52,
        "name_en": "Three of Swords",
        "name_th": "ดาบสาม",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["heartbreak", "emotional pain", "sorrow", "grief", "hurt"],
        "image_url": "/assets/tarot/swords/03.jpg"
    },
    {
        "id": 53,
        "name_en": "Four of Swords",
        "name_th": "ดาบสี่",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["rest", "relaxation", "meditation", "contemplation", "recuperation"],
        "image_url": "/assets/tarot/swords/04.jpg"
    },
    {
        "id": 54,
        "name_en": "Five of Swords",
        "name_th": "ดาบห้า",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["conflict", "disagreements", "competition", "defeat", "winning at all costs"],
        "image_url": "/assets/tarot/swords/05.jpg"
    },
    {
        "id": 55,
        "name_en": "Six of Swords",
        "name_th": "ดาบหก",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["transition", "change", "rite of passage", "releasing baggage", "journey"],
        "image_url": "/assets/tarot/swords/06.jpg"
    },
    {
        "id": 56,
        "name_en": "Seven of Swords",
        "name_th": "ดาบเจ็ด",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["betrayal", "deception", "getting away with something", "stealth", "strategy"],
        "image_url": "/assets/tarot/swords/07.jpg"
    },
    {
        "id": 57,
        "name_en": "Eight of Swords",
        "name_th": "ดาบแปด",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["negative thoughts", "self-imposed restriction", "imprisonment", "victim mentality"],
        "image_url": "/assets/tarot/swords/08.jpg"
    },
    {
        "id": 58,
        "name_en": "Nine of Swords",
        "name_th": "ดาบเก้า",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["anxiety", "worry", "fear", "depression", "nightmares"],
        "image_url": "/assets/tarot/swords/09.jpg"
    },
    {
        "id": 59,
        "name_en": "Ten of Swords",
        "name_th": "ดาบสิบ",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["painful endings", "deep wounds", "betrayal", "loss", "rock bottom"],
        "image_url": "/assets/tarot/swords/10.jpg"
    },
    {
        "id": 60,
        "name_en": "Page of Swords",
        "name_th": "เพจแห่งดาบ",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["curiosity", "restlessness", "mental energy", "new ideas", "thirst for knowledge"],
        "image_url": "/assets/tarot/swords/page.jpg"
    },
    {
        "id": 61,
        "name_en": "Knight of Swords",
        "name_th": "อัศวินแห่งดาบ",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["ambitious", "action-oriented", "driven", "fast thinking", "impatient"],
        "image_url": "/assets/tarot/swords/knight.jpg"
    },
    {
        "id": 62,
        "name_en": "Queen of Swords",
        "name_th": "ราชินีแห่งดาบ",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["independent", "unbiased judgment", "clear boundaries", "direct communication"],
        "image_url": "/assets/tarot/swords/queen.jpg"
    },
    {
        "id": 63,
        "name_en": "King of Swords",
        "name_th": "ราชาแห่งดาบ",
        "arcana": "minor",
        "suit": "swords",
        "keywords": ["mental clarity", "intellectual power", "authority", "truth", "logic"],
        "image_url": "/assets/tarot/swords/king.jpg"
    },
]

# ============================================================================
# MINOR ARCANA - PENTACLES (64-77) - 14 Cards
# ============================================================================

PENTACLES: List[Dict] = [
    {
        "id": 64,
        "name_en": "Ace of Pentacles",
        "name_th": "เอซแห่งเหรียญ",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["new financial opportunity", "manifestation", "abundance", "prosperity"],
        "image_url": "/assets/tarot/pentacles/ace.jpg"
    },
    {
        "id": 65,
        "name_en": "Two of Pentacles",
        "name_th": "เหรียญสอง",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["balance", "adaptability", "time management", "prioritization", "flexibility"],
        "image_url": "/assets/tarot/pentacles/02.jpg"
    },
    {
        "id": 66,
        "name_en": "Three of Pentacles",
        "name_th": "เหรียญสาม",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["teamwork", "collaboration", "learning", "implementation", "craftsmanship"],
        "image_url": "/assets/tarot/pentacles/03.jpg"
    },
    {
        "id": 67,
        "name_en": "Four of Pentacles",
        "name_th": "เหรียญสี่",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["saving money", "security", "conservatism", "scarcity", "control"],
        "image_url": "/assets/tarot/pentacles/04.jpg"
    },
    {
        "id": 68,
        "name_en": "Five of Pentacles",
        "name_th": "เหรียญห้า",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["financial loss", "poverty", "lack mindset", "isolation", "worry"],
        "image_url": "/assets/tarot/pentacles/05.jpg"
    },
    {
        "id": 69,
        "name_en": "Six of Pentacles",
        "name_th": "เหรียญหก",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["giving", "receiving", "sharing wealth", "generosity", "charity"],
        "image_url": "/assets/tarot/pentacles/06.jpg"
    },
    {
        "id": 70,
        "name_en": "Seven of Pentacles",
        "name_th": "เหรียญเจ็ด",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["long-term view", "sustainable results", "perseverance", "investment", "patience"],
        "image_url": "/assets/tarot/pentacles/07.jpg"
    },
    {
        "id": 71,
        "name_en": "Eight of Pentacles",
        "name_th": "เหรียญแปด",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["apprenticeship", "repetitive tasks", "mastery", "skill development", "diligence"],
        "image_url": "/assets/tarot/pentacles/08.jpg"
    },
    {
        "id": 72,
        "name_en": "Nine of Pentacles",
        "name_th": "เหรียญเก้า",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["abundance", "luxury", "self-sufficiency", "financial independence", "discipline"],
        "image_url": "/assets/tarot/pentacles/09.jpg"
    },
    {
        "id": 73,
        "name_en": "Ten of Pentacles",
        "name_th": "เหรียญสิบ",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["wealth", "financial security", "family", "long-term success", "inheritance"],
        "image_url": "/assets/tarot/pentacles/10.jpg"
    },
    {
        "id": 74,
        "name_en": "Page of Pentacles",
        "name_th": "เพจแห่งเหรียญ",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["manifestation", "financial opportunity", "skill development", "study"],
        "image_url": "/assets/tarot/pentacles/page.jpg"
    },
    {
        "id": 75,
        "name_en": "Knight of Pentacles",
        "name_th": "อัศวินแห่งเหรียญ",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["hard work", "productivity", "routine", "conservatism", "reliability"],
        "image_url": "/assets/tarot/pentacles/knight.jpg"
    },
    {
        "id": 76,
        "name_en": "Queen of Pentacles",
        "name_th": "ราชินีแห่งเหรียญ",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["nurturing", "practical", "providing financially", "working parent", "grounded"],
        "image_url": "/assets/tarot/pentacles/queen.jpg"
    },
    {
        "id": 77,
        "name_en": "King of Pentacles",
        "name_th": "ราชาแห่งเหรียญ",
        "arcana": "minor",
        "suit": "pentacles",
        "keywords": ["wealth", "business", "leadership", "security", "discipline", "abundance"],
        "image_url": "/assets/tarot/pentacles/king.jpg"
    },
]

# ============================================================================
# COMPLETE DECK - All 78 Cards
# ============================================================================

FULL_DECK: List[Dict] = MAJOR_ARCANA + WANDS + CUPS + SWORDS + PENTACLES


# ============================================================================
# SPREAD POSITIONS
# ============================================================================

SPREAD_POSITIONS = {
    "single": ["Guidance"],
    "past_present_future": ["Past", "Present", "Future"],
    "celtic_cross": [
        "Present Situation",
        "Challenge/Obstacle",
        "Past Foundation",
        "Recent Past",
        "Best Outcome",
        "Near Future",
        "Your Approach",
        "External Influences",
        "Hopes and Fears",
        "Final Outcome"
    ]
}


# ============================================================================
# DRAWING FUNCTIONS
# ============================================================================

def draw_cards(count: int = 1) -> Tuple[List[Dict], str, List[str]]:
    """
    Draw random tarot cards from the deck.
    
    Args:
        count: Number of cards to draw (1, 3, or 10)
        
    Returns:
        Tuple of (cards, spread_type, positions)
    """
    # Determine spread type based on count
    if count == 1:
        spread_type = "single"
    elif count == 3:
        spread_type = "past_present_future"
    elif count == 10:
        spread_type = "celtic_cross"
    else:
        # Default to custom spread
        spread_type = f"custom_{count}_card"
    
    # Get positions for this spread
    positions = SPREAD_POSITIONS.get(spread_type, [f"Card {i+1}" for i in range(count)])
    
    # Draw unique cards
    drawn_cards = random.sample(FULL_DECK, min(count, len(FULL_DECK)))
    
    return drawn_cards, spread_type, positions


def draw_single() -> Tuple[Dict, str, List[str]]:
    """Draw a single card for quick guidance."""
    cards, spread_type, positions = draw_cards(1)
    return cards[0], spread_type, positions


def draw_three() -> Tuple[List[Dict], str, List[str]]:
    """Draw three cards for Past/Present/Future spread."""
    return draw_cards(3)


def draw_celtic_cross() -> Tuple[List[Dict], str, List[str]]:
    """Draw ten cards for Celtic Cross spread."""
    return draw_cards(10)


def get_card_by_id(card_id: int) -> Dict | None:
    """Get a specific card by its ID."""
    for card in FULL_DECK:
        if card["id"] == card_id:
            return card
    return None


def get_cards_by_suit(suit: str) -> List[Dict]:
    """Get all cards of a specific suit."""
    return [card for card in FULL_DECK if card.get("suit") == suit]


def get_major_arcana() -> List[Dict]:
    """Get all Major Arcana cards."""
    return MAJOR_ARCANA.copy()


def get_minor_arcana() -> List[Dict]:
    """Get all Minor Arcana cards."""
    return WANDS + CUPS + SWORDS + PENTACLES
