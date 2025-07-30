# paicc-2 Project Structure
```
paicc-2/
├── AI_DOCS/                          # AI documentation
│   │
│   └── openai_structured_output_example_code.md
├── src/                              # Source code 
│   └── transcript_analytics/         # Main package    
│       ├── __init__.py              # Package initialization   
│       └── main.py                  # Entry point
│
├── README.md                         # Project documentation
│
├── pyproject.toml                    # Python project configuration
│
├── transcript.txt                    # Sample transcript file
│
├── transcript2.txt                   # Another transcript file
│
└── uv.lock                          # UV package lock file
```
the above is the folder structure of the paicc2.
* first create all the necessary files required by refering to the above folder structure and put it in a src folder inside the current root folder.
* after creating all the necessary folders move to the next task which is refering to the transcript.


# Lesson 2: Multi-File Editing with AI - Transcript

## Setting Up the Project
Let's continue from our previous application. From lesson one, we'll open up the terminal.

```bash
# Clone the lesson 2 codebase
git clone [URL from course materials]

# Navigate to the directory
cd lesson-02-multi-file-editing

# Open in VS Code
code .
```

### Dependencies Setup

Open the README file for setup instructions:

```bash
# Install dependencies using UV (modern Python package manager)
uv sync

# Copy environment sample file
cp .env.sample .env

# Add your Gemini API key to the .env file
# GEMINI_API_KEY=your_api_key_here
```

**Important**: UV is a modern Python package manager we'll be using moving forward since it makes Python dependencies easier to work with.

**Note**: The example uses a Gemini API key. Make sure to get your own API key from Google AI Studio.

### Running the Application

```bash
# Run the main application
uv run main
```

The `uv run main` command is equivalent to running `python main.py` but uses the UV package manager.

### Our Enhancement Checklist

1. **Update the application to accept a CLI argument for the transcript file path**
   - **Value**: Allows us to run our transcript app on any file instead of hardcoded `transcript.txt`

2. **Add a blacklist to filter out common words**
   - **Value**: Filters out noisy, low-value words like "the", "a", "of", etc.

3. **Add Gemini API integration for transcript analysis**
   - **Value**: Generate quick summaries, bullet points, sentiment analysis, and keyword extraction using Google's Gemini model

## Task 1: Adding CLI Arguments

Let's boot up Claude Code and make our first change:

```bash
# Start Claude Code
claude
```

Claude Code will automatically detect the main.py file in your project and include it in the context.

First prompt:
```
Update main to accept a CLI arg transcript_file
```

Claude Code will:
- Import argparse
- Parse the command line argument
- Update the file reading to use the provided argument

### Validation

```bash
# Run without argument (should show error)
uv run main

# Run with transcript file
uv run main transcript.txt
uv run main transcript2.txt
```

## Task 2: Multi-File Refactoring

Now let's make our first multi-file edit by moving the parsing logic to a separate file:

```
Move CLI arg parsing into a file next to main.py called arg_parse.py
```

Key points about this prompt:
- **"Move"** keyword indicates we want to relocate code
- Specifies exact location ("next to main.py")
- Clear filename specification
- Claude Code will handle the multi-file editing automatically

### Adding More Arguments

```
Move min_count_threshold into parse_arguments function, default 3
```

This demonstrates:
- Moving variables between files
- Referencing specific function names
- Maintaining default values

### Fixing Import Issues

If you encounter import errors, Claude Code will automatically detect and fix them when you run:

```bash
uv run main
```

Claude Code monitors the terminal output and can automatically suggest fixes for any errors.

## Context Management in Claude Code

## Task 3: Adding Word Blacklist

Create a constants file with common words to filter:

```
Create constants.py next to main, add word_blacklist var based off transcript.txt with words like "to", "the", etc, then filter out words in main
```

This prompt demonstrates:
- Creating new files
- Adding variables with specific content
- Implementing filtering logic across files

## Task 4: Data Cleaning

Strip punctuation from words:

```
Update word.lower() to strip punctuation: comma, period, question mark, exclamation
```

## Task 5: Gemini Integration

### Creating Type Definitions

```
Create data_types.py next to main, use pydantic, add TranscriptAnalysis(BaseModel) {quick_summary: str, bullet_point_highlights: list[str], sentiment_analysis: str}
```

### Adding LLM Functionality

Using Google's Gemini API for structured outputs. Here's an example to provide to Claude Code:

```python
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("Analyze this transcript...")
```

Then prompt:
```
Create llm.py next to main, create def analyze_transcript(transcript) -> TranscriptAnalysis, use Gemini API with the example code provided
```

### Integrating the Analysis

```
Add analyze_transcript to main, run and print after keywords
```

### Enhancing with Word Counts

```
Update TranscriptAnalysis: add keywords: list[str]
Update analyze_transcript: pass in and use word_count
Update main.py: print keywords
```

### The Mental Model Shift

Think of yourself as:
- **Code Reviewer**: Validate and approve generated code
- **Code Curator**: Select what to keep and what to modify
- **Code Delegator**: Assign tasks to Claude Code


follow all the above transcript step by step and make the changes.
think deeply and take your time if there are any errors analyze and solve it yourself.