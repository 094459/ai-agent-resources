---
inclusion: always
---

# Engineering Principles

## Core Philosophy
You are assisting a senior engineer who builds demos, prototypes, and production-ready applications on AWS. Every line of code you generate must be clean, purposeful, and maintainable.

## Common Pitfalls — Mistakes to Prevent
These are real, recurring mistakes. Check every output against this list. When you catch yourself making a mistake not on this list, suggest adding it.
- Don't over-engineer: a simple function doesn't need a Strategy pattern, a Factory, and an interface. Match complexity to the problem.
- Don't add error handling, logging, or validation that wasn't asked for. Keep diffs small and focused.
- Don't refactor surrounding code when fixing a bug. Fix the bug, nothing else.
- Don't create abstractions for a single use case. Wait until you have 3+ concrete cases before extracting.
- Don't use `Any` or `any` types. If the type is unclear, define it explicitly.
- Don't generate placeholder/TODO implementations. Either implement it fully or say you can't.
- When modifying existing code, match the existing style — don't reformat the whole file.
- Don't add dependencies without checking if the project already has an equivalent.

## SOLID Principles — Non-Negotiable
- **Single Responsibility**: One class/module = one reason to change. If a function does two things, split it.
- **Open/Closed**: Extend via composition and interfaces, not by modifying existing code. Use strategy patterns over if/else chains.
- **Liskov Substitution**: Subclasses must be drop-in replacements. Never override methods that break parent contracts.
- **Interface Segregation**: Small, focused interfaces. No god-interfaces. Clients should not depend on methods they don't use.
- **Dependency Inversion**: Depend on abstractions, not concretions. Inject dependencies — never instantiate collaborators inside business logic.

## Additional Principles
- **DRY**: Extract shared logic into utilities or shared modules. But don't over-abstract — duplication is better than the wrong abstraction.
- **KISS**: Prefer the simplest solution that works correctly. No premature optimization. No clever code.
- **YAGNI**: Don't build features that aren't explicitly requested. No speculative generalization.
- **Separation of Concerns**: Infrastructure, business logic, and presentation must live in separate layers. Never mix CDK constructs with application code.
- **Composition over Inheritance**: Prefer composing small, focused functions/classes over deep inheritance hierarchies.

## Code Clarity Rules
- Functions should be ≤ 25 lines. If longer, decompose.
- Maximum 3 parameters per function. Use objects/dataclasses for more.
- Name things for what they DO, not what they ARE. `calculate_risk_score()` not `processor()`.
- No magic numbers or strings. Use constants with descriptive names.
- Every public function must have a docstring/JSDoc explaining what it does, its parameters, and what it returns.

## Tool & MCP Usage
- Prefer MCP-sourced documentation over training data for AWS guidance — it's more current
- Use sequential thinking for multi-file changes, architectural decisions, or debugging with unclear root cause
- When MCP guidance conflicts with existing code patterns, flag it for review

## Anti-Patterns to Avoid
- God classes or modules that do everything
- Nested callbacks deeper than 2 levels
- Mutable global state
- Silent exception swallowing
- Copy-paste code across files
