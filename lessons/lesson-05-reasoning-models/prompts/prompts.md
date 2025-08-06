  paicc-5/
  ├── README.md                    # Project documentation with setup instructions
  ├── pyproject.toml              # Python project config (dependencies, build settings)
  ├── uv.lock                     # Dependency lock file for uv package manager
  ├── transcript.txt              # Sample transcript file
  ├── transcript2.txt             # Sample transcript file
  ├── transcript3.txt             # Sample transcript file
  ├── specs/                      # Specification documents directory
  │   ├── spec-template.md        # Template for writing specifications
  │   └── transcript-analytics-v0.md  # Analytics specification document
  └── src/                        # Source code directory
      └── spec_based_ai_coding/   # Main package directory
          ├── __init__.py         # Python package initializer
          ├── main.py            # Main entry point for the application
          └── py.typed           # Marker file for PEP 561 type checking

  Directory Descriptions:

  - Root Directory: Contains project configuration and sample transcript files for analysis
  - specs/: Holds specification documents used for AI-assisted coding workflows
  - src/spec_based_ai_coding/: Python package containing the main application logic for spec-based AI        
  coding

  **the above is the basic folder structure that is to be created in the src file present in D:\Agentic coding\ai-coding-course-claude\lessons\lesson-05-reasoning-models\src  before executing the tasks present in the transcript-analytics-vo.md.

  ** The next task is to execute the below prompts 
  # Transcript Analytics v0 Specification

## High-Level Objective

- Create a CLI transcript analytics application

## Mid-Level Objective

- Build a python MVP typer CLI application.
- Accept a path to a text file.
- Count the frequency of each word in a file, filter out common words, and limit by count threshold.
- Use an openai chat completion with structured output analyze the transcript and word counts.
- Rich print the frequency of each word to the terminal and the transcript analysis.

## Implementation Notes
- No need to import any external libraries see pyproject.toml for dependencies.
- Comment every function.
- For typer commands add usage examples starting with `uv run main <func name dash sep and params>`
- When code block is given in low-level tasks, use it without making changes (Task 4).
- Carefully review each low-level task for exact code changes.

## Context

### Beginning context
- `src/spec_based_ai_coding/main.py`
- `pyproject.toml` (readonly)

### Ending context
- `src/spec_based_ai_coding/main.py`
- `pyproject.toml`
- `src/spec_based_ai_coding/llm.py` (new file)
- `src/spec_based_ai_coding/word_counter.py` (new file)
- `src/spec_based_ai_coding/data_types.py` (new file)
- `src/spec_based_ai_coding/constants.py` (new file)

## Low-Level Tasks
> Ordered from start to finish

1. Create common word blacklist.
```aider
CREATE src/spec_based_ai_coding/constants.py: 
    CREATE COMMON_WORDS_BLACKLIST = ['the', 'and', ...add 50 more common words]
```

2. Create our data types.
```aider
CREATE src/spec_based_ai_coding/data_types.py:

    CREATE pydantic types:

        WordCounts(BaseModel): {count_to_word_map: Dict[str, int]},

        TranscriptAnalysis(BaseModel): {
            quick_summary: str
            bullet_point_highlights: List[str]
            sentiment_analysis: str
            keywords: List[str]
        }
```

3. Create our word counter & filter out & limit by count threshold.
```aider
CREATE src/spec_based_ai_coding/word_counter.py:
    CREATE word_counter(script: str, min_count_threshold: int = 10) -> WordCounts:
        Remove punctuation from script and make all words lowercase,
        Use the COMMON_WORDS_BLACKLIST to filter out common words,
        Only include words that are greater than the min_count_threshold.
        Sort descending by count.
```

