"""Data models and type definitions."""

from typing import Dict, List
from pydantic import BaseModel

class TranscriptAnalysis(BaseModel):
    summary: str
    bullet_points: List[str]
    keywords: List[str]
    sentiment: str
    word_count: Dict[str, int]
    total_words: int
    unique_words: int