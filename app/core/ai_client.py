"""
Google Gemini AI Client
Wrapper for Google Generative AI SDK
"""

import google.generativeai as genai
from typing import Optional
from app.core.config import settings


# Configure the API
def get_gemini_client():
    """Initialize and return Gemini client."""
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY not configured. Add it to your .env file.")
    
    genai.configure(api_key=settings.GEMINI_API_KEY)
    return genai


def get_model(model_name: str = "gemini-2.0-flash-exp"):
    """Get a Gemini model instance."""
    client = get_gemini_client()
    return client.GenerativeModel(model_name)


async def generate_interpretation(
    prompt: str,
    system_instruction: Optional[str] = None,
    model_name: str = "gemini-2.0-flash-exp",
    temperature: float = 0.9,
    max_tokens: int = 1024
) -> str:
    """
    Generate AI interpretation using Gemini.
    
    Args:
        prompt: The user prompt with context
        system_instruction: System prompt for persona
        model_name: Gemini model to use
        temperature: Creativity level (0-1)
        max_tokens: Maximum response length
        
    Returns:
        Generated text response
    """
    try:
        client = get_gemini_client()
        
        # Create model with system instruction
        model = client.GenerativeModel(
            model_name=model_name,
            system_instruction=system_instruction,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_tokens,
            }
        )
        
        # Generate response
        response = model.generate_content(prompt)
        
        return response.text
        
    except Exception as e:
        # Return error message for debugging
        return f"❌ AI Error: {str(e)}"


async def generate_tarot_reading(
    cards: list,
    question: Optional[str] = None,
    spread_type: str = "single",
    lang: str = "th"
) -> str:
    """Generate AI interpretation for tarot cards."""
    from app.core.prompts import TAROT_GYPSY_PROMPT, build_tarot_prompt
    
    prompt = build_tarot_prompt(cards, question, spread_type, lang)
    system = TAROT_GYPSY_PROMPT if lang == "th" else TAROT_GYPSY_PROMPT
    
    return await generate_interpretation(prompt, system_instruction=system)


async def generate_thai_fortune(
    birth_data: dict,
    question: Optional[str] = None
) -> str:
    """Generate AI Thai fortune reading."""
    from app.core.prompts import THAI_FORTUNE_PROMPT, build_thai_prompt
    
    prompt = build_thai_prompt(birth_data, question)
    
    return await generate_interpretation(prompt, system_instruction=THAI_FORTUNE_PROMPT)
