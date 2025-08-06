from .llm import analyze_with_sentiment
from .data_types import TranscriptAnalysisV2
from .constants import DEFAULT_THRESHOLD


def analyze_transcript_v2(text: str, threshold: int = DEFAULT_THRESHOLD) -> TranscriptAnalysisV2:
    return analyze_with_sentiment(text, threshold)


def get_enhanced_analysis(transcript_path: str, threshold: int = DEFAULT_THRESHOLD) -> TranscriptAnalysisV2:
    with open(transcript_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    return analyze_with_sentiment(text, threshold)