"""Command-line argument parsing for transcript analytics."""

import argparse
from pathlib import Path


def parse_arguments():
    """Parse command-line arguments for transcript analysis."""
    parser = argparse.ArgumentParser(
        description="Analyze transcript files for word frequency and insights"
    )
    
    parser.add_argument(
        "transcript_file",
        type=Path,
        help="Path to the transcript file to analyze"
    )
    
    parser.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="Minimum word frequency threshold (default: 5)"
    )
    
    parser.add_argument(
        "--output-format",
        choices=["text", "json", "yaml", "markdown"],
        default="text",
        help="Output format for results (default: text)"
    )
    
    args = parser.parse_args()
    
    # Validate file exists
    if not args.transcript_file.exists():
        parser.error(f"Transcript file not found: {args.transcript_file}")
    
    return args