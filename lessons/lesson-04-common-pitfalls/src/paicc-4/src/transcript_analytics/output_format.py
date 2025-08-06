import json
import yaml
from typing import List, Optional
from .data_types import TranscriptAnalysis, TranscriptAnalysisV2


def format_as_json(analysis: TranscriptAnalysis) -> str:
    return json.dumps(analysis.model_dump(), indent=2)


def format_as_yaml(analysis: TranscriptAnalysis) -> str:
    return yaml.dump(analysis.model_dump(), default_flow_style=False, sort_keys=False)


def format_as_text(analysis: TranscriptAnalysis) -> str:
    output = []
    output.append("=" * 60)
    output.append("TRANSCRIPT ANALYSIS REPORT")
    output.append("=" * 60)
    output.append("")
    
    output.append("EXECUTIVE SUMMARY:")
    output.append("-" * 40)
    output.append(analysis.summary)
    output.append("")
    
    output.append("KEY POINTS:")
    output.append("-" * 40)
    for i, point in enumerate(analysis.bullet_points, 1):
        output.append(f"{i}. {point}")
    output.append("")
    
    output.append("KEYWORDS:")
    output.append("-" * 40)
    output.append(", ".join(analysis.keywords))
    output.append("")
    
    if hasattr(analysis, 'sentiment'):
        output.append("SENTIMENT ANALYSIS:")
        output.append("-" * 40)
        output.append(f"Overall Sentiment: {analysis.sentiment}")
        output.append("")
    
    output.append("STATISTICS:")
    output.append("-" * 40)
    output.append(f"Total Words: {analysis.total_words:,}")
    output.append(f"Unique Words: {analysis.unique_words:,}")
    output.append("")
    
    output.append("TOP 20 WORD FREQUENCIES:")
    output.append("-" * 40)
    top_words = list(analysis.word_count.items())[:20]
    for word, count in top_words:
        output.append(f"{word:20} : {count:4}")
    
    return "\n".join(output)


def format_as_markdown(analysis: TranscriptAnalysis, chart_paths: Optional[List[str]] = None) -> str:
    output = []
    output.append("# Transcript Analysis Report")
    output.append("")
    
    output.append("## Executive Summary")
    output.append(analysis.summary)
    output.append("")
    
    output.append("## Key Points")
    for point in analysis.bullet_points:
        output.append(f"- {point}")
    output.append("")
    
    output.append("## Keywords")
    output.append(f"**{', '.join(analysis.keywords)}**")
    output.append("")
    
    if hasattr(analysis, 'sentiment'):
        output.append("## Sentiment Analysis")
        output.append(f"Overall Sentiment: **{analysis.sentiment}**")
        output.append("")
    
    output.append("## Statistics")
    output.append(f"- **Total Words:** {analysis.total_words:,}")
    output.append(f"- **Unique Words:** {analysis.unique_words:,}")
    output.append("")
    
    output.append("## Top Word Frequencies")
    output.append("")
    output.append("| Word | Frequency |")
    output.append("|------|-----------|")
    top_words = list(analysis.word_count.items())[:20]
    for word, count in top_words:
        output.append(f"| {word} | {count} |")
    output.append("")
    
    if chart_paths:
        output.append("## Visualizations")
        output.append("")
        for path in chart_paths:
            if path:
                filename = path.split('/')[-1].split('\\')[-1]
                output.append(f"### {filename.replace('_', ' ').replace('.png', '').title()}")
                output.append(f"![{filename}]({path})")
                output.append("")
    
    return "\n".join(output)