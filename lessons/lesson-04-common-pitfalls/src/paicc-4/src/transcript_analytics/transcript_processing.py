import logging
from typing import Dict, Optional
from pathlib import Path
from .llm import analyze_with_sentiment
from .data_types import TranscriptAnalysisV2
from .constants import DEFAULT_THRESHOLD

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def process_transcript_with_logging(
    transcript_path: str, 
    threshold: int = DEFAULT_THRESHOLD,
    verbose: bool = True
) -> TranscriptAnalysisV2:
    
    if verbose:
        logger.info(f"Starting transcript processing for: {transcript_path}")
    
    if not Path(transcript_path).exists():
        logger.error(f"File not found: {transcript_path}")
        raise FileNotFoundError(f"Transcript file not found: {transcript_path}")
    
    try:
        if verbose:
            logger.info("Reading transcript file...")
        
        with open(transcript_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        file_size = len(text)
        if verbose:
            logger.info(f"Loaded transcript: {file_size:,} characters")
        
        if verbose:
            logger.info(f"Analyzing with threshold: {threshold}")
        
        analysis = analyze_with_sentiment(text, threshold)
        
        if verbose:
            logger.info("Analysis complete!")
            logger.info(f"Found {analysis.total_words:,} total words")
            logger.info(f"Found {analysis.unique_words:,} unique words")
            logger.info(f"Sentiment: {analysis.sentiment}")
            logger.info(f"Keywords: {', '.join(analysis.keywords[:5])}")
        
        return analysis
    
    except Exception as e:
        logger.error(f"Error during processing: {str(e)}")
        raise


def batch_process_transcripts(
    transcript_paths: list[str],
    threshold: int = DEFAULT_THRESHOLD
) -> Dict[str, TranscriptAnalysisV2]:
    
    results = {}
    logger.info(f"Starting batch processing of {len(transcript_paths)} transcripts")
    
    for i, path in enumerate(transcript_paths, 1):
        logger.info(f"Processing transcript {i}/{len(transcript_paths)}: {path}")
        
        try:
            analysis = process_transcript_with_logging(path, threshold, verbose=False)
            results[path] = analysis
            logger.info(f"✓ Successfully processed: {Path(path).name}")
        
        except Exception as e:
            logger.error(f"✗ Failed to process {path}: {str(e)}")
            results[path] = None
    
    successful = sum(1 for v in results.values() if v is not None)
    logger.info(f"Batch processing complete: {successful}/{len(transcript_paths)} successful")
    
    return results


def quick_analysis(text: str, verbose: bool = False) -> Dict:
    if verbose:
        print("Performing quick analysis...")
    
    analysis = analyze_with_sentiment(text, DEFAULT_THRESHOLD)
    
    result = {
        "summary": analysis.summary,
        "sentiment": analysis.sentiment,
        "top_keywords": analysis.keywords[:5],
        "word_stats": {
            "total": analysis.total_words,
            "unique": analysis.unique_words
        },
        "top_words": dict(list(analysis.word_count.items())[:10])
    }
    
    if verbose:
        print("Quick analysis complete!")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Top Keywords: {', '.join(result['top_keywords'])}")
    
    return result