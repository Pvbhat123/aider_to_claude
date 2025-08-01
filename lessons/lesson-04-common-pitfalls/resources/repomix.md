# paicc-4 Repository Structure

## Overview
Transcript analytics tool for processing text files, extracting word frequencies, generating visualizations, and providing AI-powered analysis using OpenAI's API.

## Directory Structure

```
paicc-4/
├── README.md                          # Setup guide with AI coding pitfall examples
├── pyproject.toml                     # Python >=3.11, deps: openai, pydantic, matplotlib
├── uv.lock                            # Exact dependency versions lock file
├── transcript.txt                     # Sample: OpenAI real-time API discussion
├── transcript2.txt                    # Sample: Prompt chaining techniques
├── transcript3.txt                    # Sample: AI engineering future
└── src/
    └── transcript_analytics/
        ├── __init__.py                # Package init with hello() function
        ├── arg_parse.py               # CLI args: file, threshold, output format
        ├── chart.py                   # Matplotlib visualizations: bar, pie, line
        ├── constants.py               # word_blacklist set for filtering
        ├── data_types.py              # Pydantic models: TranscriptAnalysis variants
        ├── llm.py                     # OpenAI GPT-4o-mini integration
        ├── main.py                    # Entry point, orchestrates analysis flow
        ├── output_format.py           # Formatters: text, JSON, YAML, markdown
        ├── transcript_analysis_v2.py  # Analysis with sentiment detection
        ├── transcript_handler.py      # Alternative v2 analysis implementation
        └── transcript_processing.py   # Analysis variant with logging
```

## File Descriptions

### Configuration Files

**pyproject.toml**
- Project configuration with dependencies
- Requires Python >=3.11
- Key dependencies: openai, pydantic, matplotlib, pyyaml, python-dotenv

**uv.lock**
- Dependency lock file for reproducible installations
- Contains exact versions of all dependencies

### Documentation

**README.md**
- Setup instructions and usage examples
- Documents common AI coding pitfalls
- Examples of context, prompt, and model issues

### Core Package (src/transcript_analytics/)

**__init__.py**
- Simple package initializer
- Contains hello() function returning greeting

**arg_parse.py**
- Command-line argument parsing setup
- Defines: transcript file path, word threshold, output format

**chart.py**
- Data visualization functions
- Functions: word_count_bar_chart(), word_count_pie_chart(), word_count_line_chart()
- Uses matplotlib for plotting

**constants.py**
- Contains word_blacklist set
- Common words to exclude from frequency analysis

**data_types.py**
- Pydantic data models
- Classes: TranscriptAnalysis, TranscriptAnalysisV2, TranscriptAnalysisVNext
- Defines structure for analysis results

**llm.py**
- OpenAI API integration
- Uses GPT-4o-mini model
- Analyzes transcripts for key topics and summaries

**main.py**
- Entry point and main processing logic
- Orchestrates: file reading, word counting, visualization, LLM analysis
- Handles output formatting based on CLI args

**output_format.py**
- Output formatting functions
- Formats: text, JSON, YAML, markdown
- Converts TranscriptAnalysis objects to various formats

**transcript_analysis_v2.py**
- Alternative analysis implementation
- Includes sentiment detection (positive/negative)
- Returns TranscriptAnalysis object

**transcript_handler.py**
- Another v2 analysis variant
- Different implementation approach
- Similar functionality to transcript_analysis_v2.py

**transcript_processing.py**
- Analysis variant with logging
- Adds console output during processing
- Useful for debugging and progress tracking

### Sample Data

**transcript.txt**
- Long transcript about OpenAI real-time API
- Discusses AI assistants and coding tools

**transcript2.txt**
- Transcript about prompt chaining and O1 models
- Covers prompt engineering techniques

**transcript3.txt**
- Transcript about future of AI engineering
- Discusses personal AI assistants and productivity

## Core Dependencies

- **openai**: LLM API integration
- **pydantic**: Data validation and modeling
- **matplotlib**: Chart generation
- **pyyaml**: YAML output support
- **python-dotenv**: Environment variable management

## Processing Flow

1. Parse command-line arguments
2. Read transcript file
3. Filter words using blacklist
4. Count word frequencies
5. Generate visualizations (bar/pie/line charts)
6. Run LLM analysis for insights
7. Format output (text/JSON/YAML/markdown)
8. Display results

## Usage Pattern

```bash
python -m transcript_analytics <transcript_file> [--threshold N] [--output-format FORMAT]
```

Where FORMAT can be: text, json, yaml, or markdown