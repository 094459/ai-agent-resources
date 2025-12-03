# SQL and Data Optimization Review Rules

## Overview
This document provides a systematic approach to reviewing SQL queries, database schemas, and data-related code against four key criteria: query design, index design, performance, and security.

## Review Process

### 1. Query Design Review

#### Evaluation Criteria
- **Readability & Maintainability**
  - Table aliases: 2-4 characters, meaningful (u for users, o for orders)
  - Column selection: Explicit columns only, no SELECT *
  - Indentation: 2-4 spaces, aligned JOIN/WHERE clauses
  - Line length: Max 120 characters per line
  
- **Correctness & Logic**
  - JOIN conditions: Always include ON clause, avoid comma joins
  - WHERE clauses: Use proper operators (= vs LIKE vs IN)
  - NULL handling: Explicit IS NULL/IS NOT NULL checks
  - Aggregates: GROUP BY includes all non-aggregate SELECT columns
  - Data types: Consistent comparison types (avoid implicit conversions)

- **Query Structure Efficiency**
  - CTEs for readability when query >3 levels deep
  - Window functions instead of self-joins for ranking
  - EXISTS instead of IN for subqueries with potential NULLs
  - UNION ALL instead of UNION when duplicates acceptable

#### Specific Issues to Flag
- **Critical**: Cartesian products (missing JOIN conditions)
- **High**: SELECT * in production queries
- **High**: Subqueries in SELECT clause that could be JOINs
- **Medium**: DISTINCT without clear business justification
- **Medium**: Functions in WHERE clause on indexed columns
- **Low**: Inconsistent alias naming patterns

### 2. Index Design Review

#### Evaluation Criteria
- **Index Coverage Analysis**
  - Primary keys: Clustered index exists
  - Foreign keys: Non-clustered indexes on all FK columns
  - WHERE clauses: Indexes on columns used in >10% of queries
  - JOIN columns: Indexes on both sides of JOIN conditions
  - ORDER BY: Covering indexes for frequent sorting operations

- **Index Efficiency Metrics**
  - Selectivity: >95% for unique, >80% for non-unique indexes
  - Composite order: Most selective column first, then query pattern order
  - Index size: <20% of table size for non-covering indexes
  - Usage stats: Drop indexes with <1% usage over 30 days
  - Fill factor: 80-90% for high-insert tables, 95-100% for read-only

- **Index Type Selection**
  - B-tree: Default for range queries and sorting
  - Hash: Equality lookups only (PostgreSQL, Oracle)
  - Bitmap: Low-cardinality columns with complex WHERE clauses
  - Partial: Filtered indexes when <30% of rows match condition
  - Covering: Include frequently accessed non-key columns

#### Specific Issues to Flag
- **Critical**: Missing indexes causing table scans >1000 rows
- **Critical**: Duplicate indexes (same column order and includes)
- **High**: Indexes with selectivity <50%
- **High**: Missing foreign key indexes
- **Medium**: Composite indexes with wrong column order
- **Medium**: Over-indexing (>7 indexes per table)
- **Low**: Unused indexes (0 seeks in 30 days)

### 3. Performance Review

#### Measurable Performance Criteria
- **Execution Time Thresholds**
  - OLTP queries: <100ms for 95th percentile
  - Reporting queries: <5 seconds for 95th percentile
  - Batch operations: <30 minutes for full completion
  - Real-time dashboards: <500ms response time

- **Resource Consumption Limits**
  - Logical reads: <1000 per query for OLTP
  - Physical reads: <10% of logical reads (good buffer hit ratio)
  - CPU time: <50ms for simple queries, <2s for complex
  - Memory grants: <100MB for OLTP, <1GB for analytics
  - Parallel operations: Only for queries >2 seconds

- **Execution Plan Red Flags**
  - Table scans on tables >10,000 rows
  - Index scans with >20% of table rows
  - Hash joins on large datasets (>100k rows)
  - Nested loop joins with outer table >1000 rows
  - Sort operations >100MB memory
  - Key lookups >10% of index seeks

#### Specific Performance Issues
- **Critical**: Queries >10 seconds execution time
- **Critical**: Blocking locks >5 seconds
- **Critical**: Deadlocks occurring >1 per hour
- **High**: Table scans on tables >100k rows
- **High**: Implicit conversions in WHERE/JOIN clauses
- **High**: Parameter sniffing causing plan reuse issues
- **Medium**: Missing statistics or outdated (>7 days old)
- **Medium**: Excessive memory grants (>500MB for OLTP)
- **Low**: Suboptimal join order in execution plans

### 4. Security Review

#### Security Compliance Checklist
- **SQL Injection Prevention (100% Required)**
  - Parameterized queries: All user inputs use bind variables
  - Dynamic SQL: Whitelist approach for table/column names
  - Input validation: Length limits, type checking, regex patterns
  - Stored procedures: No EXEC() with concatenated strings
  - ORM usage: Verify parameterized query generation

