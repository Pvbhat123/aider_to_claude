#!/usr/bin/env python3

import sys
from pathlib import Path
from datetime import datetime

from argparse_module import parse_arguments
from gemini_llm import GeminiAnalyzer
from chart import generate_bar_chart, generate_pie_chart
from output_format import (
    format_as_json,
    format_as_yaml,
    format_as_text,
    format_as_markdown,
    format_as_html_with_slider
)

def get_output_filename(format_type: str, custom_filename: str = None) -> str:
    if custom_filename:
        return custom_filename
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    extensions = {
        "json": "json",
        "yaml": "yaml",
        "markdown": "md",
        "text": "txt",
        "html": "html"
    }
    
    ext = extensions.get(format_type, "txt")
    return f"analysis_{timestamp}.{ext}"

def main():
    args = parse_arguments()
    
    if not Path(args.transcript_file).exists():
        print(f"Error: File '{args.transcript_file}' not found", file=sys.stderr)
        sys.exit(1)
    
    with open(args.transcript_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Analyzing transcript...")
    analyzer = GeminiAnalyzer()
    analysis = analyzer.analyze_transcript(text, args.min_count)
    
    bar_chart_path = None
    pie_chart_path = None
    
    if not args.no_charts:
        print("Generating visualizations...")
        bar_chart_path = generate_bar_chart(analysis.word_count)
        pie_chart_path = generate_pie_chart(analysis.word_count)
        if bar_chart_path:
            print(f"Bar chart saved to: {bar_chart_path}")
        if pie_chart_path:
            print(f"Pie chart saved to: {pie_chart_path}")
    
    if args.output_format == "json":
        output_content = format_as_json(analysis)
    elif args.output_format == "yaml":
        output_content = format_as_yaml(analysis)
    elif args.output_format == "markdown":
        output_content = format_as_markdown(analysis, bar_chart_path, pie_chart_path)
    elif args.output_format == "html":
        output_content = format_as_html_with_slider(analysis)
    else:
        output_content = format_as_text(analysis)
    
    print(output_content)
    
    output_file = get_output_filename(args.output_format, args.output_file)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    print(f"\nAnalysis saved to: {output_file}")

if __name__ == "__main__":
    main()