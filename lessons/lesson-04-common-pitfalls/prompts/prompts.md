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

** the above is the folder structure that is to be created before anything.after creating all the folder structure as required go to the next task which is following the transcript of the video and performing the task.
*** create the above folder structure inside the src folder which is present in 
D:\Agentic coding\ai-coding-course-claude\lessons\lesson-04-common-pitfalls\src


# AI Coding Principles and Pitfalls Guide

## Core Principle: Balance, Then Boost
First do it, then do it right, then make it fast.

## The Big Three Bulls Eye
Always align: **Context + Model + Prompt**

## Common Pitfalls and Solutions

### 1. Context Pitfalls

#### Missing Context
- **Problem**: Files needed for changes are not in context window
- **Severity**: Low to Medium
- **Solution**: 
  - Always think from AI assistant's perspective
  - Ask: "Can I solve this with these files and this prompt?"
  - Add missing files before running prompt
  - Mention files explicitly in prompt for auto-suggestion

#### Excessive Context
- **Problem**: Too many files overwhelm the model
- **Severity**: Medium
- **Solution**:
  - Only add files that need changes
  - Use specific glob patterns, not wildcards
  - Avoid adding lock files, documentation unnecessarily
  - Use `/tokens` to check context distribution

### 2. Prompt Pitfalls

#### Too High Level
- **Problem**: Vague prompts like "enhance visualization"
- **Severity**: Mid to Heavy
- **Bad Example**: "enhance the visualization of our data top and bottom"
- **Solution**: Use Location + Action + Detail structure
- **Good Example**: "update chart.py word_count_bar_chart: make top quartile green, bottom red, rest blue"

#### Too Low Level
- **Problem**: Overly detailed prompts waste time
- **Severity**: Low
- **Solution**: Find the mid-level sweet spot using information-dense keywords (IDKs)

### 3. Model Pitfalls

#### Weak/Cheap Model
- **Problem**: Using Gemini for complex tasks
- **Severity**: High
- **Solution**: Use powerful base models (gemini-2.0-flash)
- **Note**: Don't optimize for cost at expense of time and accuracy

#### Model Overkill
- **Problem**: Using reasoning models for simple tasks
- **Severity**: Low to Mid
- **Solution**: Match model power to task complexity

## Information Dense Keywords (IDKs)

### Action Keywords
- `update` - modify existing code
- `add` - create new functionality
- `fix` - resolve issues

- `refactor` - restructure code
- `implement` - build new features

### Location Keywords
- File names: `main.py`, `chart.py`
- Function names: `word_count_bar_chart()`
- Class names
- Line numbers when specific

### Detail Patterns
- Use lists: "make top quartile green, bottom red, rest blue"
- Be specific about changes
- Include expected behavior

## Claude Code Best Practices

### Working with Context
- **Add specific files**: "Look at main.py and chart.py"
- **Read-only reference**: "Use README.md as reference but don't modify it"
- **Multiple files**: "Update these files: main.py, chart.py, constants.py"
- **Pattern matching**: "Check all Python files in src/ directory"

### Essential Claude Code Patterns
- **Check context**: "What files are you currently looking at?"
- **Add files**: "Also look at [filename]"
- **Remove from context**: "Stop looking at [filename]"
- **Run commands**: "Run pytest and show me the output"
- **Revert changes**: "Undo the last change to [filename]"
- **Clear context**: "Start fresh without any files"
- **File search**: "Find files containing [pattern]"
- **Code search**: "Search for [function/class] in the codebase"

### Configuration Through CLAUDE.md
Create a CLAUDE.md file in your project root with:
```markdown
# Project Guidelines

## Always run these after changes:
- pytest
- npm run lint
- npm run typecheck

## Project conventions:
- Use TypeScript for all new files
- Follow existing code style
- Add tests for new features
```

## Prompt Templates

### Basic Update
```
update [file] [function]: [specific changes]
```

### Multi-file Change
```
update across [file1], [file2]:
1. [change 1]
2. [change 2]
```

### Feature Implementation
```
implement [feature] in [location]:
- [requirement 1]
- [requirement 2]
ensure [constraint]
```

## Best Practices Summary

1. **Context Management**
   - Add only necessary files
   - Use read-only for documentation
   - Check with `/tokens` before complex prompts

2. **Prompt Writing**
   - Start with low-level prompts
   - Use IDKs for clarity
   - Include location, action, and details
   - Think: "Could I solve this with this info?"

3. **Model Selection**
   - Use powerful base models for coding
   - Save reasoning models for complex logic
   - Don't sacrifice quality for cost

4. **Workflow Optimization**
   - Set up .aider.yaml for consistency
   - Use auto-test for confidence
   - Master essential commands
   - Iterate from low to high-level prompts

## Red Flags to Avoid
- Prompts without file/function specifics
- Words like "enhance", "improve", "data" without context
- Adding entire directories with `**/*`
- Using weak models for production code
- Not checking context before running prompts

## Progressive Prompt Levels

1. **Low Level** (Most Detail)
   - Exact file, function, and line references
   - Step-by-step instructions
   - Explicit variable names

2. **Mid Level** (Sweet Spot)
   - File and function references
   - Clear action verbs
   - Concise change list

3. **High Level** (Least Detail)
   - General intent
   - Minimal specifics
   - Requires model inference

   ***follow the transcript step by step and resolve the errors and keep it optimized and error prooned and efficient.