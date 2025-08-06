import json
from typing import Optional
import yaml

from datatypes import TranscriptAnalysis

def format_as_json(analysis: TranscriptAnalysis) -> str:
    data = {
        "summary": analysis.summary,
        "bullet_points": analysis.bullet_points,
        "keywords": analysis.keywords,
        "sentiment": analysis.sentiment,
        "total_words": analysis.total_words,
        "unique_words": analysis.unique_words,
        "word_frequency": analysis.word_count
    }
    return json.dumps(data, indent=2)

def format_as_yaml(analysis: TranscriptAnalysis) -> str:
    data = {
        "summary": analysis.summary,
        "bullet_points": analysis.bullet_points,
        "keywords": analysis.keywords,
        "sentiment": analysis.sentiment,
        "total_words": analysis.total_words,
        "unique_words": analysis.unique_words,
        "word_frequency": analysis.word_count
    }
    return yaml.dump(data, default_flow_style=False, sort_keys=False)

def format_as_text(analysis: TranscriptAnalysis) -> str:
    output = []
    output.append("=" * 60)
    output.append("TRANSCRIPT ANALYSIS REPORT")
    output.append("=" * 60)
    output.append("")
    
    output.append("EXECUTIVE SUMMARY:")
    output.append(analysis.summary)
    output.append("")
    
    output.append("KEY POINTS:")
    for i, point in enumerate(analysis.bullet_points, 1):
        output.append(f"  {i}. {point}")
    output.append("")
    
    output.append("KEYWORDS:")
    output.append(", ".join(analysis.keywords))
    output.append("")
    
    output.append(f"SENTIMENT: {analysis.sentiment}")
    output.append("")
    
    output.append("STATISTICS:")
    output.append(f"  Total Words: {analysis.total_words}")
    output.append(f"  Unique Words: {analysis.unique_words}")
    output.append("")
    
    output.append("TOP WORD FREQUENCIES:")
    for word, count in list(analysis.word_count.items())[:20]:
        output.append(f"  {word}: {count}")
    
    return "\n".join(output)

def format_as_markdown(analysis: TranscriptAnalysis, bar_chart_path: Optional[str] = None, pie_chart_path: Optional[str] = None) -> str:
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
    output.append(", ".join(f"`{kw}`" for kw in analysis.keywords))
    output.append("")
    
    output.append("## Sentiment Analysis")
    output.append(f"**{analysis.sentiment.upper()}**")
    output.append("")
    
    output.append("## Statistics")
    output.append(f"- **Total Words:** {analysis.total_words}")
    output.append(f"- **Unique Words:** {analysis.unique_words}")
    output.append("")
    
    if bar_chart_path:
        output.append("## Word Frequency Bar Chart")
        output.append(f"![Word Frequency Bar Chart]({bar_chart_path})")
        output.append("")
    
    if pie_chart_path:
        output.append("## Word Frequency Pie Chart")
        output.append(f"![Word Frequency Pie Chart]({pie_chart_path})")
        output.append("")
    
    output.append("## Top Word Frequencies")
    output.append("")
    output.append("| Word | Frequency |")
    output.append("|------|-----------|")
    for word, count in list(analysis.word_count.items())[:20]:
        output.append(f"| {word} | {count} |")
    
    return "\n".join(output)

def format_as_html_with_slider(analysis: TranscriptAnalysis) -> str:
    word_freq_json = json.dumps(analysis.word_count)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Transcript Analysis Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #4ECDC4;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #555;
            margin-top: 30px;
        }}
        .summary {{
            background-color: #f8f9fa;
            padding: 15px;
            border-left: 4px solid #4ECDC4;
            margin: 20px 0;
        }}
        .sentiment {{
            display: inline-block;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            background-color: #e7f5ff;
            color: #0066cc;
        }}
        .keywords {{
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 15px 0;
        }}
        .keyword {{
            background-color: #95E77E;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 14px;
        }}
        .stats {{
            display: flex;
            gap: 30px;
            margin: 20px 0;
        }}
        .stat {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            flex: 1;
        }}
        .stat-value {{
            font-size: 24px;
            font-weight: bold;
            color: #4ECDC4;
        }}
        .slider-container {{
            margin: 30px 0;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 8px;
        }}
        .slider {{
            width: 100%;
            margin: 15px 0;
        }}
        #threshold-value {{
            font-weight: bold;
            color: #4ECDC4;
            font-size: 18px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #4ECDC4;
            color: white;
        }}
        tr:hover {{
            background-color: #f5f5f5;
        }}
        .hidden {{
            display: none;
        }}
        ul {{
            line-height: 1.8;
        }}
        li {{
            margin: 10px 0;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>=� Transcript Analysis Report</h1>
        
        <h2>Executive Summary</h2>
        <div class="summary">{analysis.summary}</div>
        
        <h2>Key Points</h2>
        <ul>
            {''.join(f"<li>{point}</li>" for point in analysis.bullet_points)}
        </ul>
        
        <h2>Keywords</h2>
        <div class="keywords">
            {''.join(f'<span class="keyword">{kw}</span>' for kw in analysis.keywords)}
        </div>
        
        <h2>Sentiment Analysis</h2>
        <div><span class="sentiment">{analysis.sentiment.upper()}</span></div>
        
        <h2>Statistics</h2>
        <div class="stats">
            <div class="stat">
                <div>Total Words</div>
                <div class="stat-value">{analysis.total_words:,}</div>
            </div>
            <div class="stat">
                <div>Unique Words</div>
                <div class="stat-value">{analysis.unique_words:,}</div>
            </div>
        </div>
        
        <h2>Word Frequency Analysis</h2>
        <div class="slider-container">
            <label for="threshold-slider">
                Minimum Word Count Threshold: <span id="threshold-value">1</span>
            </label>
            <input type="range" id="threshold-slider" class="slider" min="1" max="20" value="1">
            <div>Words shown: <span id="word-count">0</span></div>
        </div>
        
        <table id="frequency-table">
            <thead>
                <tr>
                    <th>Word</th>
                    <th>Frequency</th>
                </tr>
            </thead>
            <tbody id="table-body">
            </tbody>
        </table>
    </div>
    
    <script>
        const wordFrequency = {word_freq_json};
        const slider = document.getElementById('threshold-slider');
        const thresholdValue = document.getElementById('threshold-value');
        const wordCount = document.getElementById('word-count');
        const tableBody = document.getElementById('table-body');
        
        function updateTable() {{
            const threshold = parseInt(slider.value);
            thresholdValue.textContent = threshold;
            
            tableBody.innerHTML = '';
            let count = 0;
            
            for (const [word, freq] of Object.entries(wordFrequency)) {{
                if (freq >= threshold) {{
                    const row = tableBody.insertRow();
                    row.insertCell(0).textContent = word;
                    row.insertCell(1).textContent = freq;
                    count++;
                }}
            }}
            
            wordCount.textContent = count;
        }}
        
        slider.addEventListener('input', updateTable);
        updateTable();
    </script>
</body>
</html>"""
    
    return html