---
inclusion: fileMatch
fileMatchPattern: "infra/**,**/cdk.json,**/cdk*.ts,scripts/deploy*,scripts/destroy*,**/Dockerfile,docker-compose*,buildspec.*"
---

# Deployment Conventions

## Philosophy
Demos and prototypes deploy fast, but never sloppy. Every deployment must be reproducible from a clean checkout. No snowflake environments.

## Environment Strategy

| Environment | Purpose | Lifecycle |
|---|---|---|
| Local | Development + unit tests | Developer machine |
| Dev | Integration testing, shared | Always running |
| Demo | Stakeholder presentations | Deployed on-demand, torn down after |

## Deployment Method

- All infrastructure via **AWS CDK** (TypeScript) — no ClickOps, no raw CloudFormation
- Frontend: `next build` → `next export` → S3 sync → CloudFront invalidation
- Backend: CDK deploys Lambda functions, API Gateway, Neptune, and supporting resources
- Use `cdk diff` before every `cdk deploy` to review changes

## Project Structure

    infra/
    ├── bin/
    │   └── app.ts              # CDK app entry point
    ├── lib/
    │   ├── stateful-stack.ts   # Neptune, DynamoDB, S3 — resources with data
    │   └── stateless-stack.ts  # Lambda, API GW, CloudFront — replaceable
    ├── cdk.json
    └── package.json

## Deployment Scripts

All deployment commands go in `scripts/` — never paste long commands into the terminal.

    scripts/
    ├── deploy.sh               # Full CDK deploy
    ├── deploy-frontend.sh      # S3 sync + CloudFront invalidation
    ├── destroy.sh              # Full teardown
    └── diff.sh                 # CDK diff before deploy

## Deployment Rules

- Always use `--profile` and `--region` flags (see aws-isengard-credentials.md)
- Because any code you produce should be sharable - dont hard code profile name, make them passable params
- Tag all resources: `Project`, `Environment`, `Owner`
- Stateful resources use `RemovalPolicy.RETAIN` in production, `DESTROY` in demo
- Run `cdk diff` before every deploy — review changes before applying
- Frontend deploys are independent of backend — S3 sync only, no full CDK deploy needed
- Always invalidate CloudFront after frontend deploy (`/*` path)

## Cleanup

Every project must have a `scripts/destroy.sh` that tears down all resources cleanly. Empty S3 buckets before stack deletion (CDK `autoDeleteObjects: true` handles this for demo stacks).
