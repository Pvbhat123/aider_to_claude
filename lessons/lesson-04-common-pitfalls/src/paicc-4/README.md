# Transcript Analytics Tool

A Python tool for analyzing transcripts with word frequency analysis, visualizations, and AI-powered insights.

## Features

- Word frequency analysis with customizable threshold
- Multiple visualization types (bar chart, pie chart, line chart)
- AI-powered transcript analysis using OpenAI's GPT-4
- Multiple output formats (text, JSON, YAML, markdown)
- Configurable word blacklist for filtering common words

## Installation

```bash
# Install dependencies
pip install -e .

# Or using uv (recommended)
uv pip install -e .
```

## Usage

```bash
# From the project root directory
python -m src.transcript_analytics <transcript_file> [--threshold N] [--output-format FORMAT]

# Or after installation
cd src
python -m transcript_analytics <transcript_file> [--threshold N] [--output-format FORMAT]
```

### Arguments

- `transcript_file`: Path to the transcript file to analyze
- `--threshold`: Minimum word frequency to include (default: 5)
- `--output-format`: Output format - text, json, yaml, or markdown (default: text)

### Examples

```bash
# Basic usage (from project root)
python -m src.transcript_analytics transcript.txt

# With custom threshold
python -m src.transcript_analytics transcript.txt --threshold 10

# With JSON output
python -m src.transcript_analytics transcript.txt --output-format json
```

## Environment Setup

Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Common AI Coding Pitfalls

### Context Pitfalls
- **Missing Context**: Ensure all necessary files are in the AI's context window
- **Excessive Context**: Avoid overwhelming the model with too many files

### Prompt Pitfalls
- **Too High Level**: Vague prompts lead to unpredictable results
- **Too Low Level**: Overly detailed prompts waste time

### Model Pitfalls
- **Weak Model**: Using GPT-4o-mini for complex tasks leads to poor results
- **Model Overkill**: Using reasoning models for simple tasks is inefficient

## Best Practices

1. **Balance Context**: Include only files that need changes
2. **Clear Prompts**: Use Location + Action + Detail structure
3. **Right Model**: Match model power to task complexity
4. **Iterate**: Start simple, then refine based on results