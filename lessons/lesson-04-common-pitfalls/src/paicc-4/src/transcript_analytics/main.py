import os
import sys
from pathlib import Path
from collections import Counter
from typing import Dict

from .arg_parse import parse_arguments
from .constants import word_blacklist, DEFAULT_THRESHOLD
from .llm import analyze_transcript
from .chart import word_count_bar_chart, word_count_pie_chart, word_count_line_chart
from .output_format import format_as_json, format_as_markdown, format_as_yaml, format_as_text


def count_words(text: str, threshold: int = DEFAULT_THRESHOLD) -> Dict[str, int]:
    words = text.lower().split()
    word_counts = Counter(words)
    
    filtered_counts = {
        word: count for word, count in word_counts.items()
        if word not in word_blacklist and count >= threshold
    }
    
    return dict(sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True))


def main():
    args = parse_arguments()
    
    if not os.path.exists(args.transcript_file):
        print(f"Error: File '{args.transcript_file}' not found.")
        sys.exit(1)
    
    try:
        with open(args.transcript_file, 'r', encoding='utf-8') as f:
            transcript_text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    word_freq = count_words(transcript_text, args.threshold)
    
    if not args.output_format or args.output_format == 'text':
        print("\nWord Frequency Analysis:")
        print("-" * 40)
        for word, count in word_freq.items():
            print(f"{word}: {count}")
        return
    
    analysis = analyze_transcript(transcript_text, args.threshold)
    
    chart_paths = []
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    try:
        bar_chart_path = word_count_bar_chart(word_freq, str(output_dir))
        pie_chart_path = word_count_pie_chart(word_freq, str(output_dir))
        line_chart_path = word_count_line_chart(word_freq, str(output_dir))
        chart_paths = [bar_chart_path, pie_chart_path, line_chart_path]
        print(f"Charts saved: {', '.join(chart_paths)}")
    except Exception as e:
        print(f"Warning: Could not generate charts: {e}")
    
    output_filename = args.output_file
    if not output_filename:
        base_name = Path(args.transcript_file).stem
        output_filename = f"analysis.{args.output_format}"
    
    try:
        if args.output_format == 'json':
            output_content = format_as_json(analysis)
        elif args.output_format == 'yaml':
            output_content = format_as_yaml(analysis)
        elif args.output_format == 'markdown':
            output_content = format_as_markdown(analysis, chart_paths)
        else:
            output_content = format_as_text(analysis)
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(output_content)
        
        print(f"\nAnalysis saved to: {output_filename}")
        print("\n" + output_content[:500] + "..." if len(output_content) > 500 else output_content)
        
    except Exception as e:
        print(f"Error generating output: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()