# CLI Transcript Analyzer - Hierarchical Development Specification

# ROLE: Senior Python Developer

## 🎯 HIGH-LEVEL TASK

**Primary Goal**: Build a CLI application that ingests transcript files, uses an AI model (Gemini-1.5-flash) to extract structured insights (e.g., themes, bullet points, keywords, summaries, sentiment analysis), and outputs results in .md, .json, .yaml, .txt formats. All generated visualizations (e.g., word frequency charts) should be saved as .png files. All output formats are automatically saved to files.

## 🎯 MID-LEVEL TASK

### 0. **Basic Repo Build**
Follow the project structure in the context and build a basic repo through which you are working further. Ask user to confirm basic repo build is fine. If yes, continue with low level tasks.

### 1. **Text Processing Engine**
Transform raw transcript text into structured word frequency data with AI-powered insights.

### 2. **AI Analysis Integration** 
Leverage Gemini gemini-1.5-flash model to generate executive summaries, sentiment analysis, and key highlights from transcripts.

### 3. **Visualization Generation**
Create professional charts (horizontal bar chart with color coding, pie chart, line chart) saved as PNG files in an output directory.

### 4. **Multi-Format Output System**
Support text, JSON, markdown, and YAML output formats with consistent structure. All formats automatically save to files: analysis.txt, analysis.json, analysis.md, analysis.yaml.

### 5. **CLI Interface**
User-friendly command-line interface with proper argument parsing and error handling. Example: "python -m transcript_analytics transcript.txt --output-format markdown"

## 🎯 LOW-LEVEL TASK

✅ [Step 1] main.py: CLI Entry - Display Word Count
Goal: Implement initial CLI entry point to display word frequency of a transcript.

Command: python -m transcript_analytics transcript.txt

Output: Print {word: count} dictionary to terminal.

✅ [Step 2] arg_parse.py: Argument Parser
Goal: Create a parse_arguments() function using argparse.

Required: transcript_file (positional)

Optional: 
- --threshold (int, default = 3)
- --output-format (choices: json, yaml, markdown, text, default: text)
- --output-file (str, optional - but auto-generated for markdown/json)

Returns: Namespace object used in main.py

✅ [Step 3] constants.py: Configuration Constants
Goal: Define all reusable constants.

word_blacklist set for filtering common words

SUPPORTED_FORMATS: ["json", "yaml", "markdown", "text"]

DEFAULT_THRESHOLD = 3

Common words to exclude from frequency analysis

✅ [Step 4] data_types.py: Data Model
Goal: Create TranscriptAnalysis models using pydantic.BaseModel.

Classes:
- TranscriptAnalysis: Base model
- TranscriptAnalysisV2: Extended with sentiment
- TranscriptAnalysisVNext: Future extensions

Fields:
- summary: str
- bullet_points: List[str]  
- keywords: List[str]
- sentiment: str (for V2)
- word_count: Dict[str, int]
- total_words: int
- unique_words: int

✅ [Step 5] llm.py: Gemini API Integration
Goal: Create analyzer to process transcript text.

Method: analyze_transcript(text: str, threshold: int = 3) -> TranscriptAnalysis

Responsibilities:
- Perform word frequency count (respecting blacklist and threshold)
- Call Gemini Gemini-flash-1.5 API
- Parse response: summary, bullet_points, keywords, sentiment
- Return populated TranscriptAnalysis object

✅ [Step 6] chart.py: Visualization Module
Goal: Generate word frequency bar, pie, and line charts using matplotlib.

Functions:
- word_count_bar_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str
- word_count_pie_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str
- word_count_line_chart(freq_dict: Dict[str, int], output_dir: str = "output") -> str

Features:
- Sort and color-code bars by frequency tiers
- Save .png files in output folder
- Return file paths
- Create output directory if it doesn't exist

✅ [Step 7] output_format.py: Formatter
Goal: Support multi-format output (text, json, yaml, markdown).

Functions:
- format_as_json(analysis: TranscriptAnalysis) -> str
- format_as_markdown(analysis: TranscriptAnalysis, chart_paths: Optional[List[str]] = None) -> str
- format_as_yaml(analysis: TranscriptAnalysis) -> str
- format_as_text(analysis: TranscriptAnalysis) -> str

Features:
- Include sentiment analysis in all formats
- Embed chart image paths in markdown output
- Format word frequency tables appropriately for each format

✅ [Step 8] transcript_analysis_v2.py: Enhanced Analysis
Goal: Alternative implementation with sentiment detection.

Method: analyze_with_sentiment(text: str) -> TranscriptAnalysisV2

Features:
- Includes sentiment detection (positive/negative)
- Returns TranscriptAnalysisV2 object
- Enhanced analysis capabilities

✅ [Step 9] transcript_handler.py & transcript_processing.py: Alternative Implementations
Goal: Provide alternative analysis approaches.

transcript_handler.py:
- Another v2 analysis variant
- Different implementation approach

transcript_processing.py:
- Analysis variant with logging
- Console output during processing
- Useful for debugging

## 📋 CONTEXT

### **Repo Structure**
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

### **Important Implementation Notes**

## Testing Part ##
1. All output formats are automatically saved to files:
   - `--output-format text` → `analysis.txt`
   - `--output-format json` → `analysis.json`
   - `--output-format markdown` → `analysis.md`
   - `--output-format yaml` → `analysis.yaml`
