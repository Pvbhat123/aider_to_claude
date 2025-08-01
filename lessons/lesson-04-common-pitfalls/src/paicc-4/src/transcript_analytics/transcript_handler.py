"""Alternative v2 transcript handler implementation."""

from pathlib import Path
from typing import Dict, Optional
from collections import Counter
import re

from .constants import word_blacklist
from .data_types import TranscriptAnalysisV2
from .llm import analyze_transcript_with_llm, get_sentiment


class TranscriptHandler:
    """Handler class for transcript processing."""
    
    def __init__(self, file_path: Path):
        """Initialize with transcript file path."""
        self.file_path = file_path
        self.text = self._read_file()
        self.word_frequencies: Dict[str, int] = {}
        
    def _read_file(self) -> str:
        """Read transcript file."""
        try:
            return self.file_path.read_text(encoding='utf-8')
        except Exception as e:
            raise RuntimeError(f"Failed to read transcript: {e}")
    
    def process(self, threshold: int = 5) -> TranscriptAnalysisV2:
        """Process transcript and return analysis."""
        # Tokenize and clean
        tokens = self._tokenize()
        
        # Count frequencies
        self.word_frequencies = self._count_frequencies(tokens, threshold)
        
        # Get top words
        top_words = sorted(
            self.word_frequencies.items(), 
            key=lambda x: x[1], 
            reverse=True
        )[:20]
        
        # Run LLM analysis
        llm_results = analyze_transcript_with_llm(self.text)
        
        # Get sentiment
        sentiment, sentiment_score = get_sentiment(self.text)
        
        return TranscriptAnalysisV2(
            word_frequencies=self.word_frequencies,
            total_words=len(tokens),
            unique_words=len(self.word_frequencies),
            top_words=top_words,
            llm_summary=llm_results["summary"],
            key_topics=llm_results["topics"],
            sentiment=sentiment,
            sentiment_score=sentiment_score
        )
    
    def _tokenize(self) -> list[str]:
        """Tokenize text into words."""
        # Remove URLs
        text = re.sub(r'https?://\S+', '', self.text)
        
        # Remove email addresses
        text = re.sub(r'\S+@\S+', '', text)
        
        # Convert to lowercase and split
        words = text.lower().split()
        
        # Clean and filter
        cleaned = []
        for word in words:
            # Remove punctuation
            word = re.sub(r'[^\w\s]', '', word)
            if word and word not in word_blacklist and len(word) > 2:
                cleaned.append(word)
        
        return cleaned
    
    def _count_frequencies(self, tokens: list[str], threshold: int) -> Dict[str, int]:
        """Count word frequencies with threshold."""
        counts = Counter(tokens)
        return {
            word: count 
            for word, count in counts.items() 
            if count >= threshold
        }
    
    def get_statistics(self) -> dict:
        """Get additional statistics about the transcript."""
        sentences = self.text.split('.')
        paragraphs = self.text.split('\n\n')
        
        return {
            "sentence_count": len([s for s in sentences if s.strip()]),
            "paragraph_count": len([p for p in paragraphs if p.strip()]),
            "avg_sentence_length": sum(len(s.split()) for s in sentences) / max(len(sentences), 1),
            "char_count": len(self.text),
            "char_count_no_spaces": len(self.text.replace(' ', ''))
        }