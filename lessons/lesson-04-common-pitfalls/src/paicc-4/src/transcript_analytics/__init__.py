from .data_types import TranscriptAnalysis, TranscriptAnalysisV2, TranscriptAnalysisVNext
from .llm import analyze_transcript, analyze_with_sentiment
from .transcript_analysis_v2 import analyze_transcript_v2, get_enhanced_analysis
from .transcript_handler import TranscriptHandler
from .transcript_processing import process_transcript_with_logging, batch_process_transcripts, quick_analysis

__version__ = "0.1.0"

__all__ = [
    "TranscriptAnalysis",
    "TranscriptAnalysisV2",
    "TranscriptAnalysisVNext",
    "analyze_transcript",
    "analyze_with_sentiment",
    "analyze_transcript_v2",
    "get_enhanced_analysis",
    "TranscriptHandler",
    "process_transcript_with_logging",
    "batch_process_transcripts",
    "quick_analysis",
]


def hello():
    print(f"Transcript Analytics v{__version__}")
    print("A CLI tool for analyzing transcripts with AI-powered insights")
    return "Hello from transcript_analytics!"