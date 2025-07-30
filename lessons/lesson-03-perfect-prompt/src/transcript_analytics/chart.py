import matplotlib.pyplot as plt


def word_count_bar_chart(word_count: dict, threshold: int):
    sorted_words = dict(sorted(word_count.items(), key=lambda x: x[1], reverse=True))
    
    words = list(sorted_words.keys())[:20]
    counts = list(sorted_words.values())[:20]
    
    if not words:
        print(f"No words found with frequency >= {threshold}")
        return
    
    plt.figure(figsize=(10, 8))
    plt.barh(words[::-1], counts[::-1])
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title(f'Top Word Frequencies (threshold >= {threshold})')
    plt.tight_layout()
    plt.show()