"""Output formatting functions for different formats."""

import json
import yaml
from typing import Any
from .data_types import TranscriptAnalysis, TranscriptAnalysisV2


def format_text(analysis: TranscriptAnalysis) -> str:
    """Format analysis results as plain text."""
    output = []
    output.append("TRANSCRIPT ANALYSIS RESULTS")
    output.append("=" * 50)
    output.append(f"\nTotal Words: {analysis.total_words}")
    output.append(f"Unique Words: {analysis.unique_words}")
    
    output.append("\nTop 10 Words:")
    output.append("-" * 30)
    for word, count in analysis.top_words[:10]:
        output.append(f"{word:20} {count:5}")
    
    if analysis.llm_summary:
        output.append("\nAI Summary:")
        output.append("-" * 30)
        output.append(analysis.llm_summary)
    
    if analysis.key_topics:
        output.append("\nKey Topics:")
        output.append("-" * 30)
        for topic in analysis.key_topics:
            output.append(f"• {topic}")
    
    return "\n".join(output)


def format_json(analysis: TranscriptAnalysis) -> str:
    """Format analysis results as JSON."""
    data = {
        "total_words": analysis.total_words,
        "unique_words": analysis.unique_words,
        "top_words": [{"word": word, "count": count} for word, count in analysis.top_words[:10]],
        "llm_summary": analysis.llm_summary,
        "key_topics": analysis.key_topics
    }
    return json.dumps(data, indent=2)


def format_yaml(analysis: TranscriptAnalysis) -> str:
    """Format analysis results as YAML."""
    data = {
        "transcript_analysis": {
            "statistics": {
                "total_words": analysis.total_words,
                "unique_words": analysis.unique_words
            },
            "top_words": [{"word": word, "count": count} for word, count in analysis.top_words[:10]],
            "ai_analysis": {
                "summary": analysis.llm_summary,
                "topics": analysis.key_topics
            }
        }
    }
    return yaml.dump(data, default_flow_style=False, sort_keys=False)


def format_markdown(analysis: TranscriptAnalysis) -> str:
    """Format analysis results as Markdown."""
    output = []
    output.append("# Transcript Analysis Results\n")
    
    output.append("## Statistics\n")
    output.append(f"- **Total Words**: {analysis.total_words}")
    output.append(f"- **Unique Words**: {analysis.unique_words}\n")
    
    output.append("## Top 10 Words\n")
    output.append("| Word | Count |")
    output.append("|------|-------|")
    for word, count in analysis.top_words[:10]:
        output.append(f"| {word} | {count} |")
    
    if analysis.llm_summary:
        output.append("\n## AI Summary\n")
        output.append(analysis.llm_summary)
    
    if analysis.key_topics:
        output.append("\n## Key Topics\n")
        for topic in analysis.key_topics:
            output.append(f"- {topic}")
    
    return "\n".join(output)


def format_output(analysis: TranscriptAnalysis, format_type: str) -> str:
    """Format analysis results based on requested format."""
    formatters = {
        "text": format_text,
        "json": format_json,
        "yaml": format_yaml,
        "markdown": format_markdown
    }
    
    formatter = formatters.get(format_type, format_text)
    return formatter(analysis)