2. Custom output filenames can be specified with `--output-file`
3. PNG charts are always generated and saved in the project directory
4. The pyproject.toml must include proper dependencies for uv to work properly

### **Core Dependencies**
- **openai**: LLM API integration (GPT-4o-mini)
- **pydantic**: Data validation and modeling
- **matplotlib**: Chart generation
- **pyyaml**: YAML output support
- **python-dotenv**: Environment variable management

### **Processing Flow**
1. Parse command-line arguments
2. Read transcript file
3. Filter words using blacklist
4. Count word frequencies
5. Generate visualizations (bar/pie/line charts)
6. Run LLM analysis for insights
7. Format output (text/JSON/YAML/markdown)
8. Save results to files
9. Display results

### **Usage Pattern**
```bash
python -m transcript_analytics <transcript_file> [--threshold N] [--output-format FORMAT]
```

Where FORMAT can be: text, json, yaml, or markdown

### **Development Guidelines**
- Create the folder structure inside: `D:\Agentic coding\ai-coding-course-claude\lessons\lesson-04-common-pitfalls\src`
- Follow the transcript step by step
- Resolve errors proactively
- Keep implementation optimized and efficient
- Ensure error handling is robust

## AI Coding Principles and Pitfalls Guide

### Core Principle: Balance, Then Boost
First do it, then do it right, then make it fast.

### The Big Three Bulls Eye
Always align: **Context + Model + Prompt**

### Common Pitfalls and Solutions

#### 1. Context Pitfalls

**Missing Context**
- **Problem**: Files needed for changes are not in context window
- **Severity**: Low to Medium
- **Solution**: 
  - Always think from AI assistant's perspective
  - Ask: "Can I solve this with these files and this prompt?"
  - Add missing files before running prompt
  - Mention files explicitly in prompt for auto-suggestion

**Excessive Context**
- **Problem**: Too many files overwhelm the model
- **Severity**: Medium
- **Solution**:
  - Only add files that need changes
  - Use specific glob patterns, not wildcards
  - Avoid adding lock files, documentation unnecessarily
  - Use `/tokens` to check context distribution

#### 2. Prompt Pitfalls

**Too High Level**
- **Problem**: Vague prompts like "enhance visualization"
- **Severity**: Mid to Heavy
- **Bad Example**: "enhance the visualization of our data top and bottom"
- **Solution**: Use Location + Action + Detail structure
- **Good Example**: "update chart.py word_count_bar_chart: make top quartile green, bottom red, rest blue"

**Too Low Level**
- **Problem**: Overly detailed prompts waste time
- **Severity**: Low
- **Solution**: Find the mid-level sweet spot using information-dense keywords (IDKs)

#### 3. Model Pitfalls

**Weak/Cheap Model**
- **Problem**: Using weak models for complex tasks
- **Severity**: High
- **Solution**: Use powerful base models (GPT-4o-mini for this project)
- **Note**: Don't optimize for cost at expense of time and accuracy

**Model Overkill**
- **Problem**: Using reasoning models for simple tasks
- **Severity**: Low to Mid
- **Solution**: Match model power to task complexity

### Information Dense Keywords (IDKs)

**Action Keywords**
- `update` - modify existing code
- `add` - create new functionality
- `fix` - resolve issues
- `refactor` - restructure code
- `implement` - build new features

**Location Keywords**
- File names: `main.py`, `chart.py`
- Function names: `word_count_bar_chart()`
- Class names
- Line numbers when specific

**Detail Patterns**
- Use lists: "make top quartile green, bottom red, rest blue"
- Be specific about changes
- Include expected behavior

### Claude Code Best Practices

**Working with Context**
- **Add specific files**: "Look at main.py and chart.py"
- **Read-only reference**: "Use README.md as reference but don't modify it"
- **Multiple files**: "Update these files: main.py, chart.py, constants.py"
- **Pattern matching**: "Check all Python files in src/ directory"

**Essential Claude Code Patterns**
- **Check context**: "What files are you currently looking at?"
- **Add files**: "Also look at [filename]"
- **Remove from context**: "Stop looking at [filename]"
- **Run commands**: "Run pytest and show me the output"
- **Revert changes**: "Undo the last change to [filename]"
- **Clear context**: "Start fresh without any files"
- **File search**: "Find files containing [pattern]"
- **Code search**: "Search for [function/class] in the codebase"

**Configuration Through CLAUDE.md**
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

### Prompt Templates

**Basic Update**
```
update [file] [function]: [specific changes]
```

**Multi-file Change**
```
update across [file1], [file2]:
1. [change 1]
2. [change 2]
```

**Feature Implementation**
```
implement [feature] in [location]:
- [requirement 1]
- [requirement 2]
ensure [constraint]
```

### Best Practices Summary

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
   - Set up configuration for consistency
   - Use auto-test for confidence
   - Master essential commands
   - Iterate from low to high-level prompts

### Red Flags to Avoid
- Prompts without file/function specifics
- Words like "enhance", "improve", "data" without context
- Adding entire directories with `**/*`
- Using weak models for production code
- Not checking context before running prompts

### Progressive Prompt Levels

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