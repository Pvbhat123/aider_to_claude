import os
import re
from collections import Counter
from dotenv import load_dotenv
from .arg_parse import parse_arguments
from .constants import WORD_BLACKLIST
from .llm import analyze_transcript
from .output_format import format_as_str, format_as_json, format_as_markdown, format_as_yaml
from .chart import word_count_bar_chart


def main():
    load_dotenv()
    
    args = parse_arguments()
    
    print(f"Analyzing transcript: {args.transcript_path}")
    print(f"Minimum count threshold: {args.min_count_threshold}")
    
    with open(args.transcript_path, 'r', encoding='utf-8') as f:
        transcript_text = f.read()
    
    words = re.findall(r'\b[a-zA-Z]+\b', transcript_text.lower())
    
    word_count = Counter()
    
    for word in words:
        if word not in WORD_BLACKLIST:
            word_count[word] += 1
    
    filtered_word_count = {word: count for word, count in word_count.items() 
                          if count >= args.min_count_threshold}
    
    print(f"\nTotal unique words (excluding blacklist): {len(word_count)}")
    print(f"Words with frequency >= {args.min_count_threshold}: {len(filtered_word_count)}")
    
    word_count_bar_chart(filtered_word_count, args.min_count_threshold)
    
    print("\n" + "="*50)
    print("Analyzing transcript with LLM...")
    print("="*50 + "\n")
    
    analysis = analyze_transcript(transcript_text, filtered_word_count)
    
    # Format output based on selected format
    formatters = {
        "text": format_as_str,
        "json": format_as_json,
        "markdown": format_as_markdown,
        "yaml": format_as_yaml
    }
    
    formatter = formatters.get(args.output_format, format_as_str)
    formatted_output = formatter(analysis)
    
    # Print to console
    print(formatted_output)
    
    # Save to file if specified
    if args.output_file:
        # Determine file extension based on format
        extensions = {
            "text": ".txt",
            "json": ".json",
            "markdown": ".md",
            "yaml": ".yaml"
        }
        
        # Add extension if not present
        output_path = args.output_file
        if not output_path.suffix:
            output_path = output_path.with_suffix(extensions[args.output_format])
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(formatted_output)
        
        print(f"\n\nOutput saved to: {output_path}")


if __name__ == "__main__":
    main()