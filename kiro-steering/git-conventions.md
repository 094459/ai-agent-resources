---
inclusion: fileMatch
fileMatchPattern: "**/.git/**,.gitignore,.gitattributes,**/PULL_REQUEST_TEMPLATE*,**/.github/**"
---

# Git Conventions

## Commit Messages — Conventional Commits
Format: `<type>(<scope>): <description>`

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `ci`, `perf`

- Subject line ≤ 72 characters, imperative mood ("add" not "added")
- Body explains WHY, not WHAT (the diff shows what)
- Reference ticket/issue IDs when applicable
- **Good**: `feat(api): add pagination to /users endpoint`
- **Bad**: `updated stuff` or `fix bug`

## Branching
- `main` — production-ready, protected
- `feat/<ticket>-<short-desc>` — feature branches
- `fix/<ticket>-<short-desc>` — bug fixes
- `chore/<desc>` — maintenance tasks
- Always branch from `main`, always merge via PR

## Pull Requests
- Keep PRs small and focused — one concern per PR
- Title follows commit convention: `feat(auth): add Cognito authorizer`
- Description: what changed, why, how to test, any risks
- PRs must include tests for new/changed functionality
- Never push directly to main

## Rules
- Commit early, commit often — small logical units
- Never commit secrets, credentials, or `.env` files
- Use `.gitignore` to exclude: `node_modules/`, `.venv/`, `cdk.out/`, `.env`, `dist/`, `__pycache__/`
- Rebase feature branches on main before merging to keep history clean
- Delete branches after merge
