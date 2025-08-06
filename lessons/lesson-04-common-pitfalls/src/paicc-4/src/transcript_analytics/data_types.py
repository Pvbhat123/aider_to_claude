from typing import List, Dict, Optional
from pydantic import BaseModel


class TranscriptAnalysis(BaseModel):
    summary: str
    bullet_points: List[str]
    keywords: List[str]
    word_count: Dict[str, int]
    total_words: int
    unique_words: int


class TranscriptAnalysisV2(BaseModel):
    summary: str
    bullet_points: List[str]
    keywords: List[str]
    sentiment: str
    word_count: Dict[str, int]
    total_words: int
    unique_words: int


class TranscriptAnalysisVNext(BaseModel):
    summary: str
    bullet_points: List[str]
    keywords: List[str]
    sentiment: str
    word_count: Dict[str, int]
    total_words: int
    unique_words: int
    topics: Optional[List[str]] = None
    entities: Optional[Dict[str, List[str]]] = None
    confidence_score: Optional[float] = None