4. CREATE src/spec_based_ai_coding/llm.py: Updated to use Gemini
```
from typing import List
from pydantic import BaseModel
import google.generativeai as genai
import os
from .data_types import TranscriptAnalysis

# Set up Gemini client using API key from environment variable
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

def analyze_transcript(transcript: str, word_count: dict) -> TranscriptAnalysis:
    prompt = (
        "You are a helpful assistant analyzing transcripts.\n\n"
        f"Transcript:\n{transcript}\n\n"
        f"Word Count: {word_count}\n\n"
        "Return a structured response for TranscriptAnalysis."
    )

    response = model.generate_content(prompt)

    try:
        # Try to parse the text response as JSON and load into TranscriptAnalysis
        import json
        parsed = json.loads(response.text)
        return TranscriptAnalysis(**parsed)
    except Exception as e:
        raise ValueError(f"Failed to parse Gemini response: {e}\nRaw response: {response.text}")
```

5. Update our main function to use new count and analysis functions.

```aider
UPDATE src/spec_based_ai_coding/main.py:
    CREATE a new typer cli application:
        CREATE @app.command() def analyze_transcript(path_to_script_text_file, min_count_threshold: int = 10):
            Read file, count words, run analysis, rich print results,
            print words like '<word>: ###' where ### is count 3
```


**after executing the above tasks then follow the transcript given below which are necessary to perform tasks.

# Lesson V: Principled AI Coding - Spec-Based Development

## Introduction

Welcome to Lesson V of principled AI coding. In this lesson, you'll learn how to consistently generate massive amounts of code with a single prompt.

In engineering, there are always bottlenecks and limitations. Before OpenAI's reasoning models and Anthropic's Claude 3.5, LLMs still had major limitations - they would hallucinate, cause issues, and couldn't solve problems consistently.

That is no longer the case. Now it's our abilities that are the bottleneck. The question is: what can we do to unlock the full potential of these incredible models?

Spec-based AI coding is a technique you can use to capture more of the potential of these models. In this lesson, you'll learn to use the spec prompt.

## What is a Spec?

A spec is a specification, which is also simply known as a plan. If you're a senior+ engineer, you're likely familiar with:
- Planning your work
- Creating architecture docs
- Figuring out what needs to be done before you do it

Planning your work is a massively important skill for AI coding. Why? Because powerful reasoning models can do more - the true limitation is in what we can ask them to do.

Writing a great plan and passing it to your reasoning model enables you to tap into its true capabilities.

## Key Principle

**The plan is the prompt. Plans = Prompting.**

Great planning is great prompting. In this lesson, we are going to stop firing ad-hoc high and low level prompts to accomplish one task at a time. Instead, we'll:
- Use powerful reasoning models like OpenAI's O1 model series
- Combine it with two-step prompting mode built into Aider
- Write comprehensive spec documents (plans) detailing exactly what we want done

## Three Big Ideas

1. **Reasoning Models**: Advanced models that can work through and iterate over your prompts, context, and code
2. **Spec Documents**: Detailed plans that specify exactly what changes you want
3. **Architect Mode**: Aider's two-model approach - one to draft changes, another to make edits

## How Architect Mode Works

With Architect Mode:
- You use two models: one to draft changes and a second to make edits given the draft
- This mode alone drastically boosts code generation accuracy
- When combined with reasoning models and a great plan, you get extraordinary results

## Mental Shift Required

This lesson requires a significant mental shift:
- From writing code by hand → writing code with prompts → planning everything in detail
- You're shifting from the "how" to the "what"
- You're becoming a commander of compute

The only bottleneck preventing 10,000+ line code generations across 5-10-20 files is:
- Your imagination
- Your skills

## Setting Up the Environment

### Initial Setup
```bash
# Clone the lesson 5 codebase
ls  # View previous codebases
cd lesson-5-codebase
code .  # Open in VS Code
```

### Dependencies
```bash
uv sync  # Install Python dependencies
# Set up both OPENAI_API_KEY and ANTHROPIC_API_KEY in .env file
uv run main  # Should output "Hello AI world"
```

### Running Aider in Architect Mode
```bash
aider --o1-preview --architect --editor-model claude-3-5-sonnet-20241022
```

