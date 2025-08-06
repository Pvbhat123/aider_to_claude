import argparse
from .constants import SUPPORTED_FORMATS, DEFAULT_THRESHOLD


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Analyze transcript files with AI-powered insights",
        prog="transcript_analytics"
    )
    
    parser.add_argument(
        "transcript_file",
        type=str,
        help="Path to the transcript file to analyze"
    )
    
    parser.add_argument(
        "--threshold",
        type=int,
        default=DEFAULT_THRESHOLD,
        help=f"Minimum word count threshold (default: {DEFAULT_THRESHOLD})"
    )
    
    parser.add_argument(
        "--output-format",
        choices=SUPPORTED_FORMATS,
        default="text",
        help="Output format for the analysis (default: text)"
    )
    
    parser.add_argument(
        "--output-file",
        type=str,
        help="Custom output filename (auto-generated if not specified)"
    )
    
    return parser.parse_args()