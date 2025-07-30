# Transcript Analytics Tool

A Python tool for analyzing transcripts with word frequency analysis and LLM-powered insights using Google Gemini.

## Setup Instructions

### Prerequisites
- Python 3.11 or higher
- Google Gemini API key

### Installation

1. Clone this repository or download the source code

2. Install dependencies using pip:
```bash
pip install -e .
```

Or using uv package manager:
```bash
uv pip install -e .
```

3. Create a `.env` file in the project root and add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

### Usage

Run the transcript analytics tool with:
```bash
transcript-analytics path/to/transcript.txt
```

Optional arguments:
- `--min_count_threshold`: Minimum word count to include in analysis (default: 3)

Example:
```bash
transcript-analytics transcript.txt --min_count_threshold 5
```

### Features

- Word frequency analysis with configurable threshold
- Visual histogram of word frequencies
- LLM-powered analysis including:
  - Quick summary
  - Bullet point highlights
  - Sentiment analysis
  - Keyword extraction

### Sample Files

The project includes two sample transcript files for testing:
- `transcript.txt`
- `transcript2.txt`