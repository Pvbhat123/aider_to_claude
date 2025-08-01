"""Transcript processing with logging support."""

import logging
from pathlib import Path
from collections import Counter
from typing import Dict, List, Tuple

from .constants import word_blacklist
from .data_types import TranscriptAnalysis
from .llm import analyze_transcript_with_llm

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def process_transcript_with_logging(
    file_path: Path,
    threshold: int = 5
) -> TranscriptAnalysis:
    """Process transcript with detailed logging."""
    logger.info(f"Starting transcript processing for: {file_path}")
    
    # Read file
    logger.info("Reading transcript file...")
    try:
        text = file_path.read_text(encoding='utf-8')
        logger.info(f"Successfully read {len(text)} characters")
    except Exception as e:
        logger.error(f"Failed to read file: {e}")
        raise
    
    # Process words
    logger.info("Tokenizing and cleaning text...")
    words = text.lower().split()
    initial_count = len(words)
    
    cleaned_words = []
    for word in words:
        word = word.strip('.,!?;:"\'()-[]{}')
        if word and word not in word_blacklist and len(word) > 2:
            cleaned_words.append(word)
    
    logger.info(f"Cleaned {initial_count} words down to {len(cleaned_words)}")
    
    # Count frequencies
    logger.info("Counting word frequencies...")
    word_counts = Counter(cleaned_words)
    word_frequencies = {
        word: count 
        for word, count in word_counts.items() 
        if count >= threshold
    }
    
    logger.info(f"Found {len(word_frequencies)} words meeting threshold of {threshold}")
    
    # Get top words
    top_words = sorted(
        word_frequencies.items(), 
        key=lambda x: x[1], 
        reverse=True
    )[:20]
    
    # LLM analysis
    logger.info("Running AI analysis...")
    llm_results = analyze_transcript_with_llm(text)
    
    # Log summary
    logger.info("Analysis complete!")
    logger.info(f"Top 5 words: {', '.join([w[0] for w in top_words[:5]])}")
    
    return TranscriptAnalysis(
        word_frequencies=word_frequencies,
        total_words=len(words),
        unique_words=len(word_frequencies),
        top_words=top_words,
        llm_summary=llm_results["summary"],
        key_topics=llm_results["topics"]
    )


def batch_process_transcripts(
    file_paths: List[Path],
    threshold: int = 5
) -> Dict[str, TranscriptAnalysis]:
    """Process multiple transcripts and return results."""
    results = {}
    
    logger.info(f"Starting batch processing of {len(file_paths)} files")
    
    for i, file_path in enumerate(file_paths, 1):
        logger.info(f"Processing file {i}/{len(file_paths)}: {file_path.name}")
        try:
            analysis = process_transcript_with_logging(file_path, threshold)
            results[file_path.name] = analysis
        except Exception as e:
            logger.error(f"Failed to process {file_path.name}: {e}")
            continue
    
    logger.info(f"Batch processing complete. Successfully processed {len(results)} files")
    return results


def generate_comparison_report(analyses: Dict[str, TranscriptAnalysis]) -> str:
    """Generate a comparison report for multiple transcript analyses."""
    logger.info("Generating comparison report...")
    
    report = []
    report.append("TRANSCRIPT COMPARISON REPORT")
    report.append("=" * 60)
    
    for filename, analysis in analyses.items():
        report.append(f"\n{filename}")
        report.append("-" * len(filename))
        report.append(f"Total words: {analysis.total_words}")
        report.append(f"Unique words: {analysis.unique_words}")
        report.append(f"Top 3 words: {', '.join([w[0] for w in analysis.top_words[:3]])}")
        if analysis.key_topics:
            report.append(f"Key topics: {', '.join(analysis.key_topics[:3])}")
    
    return "\n".join(report)