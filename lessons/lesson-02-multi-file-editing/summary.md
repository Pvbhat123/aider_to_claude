# Lesson 02: Multi-File Editing

## Original Concept Overview
This lesson teaches how to handle multi-file Python projects with AI coding assistants, demonstrating how to refactor code across multiple files, replace API dependencies, and maintain clean project structure.

## Core AI Coding Concepts
1. Multi-file refactoring: Breaking down monolithic code into modular components
2. API migration: Replacing one service (OpenAI) with another (Google Gemini)
3. Feature enhancement: Adding command-line arguments and data filtering
4. Project structure: Organizing code into logical modules with clear responsibilities
5. Type safety: Using data classes for structured responses

## AIDER Implementation Approach
- AIDER would typically handle multi-file edits through its `/add` command to track multiple files
- Uses git integration for tracking changes across files
- Relies on conversation context to maintain coherence across file edits

## Claude Code Translation
### Concept Mapping
| AIDER Approach | Claude Code Approach | Notes |
|----------------|---------------------|-------|
| `/add` multiple files | Automatic file discovery with Glob/Read | Claude proactively finds related files |
| Manual file tracking | TodoWrite for task management | Better organization of multi-step tasks |
| Git-based change tracking | Direct file manipulation with Edit/Write | More immediate feedback |
| Context window management | Efficient tool use batching | Better performance with parallel operations |

### Implementation Changes
- Enhanced error handling for Gemini API responses with JSON parsing fallback
- More robust punctuation stripping and word filtering
- Structured data types using dataclasses for type safety
- Modular architecture with clear separation of concerns

## Code Structure Changes
- Original structure: Single-file script with all logic in one place
- New structure: Multi-module package with:
  - `main.py`: Entry point and orchestration
  - `llm.py`: LLM integration and prompt engineering
  - `constants.py`: Configuration and blacklists
  - `data_types.py`: Type definitions
  - `arg_parse.py`: CLI argument handling
- Rationale: Better maintainability, testability, and code reuse

## Gemini 2.5 Integration Points
- Replaced OpenAI API calls with Google Gemini API
- Added robust JSON response parsing with regex fallbacks
- Implemented structured prompts for consistent responses
- Added sentiment analysis and keyword extraction features

## Key Takeaways: Agentic AI Coding Principles

### 1. Proactive File Discovery and Context Building
- AI agents should autonomously discover related files using tools like Glob and Grep
- Build comprehensive understanding of codebase structure before making changes
- Batch file operations for efficiency (parallel Read/Edit operations)

### 2. Task Decomposition and Management
- Complex refactoring requires systematic task tracking (TodoWrite tool)
- Break multi-file operations into atomic, verifiable steps
- Maintain clear progress indicators for user visibility

### 3. Autonomous Decision Making with Guardrails
- AI should infer project structure and conventions from existing code
- Make architectural decisions based on discovered patterns
- Apply consistent coding standards across all modified files

### 4. Tool Orchestration for Complex Operations
- Combine multiple tools strategically (Search → Read → Edit → Verify)
- Use specialized tools for their strengths (Grep for content, Glob for structure)
- Minimize context usage through efficient tool selection

### 5. Verification and Self-Correction
- Autonomous validation of changes (running tests, type checking)
- Proactive error detection and resolution
- Maintain code integrity throughout multi-file transformations