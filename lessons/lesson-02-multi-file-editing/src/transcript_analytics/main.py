from collections import Counter
import string

try:
    from .arg_parse import parse_arguments
    from .constants import WORD_BLACKLIST
    from .llm import analyze_transcript
except ImportError:
    from arg_parse import parse_arguments
    from constants import WORD_BLACKLIST
    from llm import analyze_transcript

def main():
    args = parse_arguments()
    
    with open(args.transcript_file, "r") as f:
        transcript = f.read()
    
    # Strip punctuation and convert to lowercase
    words = []
    for word in transcript.lower().split():
        # Remove punctuation from the end of words
        cleaned_word = word.rstrip(',.?!')
        # Remove punctuation from the beginning of words
        cleaned_word = cleaned_word.lstrip(',.?!')
        if cleaned_word:  # Only add non-empty words
            words.append(cleaned_word)
    
    word_count = Counter(words)
    
    # Filter out blacklisted words
    filtered_word_count = {word: count for word, count in word_count.items() 
                          if word not in WORD_BLACKLIST}
    
    min_count_threshold = args.min_count
    filtered_words = {word: count for word, count in filtered_word_count.items() 
                     if count >= min_count_threshold}
    
    sorted_words = sorted(filtered_words.items(), key=lambda x: x[1], reverse=True)
    
    print("Word frequency analysis:")
    for word, count in sorted_words[:20]:
        print(f"{word}: {count}")
    
    # Analyze transcript with Gemini
    print("\n" + "="*50 + "\n")
    print("AI-Powered Transcript Analysis:")
    print("="*50 + "\n")
    
    analysis = analyze_transcript(transcript, sorted_words)
    
    print(f"Quick Summary:\n{analysis.quick_summary}\n")
    
    print("Key Highlights:")
    for highlight in analysis.bullet_point_highlights:
        print(f"  • {highlight}")
    
    print(f"\nSentiment Analysis: {analysis.sentiment_analysis}\n")
    
    print("Keywords:")
    print(", ".join(analysis.keywords))

if __name__ == "__main__":
    main()