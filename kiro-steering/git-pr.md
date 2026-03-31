# Create Pull Request

Push the current branch and open a pull request using the GitHub CLI.

## Process

1. Check branch name, recent commits, and changed files
2. Use your reasoning model: THINK HARD about what this change accomplishes, why it matters, and how to explain it clearly to reviewers
3. Write a PR title: type: short description
- feat | fix | refactor | docs | test | chore | perf
4. Write a concise body with:
- Summary: What and why (2-3 sentences)
- Changes: Key modifications (bullet list)
- Testing: How it was verified
5. Push the branch and run gh pr create

## Notes

- Use --draft if not ready for review
- Use --base <branch> if not targeting the default branch
- Provide the PR URL when complete
