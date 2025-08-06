import string
from collections import Counter
from .data_types import WordCounts
from .constants import COMMON_WORDS_BLACKLIST


def word_counter(script: str, min_count_threshold: int = 10) -> WordCounts:
    """
    Count word frequencies in a script, filtering out common words and punctuation.
    
    Args:
        script: The input text to analyze
        min_count_threshold: Minimum count for a word to be included
        
    Returns:
        WordCounts object with word frequency map
    """
    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_script = script.translate(translator).lower()
    
    # Split into words
    words = cleaned_script.split()
    
    # Count word frequencies
    word_freq = Counter(words)
    
    # Filter out common words and apply threshold
    filtered_counts = {
        word: count 
        for word, count in word_freq.items() 
        if word not in COMMON_WORDS_BLACKLIST and count >= min_count_threshold
    }
    
    # Sort by count descending
    sorted_counts = dict(sorted(filtered_counts.items(), key=lambda x: x[1], reverse=True))
    
    return WordCounts(count_to_word_map=sorted_counts)