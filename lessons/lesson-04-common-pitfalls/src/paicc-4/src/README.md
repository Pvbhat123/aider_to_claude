# Transcript Analytics CLI

A powerful CLI application that analyzes transcript files using AI-powered insights. The tool extracts structured insights including themes, bullet points, keywords, summaries, and sentiment analysis, outputting results in multiple formats (markdown, JSON, YAML, text) with professional visualizations.

## Features

- **AI-Powered Analysis**: Uses Google Gemini-1.5-flash model for intelligent transcript analysis
- **Multiple Output Formats**: Supports text, JSON, YAML, and Markdown outputs
- **Professional Visualizations**: Generates bar charts, pie charts, and line charts saved as PNG files
- **Word Frequency Analysis**: Filters common words and applies customizable thresholds
- **Sentiment Detection**: Analyzes overall sentiment of transcripts
- **Batch Processing**: Process multiple transcripts at once

## Installation

1. Clone the repository
2. Install dependencies using uv or pip:

```bash
# Using uv (recommended)
uv pip install -e .

# Or using pip
pip install -e .
```

3. Set up your Gemini API key:

Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```bash
python -m transcript_analytics transcript.txt
```

### With Options

```bash
python -m transcript_analytics transcript.txt --output-format markdown --threshold 5
```

### Command Line Arguments

- `transcript_file` (required): Path to the transcript file to analyze
- `--threshold`: Minimum word count threshold (default: 3)
- `--output-format`: Output format - text, json, yaml, or markdown (default: text)
- `--output-file`: Custom output filename (auto-generated if not specified)

### Examples

```bash
# Basic word frequency analysis
python -m transcript_analytics transcript.txt

# Generate markdown report with charts
python -m transcript_analytics transcript.txt --output-format markdown

# Custom threshold and JSON output
python -m transcript_analytics transcript.txt --threshold 5 --output-format json

# Specify custom output file
python -m transcript_analytics transcript.txt --output-format yaml --output-file my_analysis.yaml
```

## Output Files

The application automatically saves outputs:
- `analysis.txt` - Text format analysis
- `analysis.json` - JSON format analysis
- `analysis.md` - Markdown format with embedded charts
- `analysis.yaml` - YAML format analysis
- `output/` directory - Contains PNG chart files

## Project Structure

```
paicc-4/
├── README.md
├── pyproject.toml
├── transcript.txt           # Sample transcripts
├── transcript2.txt
├── transcript3.txt
└── src/
    └── transcript_analytics/
        ├── __init__.py
        ├── __main__.py
        ├── main.py          # CLI entry point
        ├── arg_parse.py     # Argument parsing
        ├── constants.py     # Configuration constants
        ├── data_types.py    # Pydantic data models
        ├── llm.py          # Gemini API integration
        ├── chart.py        # Visualization generation
        ├── output_format.py # Output formatters
        ├── transcript_analysis_v2.py  # Enhanced analysis
        ├── transcript_handler.py      # OOP analysis handler
        └── transcript_processing.py   # Logging variant
```

## API Usage

You can also use the package programmatically:

```python
from transcript_analytics import analyze_transcript, TranscriptHandler

# Simple analysis
analysis = analyze_transcript(text, threshold=3)

# Using the handler class
handler = TranscriptHandler("transcript.txt", threshold=5)
analysis = handler.load_and_analyze()
handler.generate_charts()
handler.save_analysis("markdown", "report.md")
```

## Requirements

- Python >= 3.11
- google-generativeai
- pydantic
- matplotlib
- pyyaml
- python-dotenv

## License

MIT