- **Access Control Implementation**
  - Database users: No shared accounts, unique per application/user
  - Permissions: Grant minimum required (SELECT vs INSERT/UPDATE/DELETE)
  - Role hierarchy: Max 3 levels deep, clear inheritance
  - Service accounts: Rotate passwords every 90 days
  - Connection limits: Max concurrent connections per user

- **Data Protection Standards**
  - PII encryption: AES-256 for SSN, credit cards, health data
  - Column masking: Hash/mask in non-prod (email → e***@***.com)
  - Audit logging: All DML operations on sensitive tables
  - Connection security: TLS 1.2+ required, certificate validation
  - Backup encryption: Encrypted at rest and in transit

#### Critical Security Issues
- **Critical**: String concatenation in WHERE clauses with user input
- **Critical**: Database users with sysadmin/DBA privileges
- **Critical**: Unencrypted PII/PHI data in production
- **Critical**: Missing audit trails on financial/sensitive tables
- **High**: Shared database accounts across applications
- **High**: Overprivileged service accounts (db_owner vs db_datareader)
- **High**: Plaintext passwords in connection strings
- **Medium**: Missing column-level encryption for sensitive data
- **Medium**: Insufficient logging of failed authentication attempts
- **Low**: Non-expiring database passwords

## Review Output Format

### What's Done Well
**Query Design Strengths:**
- [ ] Uses explicit JOIN syntax with proper ON conditions
- [ ] Avoids SELECT * in favor of specific column lists
- [ ] Implements proper NULL handling with IS NULL/IS NOT NULL
- [ ] Uses appropriate aggregate functions with correct GROUP BY
- [ ] Follows consistent naming conventions (snake_case/camelCase)

**Index Design Strengths:**
- [ ] All foreign keys have supporting indexes
- [ ] Composite indexes follow optimal column ordering
- [ ] Covering indexes reduce key lookups
- [ ] Index selectivity >80% for all non-unique indexes
- [ ] No duplicate or redundant indexes found

**Performance Strengths:**
- [ ] Query execution times <100ms for OLTP operations
- [ ] Efficient execution plans with index seeks vs scans
- [ ] Proper pagination using OFFSET/LIMIT or cursor-based
- [ ] Minimal logical reads (<1000 per query)
- [ ] No blocking locks >1 second duration

**Security Strengths:**
- [ ] 100% parameterized queries, no string concatenation
- [ ] Principle of least privilege implemented
- [ ] Sensitive data properly encrypted (AES-256)
- [ ] Comprehensive audit logging on sensitive tables
- [ ] TLS encryption for all database connections

### Priority Improvements Matrix

| Priority | Impact | Effort | Examples |
|----------|--------|--------|-----------|
| **P0 - Critical** | High | Any | SQL injection vulnerabilities, table scans >1M rows, unencrypted PII |
| **P1 - High** | High | Low-Med | Missing FK indexes, inefficient JOINs, overprivileged accounts |
| **P2 - Medium** | Med | Low-Med | Suboptimal index order, minor query refactoring, audit gaps |
| **P3 - Low** | Low | Low | Code formatting, documentation, unused indexes |

### Top 3 Recommendations

#### Recommendation 1: [Specific Issue Title]
- **Category**: Query Design/Index Design/Performance/Security
- **Priority**: P0/P1/P2/P3
- **Impact**: Quantified benefit (e.g., "Reduce query time from 5s to 200ms")
- **Effort**: Time estimate (e.g., "2 hours development + 1 hour testing")
- **Risk**: Deployment risk level (Low/Medium/High)
- **Current State**: Specific metrics showing the problem
- **Target State**: Specific metrics after fix
- **Implementation Steps**:
  1. Specific action with code example
  2. Testing approach and success criteria
  3. Deployment and rollback plan
- **Validation**: How to measure success

#### Recommendation 2: [Specific Issue Title]
- **Category**: Query Design/Index Design/Performance/Security
- **Priority**: P0/P1/P2/P3
- **Impact**: Quantified benefit
- **Effort**: Time estimate
- **Risk**: Deployment risk level
- **Current State**: Baseline metrics
- **Target State**: Expected improvement
- **Implementation Steps**:
  1. Detailed action items
  2. Testing requirements
  3. Deployment strategy
- **Validation**: Success measurement criteria

#### Recommendation 3: [Specific Issue Title]
- **Category**: Query Design/Index Design/Performance/Security
- **Priority**: P0/P1/P2/P3
- **Impact**: Quantified benefit
- **Effort**: Time estimate
- **Risk**: Deployment risk level
- **Current State**: Current performance/security posture
- **Target State**: Desired outcome
- **Implementation Steps**:
  1. Step-by-step implementation
  2. Quality assurance approach
  3. Monitoring and alerting setup
- **Validation**: Metrics to track post-implementation

## Dialect-Specific Optimization Guidelines

