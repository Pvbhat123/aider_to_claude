import json
import yaml
from .data_types import TranscriptAnalysis


def format_as_str(transcript: TranscriptAnalysis) -> str:
    output = []
    output.append("TRANSCRIPT ANALYSIS REPORT")
    output.append("=" * 50)
    output.append("")
    
    output.append("QUICK SUMMARY:")
    output.append(transcript.quick_summary)
    output.append("")
    
    output.append("BULLET POINT HIGHLIGHTS:")
    for i, highlight in enumerate(transcript.bullet_point_highlights, 1):
        output.append(f"{i}. {highlight}")
    output.append("")
    
    output.append("SENTIMENT ANALYSIS:")
    output.append(transcript.sentiment_analysis)
    output.append("")
    
    output.append("KEYWORDS:")
    output.append(", ".join(transcript.keywords))
    output.append("=" * 50)
    
    return "\n".join(output)


def format_as_json(transcript: TranscriptAnalysis) -> str:
    return json.dumps(transcript.model_dump(), indent=2)


def format_as_markdown(transcript: TranscriptAnalysis) -> str:
    output = []
    output.append("# Transcript Analysis Report")
    output.append("")
    
    output.append("## Quick Summary")
    output.append(transcript.quick_summary)
    output.append("")
    
    output.append("## Bullet Point Highlights")
    for highlight in transcript.bullet_point_highlights:
        output.append(f"- {highlight}")
    output.append("")
    
    output.append("## Sentiment Analysis")
    output.append(transcript.sentiment_analysis)
    output.append("")
    
    output.append("## Keywords")
    output.append(", ".join([f"`{keyword}`" for keyword in transcript.keywords]))
    output.append("")
    
    return "\n".join(output)


def format_as_yaml(transcript: TranscriptAnalysis) -> str:
    return yaml.dump(transcript.model_dump(), default_flow_style=False, sort_keys=False)