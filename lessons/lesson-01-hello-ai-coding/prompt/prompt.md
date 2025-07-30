# PAICC-1 Repository Structure

```
paicc-1/
├── .gitignore                  # Git ignore rules
├── README.md                   # Project setup guide
├── main.py                     # Main Python script
└── transcript.txt              # OpenAI API video transcript
The above is the repository structure of the project that is to be done initially.After creating the folder structure in the current directory inside src that is to be created by you.

# TRANSCRIPT OF THE VIDEO THAT YOU SHOULD BE FOLLOWING AND PERFORMING THE TASK ACCORDINGLY.
# AI Coding Lesson 1: Setup and Introduction to AI-Assisted Development with Claude Code

## Course Information
- **Course**: Principled AI Coding
- **Lesson**: 1 - Getting Started with AI Coding
- **Key Principle**: KISS (Keep It Simple, Stupid)
- **Objective**: Set up AI tooling and learn fundamental AI coding patterns

## Prerequisites Installation
Before starting, ensure you have installed:
1. UV (Python package manager)
2. Git
3. Python
4. pip
5. VS Code (or preferred code editor)
6. Claude Code CLI

## Initial Setup Tasks

### 1. Verify Prerequisites
Run these commands to verify installations:
```bash
uv --version
git --version
python --version
pip --version
```

### 2. Create Working Directory
```bash
mkdir lesson1
cd lesson1
```

### 3. Install Claude Code (AI Coding Assistant)
Follow the installation instructions from Claude Code documentation:
- Download Claude Code from the official website
- Install the CLI tool
- Verify installation with: `claude --version`

### 4. Configure API Keys
Set up your Anthropic API key (do not share this with anyone):
```bash
# For Unix/Mac
export ANTHROPIC_API_KEY="your-api-key-here"

# For Windows
set ANTHROPIC_API_KEY=your-api-key-here
```

## Project Structure
Create the following structure in your current directory:
```
src/
└── paicc-1/
    ├── .gitignore
    ├── README.md
    ├── main.py
    └── transcript.txt
```

## Basic AI Coding with Claude Code

### Starting Claude Code
Simply type your instructions directly in the Claude Code interface. Claude will:
- Automatically understand context from your current directory
- Create, read, update files as needed
- Execute commands when appropriate

### Essential Claude Code Features
- **Multi-file awareness**: Claude can see and work with multiple files simultaneously
- **Automatic execution**: Claude can run commands and show outputs
- **Context persistence**: Claude maintains conversation context throughout the session
- **Natural language**: Just describe what you want in plain English

## Exercise 1: Basic AI Coding Tasks

### Task 1: Create Project Structure
**Instruction**: "Create a src directory with a paicc-1 folder inside containing .gitignore, README.md, main.py, and transcript.txt files"

### Task 2: Hello World
**Instruction**: "In main.py, write code to print 'Hello AI Coding World'"
- Claude will create/modify the file
- Ask Claude to run it: "Run the main.py file"

### Task 3: Print Multiple Times
**Instruction**: "Update main.py to print 'Hello AI Coding World' 10 times"
- Review the changes
- Ask to run: "Run the updated code"

### Task 4: Use Variables
**Instruction**: "Refactor the code to store 'Hello AI Coding World' in a variable, then use it in the print statements"

### Task 5: Create Function
**Instruction**: "Move the printing logic into a function that takes the message as a parameter"

### Task 6: Revert Changes (if needed)
**Instruction**: "Revert the last change" or "Go back to the previous version"

## Exercise 2: Word Frequency Counter Project

### Project Goal
Build a word frequency counter that analyzes a transcript file.

### Implementation Steps

1. **Prepare transcript file**
   **Instruction**: "Create a transcript.txt file with sample text about AI and coding"

2. **Read transcript file**
   **Instruction**: "In main.py, read the content from transcript.txt and store it in a variable"

3. **Count word frequencies**
   **Instruction**: "Add code to count the frequency of each word using a dictionary"

4. **Display frequencies**
   **Instruction**: "Display the word frequencies by printing hashtags (#) for each count"

5. **Sort results**
   **Instruction**: "Sort the word frequencies in descending order before displaying"

6. **Run the complete program**
   **Instruction**: "Run the word frequency counter"

### Enhancement Instructions

To improve the word frequency counter:

**Instruction**: "Modify the code to only show words that appear more than 3 times, and display the count number alongside each word before the hashtags"

This demonstrates Claude's ability to:
- Make multiple related changes
- Implement conditional logic
- Format output appropriately

## Key Concepts

### Claude Code Architecture
1. **Context**: Claude automatically understands your project structure and files
2. **Intelligence**: Claude uses advanced AI to understand your intent
3. **Execution**: Claude can create, modify files and run commands directly

### Best Practices with Claude Code
- Be clear and specific in your instructions
- Describe the desired outcome, not just the steps
- Review generated code before confirming changes
- Use natural language - Claude understands context
- Break complex tasks into smaller, clear instructions

### Claude Code Advantages
- No need to manually add files to context
- Automatic understanding of project structure
- Can handle complex, multi-file operations
- Natural conversation flow
- Integrated file operations and command execution

### Important Notes
- Claude Code enhances your development workflow
- Always review code before accepting changes
- Be specific about requirements and constraints
- Claude maintains context throughout the conversation

## Advanced Claude Code Features

### Multi-file Operations
**Example**: "Create a utils.py file with helper functions and import them in main.py"

### Refactoring
**Example**: "Refactor the word frequency counter to use object-oriented programming"

### Error Handling
**Example**: "Add proper error handling for file not found scenarios"

### Testing
**Example**: "Create unit tests for the word frequency counter functions"

## Tips for Effective Claude Code Usage

1. **Be Descriptive**: Instead of "fix the bug", say "the word count is including punctuation, modify to count only alphabetic words"

2. **Provide Context**: "Following Python best practices, refactor the code to be more modular"

3. **Iterative Development**: Start simple, then add complexity incrementally

4. **Leverage Claude's Understanding**: Claude can infer common patterns and best practices

## Next Steps
- Experiment with more complex multi-file projects
- Try refactoring existing codebases
- Explore Claude's ability to explain code
- Practice with different programming languages

## Remember
- The KISS principle applies to your instructions too
- Claude Code is a conversation - be natural
- Focus on what you want to achieve, not how
- Claude can handle complex tasks while keeping things simple for you

follow the above transcript and to those changes in the src.
do the tasks in the order if any error occured solve it ,take your time and give me the result what i expect from the transcript.