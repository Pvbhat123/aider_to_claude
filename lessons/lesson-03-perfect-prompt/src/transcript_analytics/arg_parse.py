import argparse
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze transcript files for word frequency and generate insights using LLM"
    )
    
    parser.add_argument(
        "transcript_path",
        type=Path,
        help="Path to the transcript file to analyze"
    )
    
    parser.add_argument(
        "--min_count_threshold",
        type=int,
        default=3,
        help="Minimum word count threshold for frequency analysis (default: 3)"
    )
    
    parser.add_argument(
        "--output_format",
        type=str,
        choices=["text", "json", "markdown", "yaml"],
        default="text",
        help="Output format for the analysis results (default: text)"
    )
    
    parser.add_argument(
        "--output_file",
        type=Path,
        help="Path to save the output file (optional)"
    )
    
    args = parser.parse_args()
    
    if not args.transcript_path.exists():
        parser.error(f"Transcript file not found: {args.transcript_path}")
    
    if not args.transcript_path.is_file():
        parser.error(f"Path is not a file: {args.transcript_path}")
    
    if args.min_count_threshold < 1:
        parser.error("Minimum count threshold must be at least 1")
    
    return args