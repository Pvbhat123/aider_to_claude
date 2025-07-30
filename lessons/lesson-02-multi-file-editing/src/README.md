# Transcript Analytics Project

This project analyzes transcript files to extract word frequencies and provides AI-powered insights.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Copy environment file:
```bash
cp .env.sample .env
```

3. Add your Gemini API key to the .env file

## Usage

```bash
uv run python src/transcript_analytics/main.py
```