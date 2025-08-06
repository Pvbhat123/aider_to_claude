import os
from typing import Dict
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def word_count_bar_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str:
    os.makedirs(output_dir, exist_ok=True)
    
    if not freq_dict:
        return ""
    
    top_20 = dict(list(freq_dict.items())[:20])
    
    words = list(top_20.keys())
    counts = list(top_20.values())
    
    max_count = max(counts)
    min_count = min(counts)
    range_count = max_count - min_count if max_count != min_count else 1
    
    colors = []
    for count in counts:
        normalized = (count - min_count) / range_count
        if normalized > 0.75:
            colors.append('green')
        elif normalized < 0.25:
            colors.append('red')
        else:
            colors.append('blue')
    
    plt.figure(figsize=(12, 6))
    plt.barh(words[::-1], counts[::-1], color=colors[::-1])
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title('Top 20 Word Frequency Analysis')
    plt.tight_layout()
    
    output_path = os.path.join(output_dir, 'word_frequency_bar.png')
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    return output_path


def word_count_pie_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str:
    os.makedirs(output_dir, exist_ok=True)
    
    if not freq_dict:
        return ""
    
    top_10 = dict(list(freq_dict.items())[:10])
    
    labels = list(top_10.keys())
    sizes = list(top_10.values())
    
    other_count = sum(list(freq_dict.values())[10:]) if len(freq_dict) > 10 else 0
    if other_count > 0:
        labels.append('Others')
        sizes.append(other_count)
    
    plt.figure(figsize=(10, 8))
    colors = plt.cm.Set3(range(len(labels)))
    
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Word Distribution (Top 10 + Others)')
    
    output_path = os.path.join(output_dir, 'word_frequency_pie.png')
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    return output_path


def word_count_line_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str:
    os.makedirs(output_dir, exist_ok=True)
    
    if not freq_dict:
        return ""
    
    top_30 = dict(list(freq_dict.items())[:30])
    
    positions = list(range(1, len(top_30) + 1))
    counts = list(top_30.values())
    
    plt.figure(figsize=(12, 6))
    plt.plot(positions, counts, marker='o', linestyle='-', linewidth=2, markersize=6)
    plt.xlabel('Word Rank')
    plt.ylabel('Frequency')
    plt.title('Word Frequency Distribution (Zipf\'s Law)')
    plt.grid(True, alpha=0.3)
    
    for i in range(0, len(positions), 5):
        plt.annotate(list(top_30.keys())[i], 
                    xy=(positions[i], counts[i]),
                    xytext=(5, 5), 
                    textcoords='offset points',
                    fontsize=8,
                    alpha=0.7)
    
    plt.tight_layout()
    
    output_path = os.path.join(output_dir, 'word_frequency_line.png')
    plt.savefig(output_path, dpi=100, bbox_inches='tight')
    plt.close()
    
    return output_path