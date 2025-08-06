# Transcript Analytics Application

A CLI application for analyzing transcripts with word frequency counting and AI-powered insights.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Set up environment variables:
   - `GEMINI_API_KEY`: Your Google Gemini API key

## Usage

```bash
uv run python -m spec_based_ai_coding.main analyze-transcript <path-to-transcript-file>
```

## Features

- Word frequency counting with common word filtering
- AI-powered transcript analysis using Google Gemini
- Rich terminal output
- Customizable minimum word count threshold