---
inclusion: fileMatch
fileMatchPattern: "**/*.md,docs/**,**/README*,**/CHANGELOG*,**/ADR-*"
---

# Documentation & Diagrams

## Mandate
Every project must be documented well enough that another engineer can understand, deploy, and modify it without asking questions. Documentation is not an afterthought — it ships with the code.

## Required Documentation

### README.md (every project root)
Must contain:
1. **What**: One-paragraph description of what this project does and why
2. **Architecture**: ASCII diagram or link to architecture diagram
3. **Prerequisites**: Exact tools and versions needed (Node 20+, Python 3.12+, AWS CLI v2, CDK v2)
4. **Quick Start**: Numbered steps to go from clone to running locally
5. **Deploy**: Exact commands to deploy to AWS with expected outputs
6. **Environment Variables**: Table of all env vars with descriptions and example values
7. **API Reference**: Endpoints, methods, request/response examples
8. **Cleanup**: How to tear down all resources

### Architecture Diagrams
- Use diagram MCPs (Mermaid, PlantUML, or draw.io) to generate architecture diagrams
- Every project must have at least one architecture diagram showing:
  - Data flow between components
  - Network boundaries (VPC, subnets, public/private)
- Store diagrams in `docs/` directory as both source (`.mmd`, `.puml`) and rendered (`.png`)
- Update diagrams when architecture changes

### Inline Documentation
- Every module must have a top-level docstring explaining its purpose
- Complex business logic must have comments explaining WHY, not WHAT
- API endpoints must have OpenAPI/Swagger documentation
- CDK constructs must have comments explaining the infrastructure intent

### Decision Records
- For significant technical decisions, create a lightweight ADR in `docs/decisions/`
- Format: Context → Decision → Consequences
- Examples: "Why DynamoDB over RDS", "Why Lambda over ECS"

## When Creating or Modifying Code
1. Update the README if behavior changes
2. Update architecture diagrams if services/flow changes
3. Add/update inline documentation for new functions
4. Generate API docs if endpoints change
