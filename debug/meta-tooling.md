# Meta-Tooling

**When debugging requires >3 iterations, STOP and build a tool.**

```
Problem → Solve in 1-2 attempts? → Yes → Solve directly
                ↓ No
        Repeating same investigation? → Yes → BUILD TOOL
                ↓ No
        Try 3 attempts → Still stuck? → BUILD TOOL
```

**Tool guidelines**: Single purpose, JSON output, clear errors, minimal dependencies

## Workflow Integration Check

**Tools/systems are incomplete without workflow integration.**

Before marking a tool/feature complete, ask:
- "How will this be discovered/triggered?"
- "Will this actually be used?"

If no clear answer → Add integration (hook, alias, documentation)

## Continuous Improvement Cycle

```
BUILD → DEPLOY → OBSERVE → LEARN → IMPROVE → REPEAT
```

**Apply to**: Complex systems, unclear requirements, measurable metrics

## Meta-Feature Completion

After completing architecture changes/refactoring:
1. Archive meta-spec to `.kiro/specs/.archive-YYYY-MM-DD/`
2. Update product steering - show feature as original
3. Update feature specs - use new patterns
4. Archive old code with README

## Observable Systems

**Design for visibility:**
1. Structured output (JSON to stdout)
2. Passive monitoring (observe without interfering)
3. State snapshots (enable recovery)
4. Log everything

## MCP Servers

- Verify before adding
- Avoid blocking HTTP calls (SSE)
- Config: `~/.kiro/settings/mcp.json`

## Prompt Macros

- Location: `~/.kiro/macros/`
- Auto-analyze risky prompts containing: "don't stop", "must complete", "delete", "remove all"

## Screenshot

```bash
screencapture -W /tmp/screenshot.png && open /tmp/screenshot.png
```
Then read with `fs_read` mode: "Image"
