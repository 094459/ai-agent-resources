Review code changes for quality, security, and maintainability.

1. **Identify Changes**
   - Run `git diff` to find changed files
   - Determine scope of review (specific files or entire PR)

2. **Review Categories**
   - **Security** - Hardcoded secrets, injection risks, XSS, CSRF
   - **Code Quality** - Function size, complexity, nesting depth
   - **Performance** - Algorithm efficiency, N+1 queries, caching
   - **Best Practices** - Naming, documentation, error handling
   - **Maintainability** - Duplication, coupling, testability

3. **Severity Rating**
   - **CRITICAL** - Security vulnerability (must fix before merge)
   - **HIGH** - Bug or major code smell (should fix before merge)
   - **MEDIUM** - Minor issue (fix when possible)
   - **LOW** - Style/suggestion (consider fixing)

4. **Specific Recommendations**
   - File:line locations for each issue
   - Concrete fix suggestions
   - Code examples where applicable



Scope: [git diff or specific files]

Review Checklist:
- Security vulnerabilities (OWASP Top 10)
- Code quality (complexity, duplication)
- Performance issues (N+1, inefficient algorithms)
- Best practices (naming, documentation, error handling)
- Maintainability (coupling, testability)

Output: Code review report with:
- Files reviewed count
- Issues by severity (CRITICAL, HIGH, MEDIUM, LOW)
- Specific file:line locations
- Fix recommendations
- Approval recommendation (APPROVE / REQUEST CHANGES / COMMENT)"
)

## Output Format

```
CODE REVIEW REPORT
==================

Files Reviewed: 8
Total Issues: 15

CRITICAL (0)
-----------
(none)

HIGH (3)
--------
1. src/api/auth.ts:42
   Issue: User input not sanitized before SQL query
   Risk: SQL injection vulnerability
   Fix: Use parameterized queries or ORM

2. src/components/UserProfile.tsx:89
   Issue: Password displayed in plain text in logs
   Risk: Credential exposure
   Fix: Remove password from log statements

3. src/utils/validation.ts:15
   Issue: Email regex allows invalid formats
   Risk: Accepts malformed emails
   Fix: Use proven email validation library

MEDIUM (7)
----------
...

LOW (5)
-------
...

RECOMMENDATION: REQUEST CHANGES

Critical security issues must be addressed before merge.
```

## Review Checklist

The code-reviewer agent checks:

### Security
- [ ] No hardcoded secrets (API keys, passwords, tokens)
- [ ] All user inputs sanitized
- [ ] SQL/NoSQL injection prevention
- [ ] XSS prevention (escaped outputs)
- [ ] CSRF protection on state-changing operations
- [ ] Authentication/authorization properly enforced

### Code Quality
- [ ] Functions < 50 lines (guideline)
- [ ] Cyclomatic complexity < 10
- [ ] No deeply nested code (> 4 levels)
- [ ] No duplicate logic (DRY principle)
- [ ] Clear, descriptive naming

### Performance
- [ ] No N+1 query patterns
- [ ] Appropriate caching where applicable
- [ ] Efficient algorithms (avoid O(n²) when O(n) possible)
- [ ] No unnecessary re-renders (React/Vue)

### Best Practices
- [ ] Error handling present and appropriate
- [ ] Logging at appropriate levels
- [ ] Documentation for public APIs
- [ ] Tests for critical paths
- [ ] No commented-out code

## Approval Criteria

**APPROVE** - No CRITICAL or HIGH issues, minor improvements only
**REQUEST CHANGES** - CRITICAL or HIGH issues present
**COMMENT** - Only LOW/MEDIUM issues, no blocking concerns
