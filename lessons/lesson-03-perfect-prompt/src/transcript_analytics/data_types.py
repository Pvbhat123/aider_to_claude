from typing import List
from pydantic import BaseModel, Field


class TranscriptAnalysis(BaseModel):
    quick_summary: str = Field(
        description="A brief 2-3 sentence overview of the transcript's main topic and key points"
    )
    
    bullet_point_highlights: List[str] = Field(
        description="A list of 5-7 key highlights or takeaways from the transcript"
    )
    
    sentiment_analysis: str = Field(
        description="Analysis of the overall emotional tone and sentiment of the transcript (e.g., positive, negative, neutral, informative, persuasive)"
    )
    
    keywords: List[str] = Field(
        description="A list of 5-10 important keywords or phrases that capture the essence of the transcript"
    )