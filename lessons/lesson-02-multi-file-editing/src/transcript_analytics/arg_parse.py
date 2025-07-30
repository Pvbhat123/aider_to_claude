import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Analyze transcript word frequencies")
    parser.add_argument("transcript_file", help="Path to the transcript file")
    parser.add_argument("--min-count", type=int, default=3, help="Minimum count threshold for words")
    args = parser.parse_args()
    return args