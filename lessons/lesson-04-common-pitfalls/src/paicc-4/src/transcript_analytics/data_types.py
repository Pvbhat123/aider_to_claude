"""Pydantic data models for transcript analysis results."""

from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class TranscriptAnalysis(BaseModel):
    """Base model for transcript analysis results."""
    word_frequencies: Dict[str, int] = Field(
        description="Dictionary of words and their frequencies"
    )
    total_words: int = Field(description="Total number of words in transcript")
    unique_words: int = Field(description="Number of unique words")
    top_words: List[tuple[str, int]] = Field(
        description="List of top words and their counts"
    )
    llm_summary: Optional[str] = Field(
        default=None, description="AI-generated summary of the transcript"
    )
    key_topics: Optional[List[str]] = Field(
        default=None, description="Key topics identified by AI"
    )


class TranscriptAnalysisV2(BaseModel):
    """Extended model with sentiment analysis."""
    word_frequencies: Dict[str, int] = Field(
        description="Dictionary of words and their frequencies"
    )
    total_words: int = Field(description="Total number of words in transcript")
    unique_words: int = Field(description="Number of unique words")
    top_words: List[tuple[str, int]] = Field(
        description="List of top words and their counts"
    )
    llm_summary: Optional[str] = Field(
        default=None, description="AI-generated summary of the transcript"
    )
    key_topics: Optional[List[str]] = Field(
        default=None, description="Key topics identified by AI"
    )
    sentiment: Optional[str] = Field(
        default=None, description="Overall sentiment (positive/negative/neutral)"
    )
    sentiment_score: Optional[float] = Field(
        default=None, description="Sentiment score (-1 to 1)"
    )


class TranscriptAnalysisVNext(BaseModel):
    """Future version with additional features."""
    word_frequencies: Dict[str, int] = Field(
        description="Dictionary of words and their frequencies"
    )
    total_words: int = Field(description="Total number of words in transcript")
    unique_words: int = Field(description="Number of unique words")
    top_words: List[tuple[str, int]] = Field(
        description="List of top words and their counts"
    )
    llm_summary: Optional[str] = Field(
        default=None, description="AI-generated summary of the transcript"
    )
    key_topics: Optional[List[str]] = Field(
        default=None, description="Key topics identified by AI"
    )
    sentiment: Optional[str] = Field(
        default=None, description="Overall sentiment"
    )
    sentiment_score: Optional[float] = Field(
        default=None, description="Sentiment score"
    )
    speaker_segments: Optional[List[Dict]] = Field(
        default=None, description="Identified speaker segments"
    )
    action_items: Optional[List[str]] = Field(
        default=None, description="Extracted action items"
    )
    questions: Optional[List[str]] = Field(
        default=None, description="Questions raised in the transcript"
    )