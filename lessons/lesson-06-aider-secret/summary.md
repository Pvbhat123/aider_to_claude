Lesson 6 Summary: Agentic Coding with AI Developer Workflows (ADWs)

  Core Concept: ADWs enable programmatic control of AI coding assistants to automate entire
  classes of engineering problems. You write Python scripts that invoke AI assistants like Aider
  with specific contexts, prompts, and models.

  Key Agentic Aspects:

  1. Reusable AI Agents
  - Wrap AI coding assistants in scripts to solve specific problem patterns repeatedly
  - Pass parameters to make workflows dynamic (e.g., creating any chart type with a description)       
  - Example: Auto-increment version numbers, generate new output formats, create chart types

  2. Pattern-Based Automation
  - "As long as there's a pattern, you can use ADWs to solve the problem once and for all"
  - Automates migrations, API creation, templating, scaffolding, testing
  - Three occurrences make a pattern worth automating

  3. Multi-Agent Architecture
  - Combine architect and editor agents for complex tasks
  - Use spec prompts within ADWs for detailed, multi-step workflows
  - Chain multiple AI models (e.g., two Claude-3.5-Sonnet instances in architect mode)

  4. Context Management at Scale
  - Programmatically set editable vs read-only files
  - Pass project dependencies, data types, and specs as context
  - Use string templating to make prompts dynamic

  5. Engineering Role Transformation
  - Shift from "how" (implementation) to "what" (requirements)
  - Become "commanders of compute" directing AI assistants
  - Focus on architecture, planning, and review rather than low-level coding

  When to Use Each Approach:

  - Regular AI Sessions: Quick fixes, exploration, unknown solutions
  - Spec Prompts: Medium-large tasks with clear end-to-end plans (3-5+ steps)
  - ADWs: Recurring patterns, repeatable structures, automatable problem classes