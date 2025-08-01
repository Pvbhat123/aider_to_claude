"""Data visualization functions for transcript analysis."""

import matplotlib.pyplot as plt
from typing import Dict, List, Tuple


def word_count_bar_chart(word_counts: Dict[str, int], top_n: int = 20) -> None:
    """Create a bar chart of top word frequencies."""
    # Sort and get top N words
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*sorted_words) if sorted_words else ([], [])
    
    # Create bar chart
    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(len(words)), counts)
    
    # Color coding: top quartile green, bottom quartile red, rest blue
    quartile_size = len(bars) // 4
    for i, bar in enumerate(bars):
        if i < quartile_size:
            bar.set_color('green')
        elif i >= len(bars) - quartile_size:
            bar.set_color('red')
        else:
            bar.set_color('blue')
    
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title(f'Top {top_n} Word Frequencies')
    plt.xticks(range(len(words)), words, rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def word_count_pie_chart(word_counts: Dict[str, int], top_n: int = 10) -> None:
    """Create a pie chart of top word frequencies."""
    # Sort and get top N words
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    
    if not sorted_words:
        print("No data to display in pie chart")
        return
    
    words, counts = zip(*sorted_words)
    
    # Add "Others" category
    total_count = sum(word_counts.values())
    top_count = sum(counts)
    other_count = total_count - top_count
    
    if other_count > 0:
        words = list(words) + ['Others']
        counts = list(counts) + [other_count]
    
    # Create pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(counts, labels=words, autopct='%1.1f%%', startangle=90)
    plt.title(f'Top {top_n} Word Distribution')
    plt.axis('equal')
    plt.show()


def word_count_line_chart(word_counts: Dict[str, int], top_n: int = 30) -> None:
    """Create a line chart showing word frequency distribution."""
    # Sort words by frequency
    sorted_counts = sorted(word_counts.values(), reverse=True)[:top_n]
    
    if not sorted_counts:
        print("No data to display in line chart")
        return
    
    # Create line chart
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(sorted_counts) + 1), sorted_counts, marker='o', markersize=4)
    plt.xlabel('Word Rank')
    plt.ylabel('Frequency')
    plt.title('Word Frequency Distribution')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()