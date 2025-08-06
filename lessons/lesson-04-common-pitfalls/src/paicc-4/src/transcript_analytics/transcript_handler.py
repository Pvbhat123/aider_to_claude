import os
from pathlib import Path
from typing import Dict, List, Optional
from .llm import analyze_with_sentiment
from .data_types import TranscriptAnalysisV2
from .constants import DEFAULT_THRESHOLD
from .chart import word_count_bar_chart, word_count_pie_chart, word_count_line_chart
from .output_format import format_as_json, format_as_markdown, format_as_yaml, format_as_text


class TranscriptHandler:
    def __init__(self, transcript_path: str, threshold: int = DEFAULT_THRESHOLD):
        self.transcript_path = transcript_path
        self.threshold = threshold
        self.analysis = None
        self.chart_paths = []
        
    def load_and_analyze(self) -> TranscriptAnalysisV2:
        with open(self.transcript_path, 'r', encoding='utf-8') as f:
            text = f.read()
        
        self.analysis = analyze_with_sentiment(text, self.threshold)
        return self.analysis
    
    def generate_charts(self, output_dir: str = "output") -> List[str]:
        if not self.analysis:
            raise ValueError("Analysis must be performed before generating charts")
        
        self.chart_paths = []
        
        bar_path = word_count_bar_chart(self.analysis.word_count, output_dir)
        if bar_path:
            self.chart_paths.append(bar_path)
        
        pie_path = word_count_pie_chart(self.analysis.word_count, output_dir)
        if pie_path:
            self.chart_paths.append(pie_path)
        
        line_path = word_count_line_chart(self.analysis.word_count, output_dir)
        if line_path:
            self.chart_paths.append(line_path)
        
        return self.chart_paths
    
    def save_analysis(self, output_format: str, output_file: Optional[str] = None) -> str:
        if not self.analysis:
            raise ValueError("Analysis must be performed before saving")
        
        if not output_file:
            base_name = Path(self.transcript_path).stem
            output_file = f"{base_name}_analysis.{output_format}"
        
        if output_format == "json":
            content = format_as_json(self.analysis)
        elif output_format == "yaml":
            content = format_as_yaml(self.analysis)
        elif output_format == "markdown":
            content = format_as_markdown(self.analysis, self.chart_paths)
        else:
            content = format_as_text(self.analysis)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return output_file
    
    def get_summary(self) -> Dict:
        if not self.analysis:
            return {"error": "No analysis performed yet"}
        
        return {
            "summary": self.analysis.summary,
            "sentiment": self.analysis.sentiment,
            "keywords": self.analysis.keywords,
            "total_words": self.analysis.total_words,
            "unique_words": self.analysis.unique_words
        }