# Commit

Create a well-crafted git commit for the current changes.

## Process

1. Run `git status` and `git diff --staged` (and `git diff` if nothing staged)
2. Analyze the changes deeply:
   - What files changed and why?
   - What's the single unifying purpose?
   - What would a future developer need to understand?
3. THINK HARD: Write a commit message that future you will thank you for
4. Stage relevant files if needed
5. Commit with the crafted message
6. Push to current branch

## Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Subject Line (required)
- `feat` | `fix` | `refactor` | `docs` | `test` | `chore` | `perf`
- Imperative mood: "add" not "added" or "adds"
- No period at end
- Max 50 characters
- Complete the sentence: "This commit will..."

### Body (required for non-trivial changes)
- Wrap at 72 characters
- Explain WHAT and WHY, not HOW (the code shows how)
- Use blank line to separate from subject
- Use bullet points for multiple points

### Footer (optional)
- Reference issues: `Closes #123` or `Refs #456`
- Breaking changes: `BREAKING CHANGE: <description>`

## Examples

**Simple:**
```
docs: add CLAUDE.md with workflow guidance
```

**With body:**
```
feat: add three-step workflow commands

Introduce plan/build/pr commands that structure development into
discrete phases. This separation ensures:

- Plans are reviewed before execution
- Builds follow explicit specifications
- PRs have consistent, thorough descriptions

The workflow reduces context-switching and improves code review quality.
```

## Output

Confirm the commit hash and push status.
