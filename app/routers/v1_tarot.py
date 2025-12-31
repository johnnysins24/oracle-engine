"""
Tarot API Router
Endpoints for drawing tarot cards
"""

from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from app.models.tarot_models import TarotCard, TarotDrawResponse
from app.engines.tarot import draw_cards, FULL_DECK

router = APIRouter(prefix="/test", tags=["Tarot Test"])


@router.get("/draw", response_model=TarotDrawResponse, summary="Draw a single tarot card")
async def draw_single_card():
    """
    Draw a single tarot card for quick guidance.
    
    Returns a random card from the 78-card Rider-Waite deck.
    """
    cards, spread_type, positions = draw_cards(1)
    
    return TarotDrawResponse(
        spread_type=spread_type,
        cards=[TarotCard(**card) for card in cards],
        positions=positions
    )


@router.get("/draw/{count}", response_model=TarotDrawResponse, summary="Draw multiple tarot cards")
async def draw_multiple_cards(
    count: int,
    spread: Optional[str] = Query(None, description="Spread type: single, past_present_future, celtic_cross")
):
    """
    Draw multiple tarot cards.
    
    - **count=1**: Single card draw
    - **count=3**: Past/Present/Future spread
    - **count=10**: Celtic Cross spread
    - **count=other**: Custom spread with numbered positions
    """
    if count < 1:
        raise HTTPException(status_code=400, detail="Count must be at least 1")
    if count > 78:
        raise HTTPException(status_code=400, detail="Cannot draw more than 78 cards")
    
    cards, spread_type, positions = draw_cards(count)
    
    return TarotDrawResponse(
        spread_type=spread_type,
        cards=[TarotCard(**card) for card in cards],
        positions=positions
    )


@router.get("/deck", summary="Get all cards in the deck")
async def get_full_deck():
    """
    Returns all 78 cards in the Rider-Waite tarot deck.
    
    Useful for exploring the deck or building UI components.
    """
    return {
        "total_cards": len(FULL_DECK),
        "deck": [TarotCard(**card) for card in FULL_DECK]
    }


@router.get("/deck/major", summary="Get Major Arcana cards")
async def get_major_arcana():
    """Returns all 22 Major Arcana cards (The Fool through The World)."""
    major = [card for card in FULL_DECK if card["arcana"] == "major"]
    return {
        "total_cards": len(major),
        "cards": [TarotCard(**card) for card in major]
    }


@router.get("/deck/minor/{suit}", summary="Get Minor Arcana cards by suit")
async def get_minor_by_suit(suit: str):
    """
    Returns all 14 cards of a specific suit.
    
    - **wands**: Fire element - creativity, passion, action
    - **cups**: Water element - emotions, relationships, intuition
    - **swords**: Air element - intellect, conflict, decisions
    - **pentacles**: Earth element - material, career, health
    """
    valid_suits = ["wands", "cups", "swords", "pentacles"]
    if suit.lower() not in valid_suits:
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid suit. Choose from: {', '.join(valid_suits)}"
        )
    
    suit_cards = [card for card in FULL_DECK if card.get("suit") == suit.lower()]
    return {
        "suit": suit.lower(),
        "total_cards": len(suit_cards),
        "cards": [TarotCard(**card) for card in suit_cards]
    }
