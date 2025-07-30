
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
- **llm.py**: GEMINI API integration:
  - Uses gemini model with structured output parsing
  - Accepts transcript text and word frequency data
  - Returns parsed TranscriptAnalysis object

### Configuration Files
- **pyproject.toml**: Project metadata and dependencies:
  - Python 3.11+ requirement
  - Key dependencies: openai, pydantic, matplotlib, pyyaml, python-dotenv
  - Defines main script entry point

### Sample Data
- **transcript.txt & transcript2.txt**: Example transcript files for testing the analysis tool


*** The above is the detailed structure that is to be created in the src folder which is present in the root folder of my current directory.Follow all the steps and do not leave any files or folders.After completing go to the transcript which is below.


# Lesson 3: Crafting Perfect AI Coding Prompts with Information Dense Keywords (IDKs)

## Core Concept: Information Dense Keywords (IDKs)

### Essential IDK Categories

#### 1. Primary Action Keywords
- **CREATE** - Generate new files, functions, classes
- **UPDATE** - Modify existing code
- **DELETE** - Remove code elements
- **ADD** - Append to existing structures
- **REMOVE** - Take away specific elements
- **MOVE** - Relocate code between files/locations
- **REPLACE** - Substitute one element with another
- **SAVE** - Persist to file with specific format
- **MIRROR** - Copy pattern from existing code

#### 2. Code Element Keywords
- **VAR** - Variable declaration
- **FUNCTION/DEF** - Function definition (use language-specific: `def` for Python, `function` for JavaScript)
- **CLASS** - Class definition
- **TYPE** - Type definition
- **FILE** - File specification (always include extension: `.py`, `.js`, `.md`)
- **DEFAULT** - Default value specification

## Prompt Phrasing Pattern

### The Location → Action → Detail Pattern

**Structure**: `LOCATION : ACTION DETAIL`

**Examples**:
```
create output_format.py: def format_as_str(transcript: TranscriptAnalysis) -> str
update main.py: add CLI arg for file output_format default text
move threshold_logic after for word loop
```

### Key Components:

1. **LOCATION** - Where the change happens
   - File: `main.py`, `arg_parse.py`
   - Function: `def word_count_bar_chart`
   - Variable: `min_count_threshold`

2. **ACTION** - What to do
   - Primary keywords: CREATE, UPDATE, DELETE, etc.

3. **DETAIL** - Specific implementation details
   - Function signatures
   - Variable types
   - Behavioral specifications

## Practical Prompt Examples

### Example 1: Multi-File Output Format Feature
```
create output_format.py: 
  def format_as_str(transcript: TranscriptAnalysis) -> str,
  format_as_json,
  format_as_markdown

update main.py: 
  add CLI arg for file output_format default text,
  save output to file with proper extension
```

### Example 2: Bar Chart Feature
```
create chart.py: def word_count_bar_chart(word_count: dict, threshold: int): show horizontal bar chart sort descending

update main: replace word_count print with word_count_bar_chart

move threshold_logic after for word loop
```

### Example 3: Using MIRROR Keyword
```
update main.py, output_format.py, arg_parse.py: 
  add format_as_yaml 
  mirror format_as_json
```

## Best Practices

### 1. Start with Low-Level Prompts
**Good (Low-Level)**:
```
create output_format.py: def format_as_str(transcript: TranscriptAnalysis) -> str
```

**Avoid Initially (High-Level)**:
```
add json, markdown and text output formats
```

### 2. Use Proper File Extensions
- Always include: `.py`, `.js`, `.md`, `.yaml`
- This makes "output_format" become "output_format.py" (IDK)

### 3. Reference Existing Variables/Functions
- Use exact names from codebase
- Example: `word_count: dict` references existing variable

### 4. Leverage List Syntax
- Use commas to indicate multiple similar operations
- Pattern recognition helps LLMs understand intent

### 5. Be Explicit About Locations
- Specify "next to main.py" for file creation
- Use function names as locations when unique

## Common Patterns

### Creating Multiple Functions
```
create [filename].py:
  def function1(...) -> type,
  function2,
  function3
```

### Multi-File Updates
```
update file1.py, file2.py, file3.py:
  [coordinated change across files]
```

### Moving Code Between Files
```
move [element] from [source] to [destination]
```

### Adding CLI Arguments
```
update arg_parse.py: add CLI arg [name] default [value]
```

## Validation Workflow

1. Write prompt with IDKs
2. Execute with AI assistant
3. Validate output immediately
4. Fix any issues with targeted prompts
5. Always run code to verify

## Advanced Tips

- **Context Management**: Add relevant files (especially dependency files like `pyproject.toml`)
- **Pattern Recognition**: LLMs understand lists, so use comma separation
- **Error Recovery**: If something fails, write specific fix prompt
- **Progressive Enhancement**: Start detailed, remove keywords as you gain confidence

***follow all the above transcript step by step and if any errors analyse,take time and solve it.