### SQL Server Specific
- **Indexing**: Use INCLUDE columns for covering indexes
- **Pagination**: OFFSET/FETCH instead of TOP with subqueries
- **Statistics**: UPDATE STATISTICS with FULLSCAN for critical tables
- **Partitioning**: Partition elimination with proper WHERE clauses
- **Memory**: Use OPTION (RECOMPILE) for parameter sniffing issues

### PostgreSQL Specific
- **Indexing**: Partial indexes with WHERE conditions
- **Analytics**: Use window functions over self-joins
- **Text Search**: GIN indexes for full-text search
- **JSON**: Use JSONB with GIN indexes for document queries
- **Vacuum**: Regular VACUUM ANALYZE for statistics updates

### MySQL Specific
- **Indexing**: Prefix indexes for VARCHAR columns >20 chars
- **Joins**: Use STRAIGHT_JOIN to force join order when needed
- **Partitioning**: RANGE/HASH partitioning for large tables
- **Storage**: InnoDB for transactions, MyISAM for read-only analytics
- **Query Cache**: Avoid for high-write workloads

### Oracle Specific
- **Hints**: Use /*+ INDEX */ hints sparingly, prefer statistics
- **Partitioning**: Range partitioning with partition pruning
- **Analytics**: Use FIRST_VALUE/LAST_VALUE window functions
- **PL/SQL**: Bulk operations with FORALL for DML
- **Optimizer**: Gather fresh statistics with DBMS_STATS

### Universal Patterns (All Dialects)
- **CTEs**: Prefer over subqueries for readability (3+ levels)
- **EXISTS vs IN**: Use EXISTS for correlated subqueries
- **UNION ALL**: Use instead of UNION when duplicates acceptable
- **Date Functions**: Use ISO format (YYYY-MM-DD) for portability
- **NULL Handling**: Explicit COALESCE() instead of ISNULL/NVL

## Detailed Review Checklist

### Pre-Review Setup (30 minutes)
- [ ] **Environment Analysis**
  - Database version and edition
  - Hardware specs (CPU, RAM, storage type)
  - Current workload patterns (OLTP/OLAP/Mixed)
  - Peak usage times and concurrent user count

- [ ] **Baseline Metrics Collection**
  - Top 10 slowest queries (>1 second)
  - Index usage statistics (seeks vs scans)
  - Wait statistics and blocking chains
  - Buffer hit ratios and page life expectancy
  - Security audit logs and failed login attempts

- [ ] **Documentation Review**
  - ERD and table relationships
  - Business rules and data constraints
  - SLA requirements and performance targets
  - Compliance requirements (GDPR, HIPAA, SOX)

### During Review (2-4 hours)
- [ ] **Query Analysis (45 minutes)**
  - Execution plan review for top 20 queries
  - JOIN efficiency and algorithm selection
  - WHERE clause selectivity analysis
  - Parameter sniffing and plan reuse issues

- [ ] **Index Assessment (45 minutes)**
  - Missing index recommendations from DMVs
  - Duplicate and unused index identification
  - Index fragmentation levels (>30% = rebuild)
  - Covering index opportunities

- [ ] **Performance Deep Dive (60 minutes)**
  - Resource bottleneck identification
  - Lock contention and deadlock analysis
  - Memory pressure and spill events
  - I/O subsystem performance

- [ ] **Security Audit (30 minutes)**
  - SQL injection vulnerability scan
  - Permission audit (users, roles, grants)
  - Encryption status for sensitive columns
  - Audit trail completeness verification

### Post-Review Actions (60 minutes)
- [ ] **Impact Quantification**
  - Performance improvement estimates (time/throughput)
  - Resource savings calculations (CPU/Memory/I/O)
  - Risk reduction assessment (security/compliance)
  - Cost-benefit analysis for each recommendation

- [ ] **Implementation Planning**
  - Development effort estimates (hours/days)
  - Testing requirements and rollback procedures
  - Deployment windows and change management
  - Success metrics and monitoring setup

- [ ] **Follow-up Schedule**
  - 1-week post-implementation review
  - 1-month performance trend analysis
  - Quarterly optimization review cycle
  - Annual security and compliance audit

## Success Metrics

### Performance Targets
- **Query Response Time**: 95th percentile <100ms (OLTP), <5s (Analytics)
- **Throughput**: >1000 TPS for OLTP workloads
- **Resource Utilization**: <70% CPU, <80% Memory during peak
- **Availability**: >99.9% uptime with <5s failover time

### Security Compliance
- **Zero** SQL injection vulnerabilities
- **100%** parameterized queries for user input
- **AES-256** encryption for all PII/PHI data
- **Complete** audit trails for sensitive data access

### Quality Indicators
- **Index Hit Ratio**: >95% seeks vs scans
- **Buffer Hit Ratio**: >99% for OLTP systems
- **Lock Duration**: <1 second average
- **Deadlock Rate**: <1 per hour during peak usage