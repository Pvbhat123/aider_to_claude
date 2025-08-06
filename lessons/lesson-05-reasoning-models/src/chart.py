import os
from datetime import datetime
from pathlib import Path
from typing import Dict

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def generate_bar_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str:
    Path(output_dir).mkdir(exist_ok=True)
    
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:20]
    
    if not sorted_items:
        return ""
    
    words, counts = zip(*sorted_items)
    
    max_count = max(counts)
    colors = []
    for count in counts:
        if count > max_count * 0.8:
            colors.append('#FF6B6B')  # Red for high frequency
        elif count > max_count * 0.5:
            colors.append('#4ECDC4')  # Teal for medium frequency
        else:
            colors.append('#95E77E')  # Green for low frequency
    
    fig, ax = plt.subplots(figsize=(12, 8))
    
    bars = ax.barh(range(len(words)), counts, color=colors)
    
    ax.set_yticks(range(len(words)))
    ax.set_yticklabels(words)
    ax.invert_yaxis()
    
    ax.set_xlabel('Frequency', fontsize=12)
    ax.set_title('Top 20 Word Frequencies', fontsize=14, fontweight='bold')
    
    for i, (bar, count) in enumerate(zip(bars, counts)):
        ax.text(bar.get_width() + max(counts) * 0.01, bar.get_y() + bar.get_height()/2,
                str(count), ha='left', va='center', fontsize=10)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"word_frequency_bar_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)
    
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    
    return filepath

def generate_pie_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str:
    Path(output_dir).mkdir(exist_ok=True)
    
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    
    if not sorted_items:
        return ""
    
    words, counts = zip(*sorted_items)
    
    total = sum(counts)
    other_count = sum(freq_dict.values()) - total
    
    if other_count > 0:
        words = list(words) + ['Others']
        counts = list(counts) + [other_count]
    
    colors = plt.cm.Set3(range(len(counts)))
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    wedges, texts, autotexts = ax.pie(counts, labels=words, colors=colors,
                                       autopct=lambda pct: f'{pct:.1f}%' if pct > 3 else '',
                                       startangle=90, pctdistance=0.85)
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(10)
    
    ax.set_title('Word Frequency Distribution', fontsize=14, fontweight='bold', pad=20)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"word_frequency_pie_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)
    
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    
    return filepath