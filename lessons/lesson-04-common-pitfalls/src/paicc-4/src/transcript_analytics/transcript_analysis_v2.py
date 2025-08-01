"""Alternative transcript analysis implementation with sentiment detection."""

from collections import Counter
from typing import Dict, List, Tuple
from .constants import word_blacklist
from .data_types import TranscriptAnalysisV2
from .llm import analyze_transcript_with_llm, get_sentiment


def analyze_transcript_v2(text: str, threshold: int = 5) -> TranscriptAnalysisV2:
    """Analyze transcript with sentiment detection."""
    # Basic word frequency analysis
    words = text.lower().split()
    cleaned_words = []
    
    for word in words:
        word = word.strip('.,!?;:"\'()-[]{}')
        if word and word not in word_blacklist and len(word) > 2:
            cleaned_words.append(word)
    
    word_counts = Counter(cleaned_words)
    word_frequencies = {word: count for word, count in word_counts.items() if count >= threshold}
    
    # Get top words
    top_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:20]
    
    # LLM analysis
    llm_results = analyze_transcript_with_llm(text)
    
    # Sentiment analysis
    sentiment, sentiment_score = get_sentiment(text)
    
    # Create and return analysis object
    return TranscriptAnalysisV2(
        word_frequencies=word_frequencies,
        total_words=len(words),
        unique_words=len(word_frequencies),
        top_words=top_words,
        llm_summary=llm_results["summary"],
        key_topics=llm_results["topics"],
        sentiment=sentiment,
        sentiment_score=sentiment_score
    )


def get_word_context(text: str, target_word: str, window: int = 50) -> List[str]:
    """Get context snippets for a specific word."""
    contexts = []
    text_lower = text.lower()
    word_lower = target_word.lower()
    
    # Find all occurrences
    start = 0
    while True:
        pos = text_lower.find(word_lower, start)
        if pos == -1:
            break
        
        # Extract context window
        context_start = max(0, pos - window)
        context_end = min(len(text), pos + len(word_lower) + window)
        context = text[context_start:context_end]
        
        # Clean up context
        if context_start > 0:
            context = "..." + context
        if context_end < len(text):
            context = context + "..."
        
        contexts.append(context)
        start = pos + 1
        
        # Limit to 5 contexts
        if len(contexts) >= 5:
            break
    
    return contexts