This command:
- Uses O1-preview as the main model
- Enables architect mode
- Uses Claude 3.5 Sonnet as the editor model

## Understanding Spec Documents

A specification document contains:

### 1. High-Level Objective
```markdown
Create a CLI Transcript Analytics application
```

### 2. Mid-Level Objectives
- Build a Python MVP Typer CLI application
- Accept the path to a file
- Count the frequency of each word in the file
- Use OpenAI Chat API
- Rich print the frequency

### 3. Implementation Notes
Technical details, dependencies, and coding standards:
- Don't import external libraries not in pyproject.toml
- For Typer commands, include usage examples starting with `uv run main`

### 4. Context
Specify exactly what files are needed:
- **Beginning**: Files available at start
- **Ending**: Files that should exist after completion

### 5. Low-Level Tasks
Ordered list of specific prompts/tasks. Each item is both a high-level and low-level prompt.

Example structure:
```markdown
1. Create common words blacklist
   ```aider
   Create src/spec_based_ai_coding/constants.py
   Create COMMON_WORDS_BLACKLIST variable with 50+ common English words
   ```

2. Create data types
   ```aider
   Create src/spec_based_ai_coding/data_types.py
   Create Pydantic types:
   - WordCounts: dict[str, int]
   - TranscriptAnalysis with fields...
   ```
```

## Key Concepts

### Information-Dense Keywords
- Types, functions, variables, files
- Strong reference points with clear locations and meanings
- Enable communication across prompts

### Ordered Tasks
- Allow referencing work from previous steps
- Build upon each other
- Create a compound effect

### Type-Based AI Coding
- Data types, interfaces, and classes communicate information effectively
- No confusion about what things are or where they're located

## Workflow

1. **Write the Spec**
   - Think through all changes
   - Fill out context (beginning and end)
   - Work through low-level prompts top to bottom

2. **Execute with Reasoning Model**
   - Add required files to context
   - Copy entire spec and paste into Aider
   - Wait 20-60 seconds for reasoning model to process

3. **Review and Approve Changes**
   - Architect drafts changes
   - Editor model implements them
   - Review each change before approving

4. **Clean Up**
   - Expect to need minor fixes
   - Run a separate Aider instance for quick corrections
   - As you improve, spec accuracy increases: 80% → 85% → 90% → 100%

## Example: Creating Charts and Output Formats

### High-Level Objective
Add charting and output file functionality to the CLI transcript application

### Mid-Level Objectives
- Add bar, pie, and line chart capabilities in chart.py
- Add output file functionality in output_format.py
- Add chart and output_file CLI args to Typer

### Implementation Notes
- Use matplotlib for charting
- Output formats: .txt, .json, .markdown, .yaml
- Chart types: bar, pie, line

### Low-Level Tasks
1. Create output format functions
2. Create chart functions (bar, pie, line)
3. Update main to use new functions

## Best Practices

### Pattern Recognition
- Set up consistent patterns
- Use information-dense keywords
- Let the LLM pick up on your patterns

### Error Handling
- Expect to iterate
- Keep a clean-up Aider instance ready
- Focus on the mindset shift away from manual coding

### Scaling Impact
- Start with small specs (3-5 changes)
- Build up to larger specs (10-20+ changes)
- Each task should be a complete, well-formed prompt

## Key Takeaways

1. **Planning equals prompting** - Invest time upfront in detailed plans
2. **Use reasoning models** for complex, multi-file changes
3. **Architect mode** improves accuracy significantly
4. **Practice the mental shift** from coding to planning
5. **Expect iteration** but aim for increasing accuracy

## Next Steps

- Take a break to practice these concepts
- Write your own spec documents
- Test different model combinations
- Build the mental model for spec-based development

In Lessons 6 and 7, we'll scale up even further and add new dimensions to AI coding that eliminate entire classes of engineering work.

Remember: The plan is the prompt, and great planning is great prompting.


