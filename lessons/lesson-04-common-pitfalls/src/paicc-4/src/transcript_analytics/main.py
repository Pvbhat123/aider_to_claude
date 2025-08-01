"""Main entry point for transcript analytics tool."""

import sys
from pathlib import Path
from collections import Counter
from typing import Dict

from .arg_parse import parse_arguments
from .constants import word_blacklist
from .data_types import TranscriptAnalysis
from .chart import word_count_bar_chart, word_count_pie_chart, word_count_line_chart
from .llm import analyze_transcript_with_llm
from .output_format import format_output


def read_transcript(file_path: Path) -> str:
    """Read transcript from file."""
    try:
        return file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def count_words(text: str, threshold: int = 5) -> Dict[str, int]:
    """Count word frequencies, filtering by blacklist and threshold."""
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Remove punctuation and filter
    cleaned_words = []
    for word in words:
        # Remove common punctuation
        word = word.strip('.,!?;:"\'()-[]{}')
        if word and word not in word_blacklist and len(word) > 2:
            cleaned_words.append(word)
    
    # Count frequencies
    word_counts = Counter(cleaned_words)
    
    # Filter by threshold
    return {word: count for word, count in word_counts.items() if count >= threshold}


def main():
    """Main function to orchestrate transcript analysis."""
    # Parse arguments
    args = parse_arguments()
    
    # Read transcript
    print(f"Reading transcript from {args.transcript_file}...")
    transcript_text = read_transcript(args.transcript_file)
    
    # Count words
    print(f"Analyzing word frequencies (threshold: {args.threshold})...")
    word_frequencies = count_words(transcript_text, args.threshold)
    
    # Get top words
    top_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)[:20]
    
    # Create visualizations
    print("Generating visualizations...")
    word_count_bar_chart(word_frequencies)
    word_count_pie_chart(word_frequencies, top_n=10)
    word_count_line_chart(word_frequencies)
    
    # LLM analysis
    print("Running AI analysis...")
    llm_results = analyze_transcript_with_llm(transcript_text)
    
    # Create analysis object
    analysis = TranscriptAnalysis(
        word_frequencies=word_frequencies,
        total_words=len(transcript_text.split()),
        unique_words=len(word_frequencies),
        top_words=top_words,
        llm_summary=llm_results["summary"],
        key_topics=llm_results["topics"]
    )
    
    # Format and display output
    formatted_output = format_output(analysis, args.output_format)
    print("\n" + "="*50 + "\n")
    print(formatted_output)


if __name__ == "__main__":
    main()