"""
Input Validation and Prompt Injection Protection
Sanitizes user input and validates against allowed topics
"""

import re
from typing import Optional, Tuple

# ============================================================================
# ALLOWED TOPICS - Only these topics are accepted
# ============================================================================

ALLOWED_TOPICS_TH = [
    "ความรัก", "การงาน", "การเงิน", "สุขภาพ", "การเรียน", "ครอบครัว",
    "เนื้อคู่", "คู่ครอง", "ธุรกิจ", "โชคลาภ", "การเดินทาง", "ทั่วไป",
    "อนาคต", "ปีนี้", "เดือนนี้", "สัปดาห์นี้", "วันนี้"
]

ALLOWED_TOPICS_EN = [
    "love", "work", "career", "money", "finance", "health", "study", "family",
    "relationship", "business", "luck", "travel", "general",
    "future", "this year", "this month", "this week", "today"
]

# ============================================================================
# BLOCKED PATTERNS - Prompt injection attempts
# ============================================================================

BLOCKED_PATTERNS = [
    r"ignore\s*(previous|above|all)",
    r"forget\s*(previous|above|all)",
    r"disregard",
    r"system\s*prompt",
    r"you\s*are\s*now",
    r"pretend\s*to\s*be",
    r"act\s*as",
    r"new\s*instructions?",
    r"override",
    r"</?(system|user|assistant)>",
    r"\[INST\]",
    r"```(system|prompt)",
]

# Maximum question length
MAX_QUESTION_LENGTH = 100


def sanitize_input(text: Optional[str]) -> str:
    """Remove potentially dangerous characters and patterns."""
    if not text:
        return ""
    
    # Remove HTML/XML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove special characters except Thai, alphanumeric, and common punctuation
    text = re.sub(r'[^\u0E00-\u0E7Fa-zA-Z0-9\s\?\.,!]', '', text)
    
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text


def check_blocked_patterns(text: str) -> bool:
    """Check if text contains any blocked patterns."""
    text_lower = text.lower()
    
    for pattern in BLOCKED_PATTERNS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    
    return False


def validate_question(question: Optional[str], lang: str = "th") -> Tuple[bool, str, str]:
    """
    Validate and sanitize user question.
    
    Returns:
        Tuple of (is_valid, sanitized_question, error_message)
    """
    # Empty question is valid (general reading)
    if not question:
        return True, "", ""
    
    # Sanitize
    sanitized = sanitize_input(question)
    
    # Check length
    if len(sanitized) > MAX_QUESTION_LENGTH:
        return False, "", f"Question too long. Maximum {MAX_QUESTION_LENGTH} characters."
    
    # Check for blocked patterns
    if check_blocked_patterns(sanitized):
        return False, "", "Invalid question format."
    
    # Check if contains allowed topic (optional - can be strict or lenient)
    # For now, we allow any sanitized input that passes the above checks
    
    return True, sanitized, ""


def get_safe_question(question: Optional[str], lang: str = "th") -> str:
    """
    Get a safe version of the question for AI prompt.
    If validation fails, returns empty string for general reading.
    """
    is_valid, sanitized, _ = validate_question(question, lang)
    
    if not is_valid:
        return ""
    
    return sanitized
