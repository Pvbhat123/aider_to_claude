# Lesson 03: Perfect Prompt Engineering with Information Dense Keywords (IDKs)

## Original Concept Overview
This lesson focuses on crafting perfect AI coding prompts using Information Dense Keywords (IDKs) - words that carry maximum meaning and action. It demonstrates how specific keyword choices and structured prompt patterns dramatically improve AI coding assistant outputs, reducing iteration time and increasing accuracy.

## Core AI Coding Concepts
1. Information Dense Keywords (IDKs): High-value words that communicate clear actions and intent
2. Location → Action → Detail pattern: Structured prompt phrasing for consistent results
3. Low-level vs High-level prompts: Starting detailed and gradually abstracting
4. Context precision: Using file extensions, function signatures, and variable names as location identifiers
5. Pattern recognition: Leveraging LLM's ability to understand lists and repetitive structures

## AIDER Implementation Approach
- Uses `/add` command to manage context window with specific files
- Employs `/ask` for conversational queries about codebase
- Manual context management through adding/dropping files
- Relies on interactive refinement of prompts

## Claude Code Translation
### Concept Mapping
| AIDER Approach | Claude Code Approach | Notes |
|----------------|---------------------|-------|
| Manual `/add` context | Automatic context discovery | Claude can proactively find related files |
| `/ask` for queries | WebSearch/WebFetch for documentation | More comprehensive information gathering |
| Sequential prompt refinement | Parallel tool execution | Better performance with batched operations |
| Manual verification | Autonomous validation with Bash | Self-correcting behavior |

### Implementation Enhancements
- Added robust YAML format support alongside JSON/Markdown
- Enhanced chart visualization with matplotlib integration
- Implemented proper file extension handling for output formats
- Structured output using Pydantic models for type safety
- Modular architecture with clear separation of formatting logic

## Key IDK Categories

### Primary Action Keywords
- **CREATE**: Generate new files, functions, classes
- **UPDATE**: Modify existing code  
- **DELETE**: Remove code elements
- **ADD**: Append to existing structures
- **REMOVE**: Take away specific elements
- **MOVE**: Relocate code between files/locations
- **REPLACE**: Substitute one element with another
- **SAVE**: Persist to file with specific format
- **MIRROR**: Copy pattern from existing code

### Code Element Keywords
- **VAR**: Variable declaration
- **FUNCTION/DEF**: Function definition (language-specific)
- **CLASS**: Class definition
- **TYPE**: Type definition
- **FILE**: File specification (always with extension)
- **DEFAULT**: Default value specification

## The Location → Action → Detail Pattern

**Structure**: `LOCATION : ACTION DETAIL`

**Examples**:
```
create output_format.py: def format_as_str(transcript: TranscriptAnalysis) -> str
update main.py: add CLI arg for file output_format default text
move threshold_logic after for word loop
```

## Key Takeaways: Agentic AI Coding Principles

### 1. Precision Through Information Density
- AI agents perform best with information-rich keywords that eliminate ambiguity
- File extensions (.py, .js, .md) transform generic names into specific IDKs
- Function signatures serve as both location and implementation detail
- Variable names should match existing codebase for accurate targeting

### 2. Structured Communication Patterns
- Location → Action → Detail provides consistent framework for any prompt
- Comma-separated lists leverage LLM pattern recognition capabilities
- Colon notation creates clear hierarchical relationships
- Explicit references prevent hallucination and ensure accuracy

### 3. Progressive Prompt Abstraction
- Start with low-level, explicit prompts for reliability
- Gradually remove keywords as patterns become established
- Test abstraction levels to find optimal information density
- Maintain clarity over brevity when uncertainty exists

### 4. Context as a Force Multiplier
- Adding dependency files (pyproject.toml) enables feature inference
- File grouping through directory addition maximizes context efficiency
- Strategic context management reduces token usage while maintaining accuracy
- AI agents can infer implementation from well-structured context

### 5. Autonomous Validation and Recovery
- AI should immediately test generated code
- Prompt corrections should be specific and targeted
- Error recovery demonstrates adaptive problem-solving
- Validation loops ensure production-ready output

### 6. The MIRROR Pattern for Consistency
- Leverages existing code patterns for new implementations
- Reduces specification overhead through pattern replication
- Ensures consistency across similar functions
- Enables rapid feature extension with minimal prompting

### 7. Multi-File Orchestration
- Single prompts can coordinate changes across multiple files
- Atomic multi-file edits maintain codebase consistency
- Location specificity prevents cross-file conflicts
- Batch operations maximize efficiency and coherence

### 8. From Communication to Automation
- IDKs represent a structured language for human-AI collaboration
- Consistent patterns enable predictable, repeatable results
- Precision in prompting translates to autonomy in execution
- The goal: minimal human intervention with maximum output quality

## Advanced Agentic Patterns

### 1. Self-Directed Context Building
- AI agents should proactively gather necessary context
- Use Glob/Grep for discovering related files
- Build comprehensive understanding before implementation
- Minimize human-provided context through intelligent discovery

### 2. Iterative Refinement Loops
- Generate → Validate → Refine without human intervention
- Use tool combinations for comprehensive validation
- Self-correct based on execution results
- Maintain progress tracking through TodoWrite

### 3. Pattern Learning and Replication
- Identify coding patterns from existing codebase
- Apply discovered patterns to new implementations
- Maintain consistency without explicit instructions
- Build pattern library through code analysis

### 4. Intelligent Failure Recovery
- Detect and diagnose errors autonomously
- Generate targeted fixes based on error analysis
- Retry operations with adjusted parameters
- Document failure patterns for future avoidance

## Conclusion
The mastery of Information Dense Keywords and structured prompt patterns represents a fundamental shift in how we communicate with AI coding assistants. By treating prompts as a precise specification language rather than conversational requests, we enable AI agents to operate with increasing autonomy and accuracy. The progression from detailed, low-level prompts to abstracted, high-level commands mirrors the journey from supervised to autonomous AI coding, where the assistant becomes a true collaborative partner capable of independent decision-making within well-defined boundaries.