
# PAICC-3 Folder Structure

## Transcript Analytics Tool - Information Dense Keywords (IDKs) Analysis

```
paicc-3/
│
├── README.md                      # Project documentation with setup instructions
├── pyproject.toml                 # Python project configuration with dependencies (openai, pydantic, matplotlib, pyyaml, python-dotenv)
├── transcript.txt                 # Sample transcript file for analysis
├── transcript2.txt                # Additional sample transcript file
├── uv.lock                        # Lock file for uv package manager dependencies
│
└── src/
    └── transcript_analytics/      # Main package directory for transcript analysis tool
        ├── __init__.py            # Python package initializer (empty)
        ├── arg_parse.py           # Command line argument parser - handles transcript file path and min_count_threshold
        ├── constants.py           # Contains word blacklist - common words to exclude from frequency analysis
        ├── data_types.py          # Pydantic models - defines TranscriptAnalysis schema with summary, highlights, sentiment, and keywords
        ├── llm.py                 # LLM integration - uses Gemini to analyze transcripts and generate structured insights
        └── main.py                # Entry point - orchestrates word frequency counting, filtering, and LLM-based transcript analysis
```

## Component Descriptions

### Core Application Files
- **main.py**: Central orchestrator that:
  - Loads environment variables for API keys
  - Reads transcript files
  - Performs word frequency analysis with blacklist filtering
  - Displays word frequency histogram
  - Calls LLM for comprehensive transcript analysis
  - Outputs structured analysis results

### Utility Modules
- **arg_parse.py**: Handles CLI arguments:
  - Required: transcript file path
  - Optional: --min_count_threshold (default: 3)

- **constants.py**: Configuration data:
  - Maintains blacklist of common stop words to exclude from analysis

### Data Models
- **data_types.py**: Defines structured output format:
  - quick_summary: Brief overview
  - bullet_point_highlights: Key points list
  - sentiment_analysis: Emotional tone assessment
  - keywords: Important terms extraction

### AI Integration
- **llm.py**: OpenAI API integration:
  - Uses GPT-4o model with structured output parsing
  - Accepts transcript text and word frequency data
  - Returns parsed TranscriptAnalysis object

### Configuration Files
- **pyproject.toml**: Project metadata and dependencies:
  - Python 3.11+ requirement
  - Key dependencies: openai, pydantic, matplotlib, pyyaml, python-dotenv
  - Defines main script entry point

### Sample Data
- **transcript.txt & transcript2.txt**: Example transcript files for testing the analysis tool

This tool analyzes transcripts by combining traditional word frequency analysis with AI-powered insights to extract Information Dense Keywords (IDKs) and provide comprehensive transcript understanding.