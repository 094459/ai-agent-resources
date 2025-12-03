# Overview
This script helps developers quickly understand a codebase by performing a comprehensive analysis across multiple dimensions, with special focus on design principles and patterns. It systematically examines architecture, entry points, data models, dependencies, design patterns, SOLID principles, and more, compiling the results into a well-structured markdown document.

## Design Principle Analysis Constraints:
- You MUST analyze and identify specific design principles used in the code
- You MUST evaluate SOLID principles implementation (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)
- You MUST identify design patterns (Creational, Structural, Behavioral)
- You MUST assess clean code principles and best practices
- You MUST evaluate architectural patterns and their implementation quality

## Diagram Generation Constraints:
- For ALL diagrams created during analysis, you MUST use Mermaid diagram syntax exclusively
- You MUST include all Mermaid diagrams directly in the markdown document using proper code blocks

### You MUST use appropriate Mermaid diagram types based on content:
- Architecture diagrams: Use flowchart or graph syntax
- Dependency relationships: Use flowchart or graph syntax
- Component relationships: Use flowchart or C4Context syntax
- You MUST NOT use ASCII art, PlantUML, or any other diagram formats
- You MUST ensure all diagrams are clear, properly labeled, and support the analysis content


# Steps

## 1. Build Code Index with tools
- You are operating in an environment where ast-grep is installed. For any code search that requires understanding of syntax or code structure, you should default to using ast-grep --lang [language] -p '<pattern>'. Adjust the --lang flag as needed for the specific programming language. Avoid using text-only search tools unless a plain-text search is explicitly requested. Below are example commands for common tasks.
- You can use tree command for file browsing in a directory You MUST not translate the .git directory when analyzing source files to translate You SHOULD not need to examine the .git direcotry when analyzing the translation directory

## 2. Initialize Analysis Document
Create the analysis document with a table of contents and initial structure.

### Constraints:
- You MUST create the output file with proper markdown formatting
- You MUST include a table of contents with links to all analysis sections
- You MUST include a timestamp of when the analysis was performed
- You MUST include the path to the codebase being analyzed
- You SHOULD use clear section headers that correspond to each analysis step

## 3. High-Level Architecture Analysis
Analyze the codebase and provide a high-level architectural overview.

### Constraints:
- You MUST examine the directory structure, package organization, and code comments to identify main components
- You MUST analyze import statements, function calls, and dependency injection to determine component interactions
- You MUST only identify design patterns with clear implementation evidence
- You MUST determine the overall architectural style based on project structure and service definitions
- You MUST identify system boundaries and external interfaces from API definitions, client libraries, or interface declarations
- You MUST document the technology stack and frameworks used based on import statements and configuration files
- You MUST look for deployment architecture indicators in Dockerfiles and deployment scripts
- You MUST list key configuration files and their purposes
- You MUST identify communication protocols between components
- You MUST determine if components are stateful or stateless based on state management code
- You MUST identify synchronous vs. asynchronous processing patterns
- You MAY create a simple architecture diagram using Mermaid syntax if component relationships are clear
- If creating diagrams, you MUST use Mermaid diagram syntax and include the diagram directly in the markdown document
- You MUST use appropriate Mermaid diagram types (flowchart, graph, or C4Context) based on the architectural content
- You MUST NOT speculate about architectural elements that cannot be confidently determined from the code
- You MUST append the analysis results to the output file with proper formatting

## 4. Design Principles and Patterns Analysis
Analyze the codebase for design principles, patterns, and architectural best practices.

### Constraints:
You MUST analyze SOLID principles implementation:
- Single Responsibility Principle (SRP): Check if classes/functions have single, well-defined purposes
- Open/Closed Principle (OCP): Look for extension points, interfaces, and plugin architectures
- Liskov Substitution Principle (LSP): Examine inheritance hierarchies and polymorphism usage
- Interface Segregation Principle (ISP): Analyze interface design and client-specific interfaces
- Dependency Inversion Principle (DIP): Check for dependency injection and abstraction usage

You MUST identify Design Patterns with specific examples:
- Creational Patterns: Factory, Abstract Factory, Builder, Singleton, Prototype
- Structural Patterns: Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy
- Behavioral Patterns: Observer, Strategy, Command, State, Template Method, Chain of Responsibility, etc.

You MUST analyze Clean Code principles:
- Meaningful naming conventions
- Function and class size appropriateness
- Code readability and expressiveness
- Comment quality and necessity
- Error handling approaches

You MUST evaluate Architectural Patterns:
- MVC (Model-View-Controller)
- MVP (Model-View-Presenter)
- MVVM (Model-View-ViewModel)
- Layered Architecture
- Hexagonal Architecture (Ports and Adapters)
- Microservices patterns
- Event-driven architecture

You MUST assess Code Quality Principles:
- DRY (Don't Repeat Yourself)
- KISS (Keep It Simple, Stupid)
- YAGNI (You Aren't Gonna Need It)
- Separation of Concerns
- Loose Coupling and High Cohesion

You MUST create Mermaid diagrams for identified patterns:
- Use classDiagram for design pattern structures
- Use flowchart for architectural pattern flows
- Include specific class/method names from the actual code

You MUST provide specific code examples for each identified principle/pattern:
- File paths and line numbers
- Code snippets demonstrating the principle/pattern
- Explanation of how the principle/pattern is implemented

You MUST evaluate the quality of implementation:
- Rate adherence to each principle (Strong/Moderate/Weak/Not Present)
- Identify areas where principles could be better applied
- Note any anti-patterns or principle violations
- You MUST append the analysis results to the output file with proper formatting

## 5. Entry Points and Control Flow Analysis
Identify all entry points to the application and explain the control flow.

### Constraints:

- You MUST only include entry points that are explicitly defined in the code
- You MUST specify the exact file path and line number for each entry point
- You MUST describe the control flow based on actual function calls and code execution paths
- You MUST identify the main function or application startup sequence
- You MUST list all API endpoints or public interfaces found
You MUST identify event handlers or listeners
- You MUST document background jobs or scheduled tasks
- You MUST trace control flow through the system for key operations
- You MUST clearly state when control flow cannot be fully determined and why
- You MUST append the analysis results to the output file with proper formatting

## 6. Data Models and Schema Analysis
Analyze the data models in the codebase.

### Constraints:

- You MUST identify key entities and their relationships from class/type definitions
- You MUST document database schema if explicitly defined in migration files or ORM mappings
- You MUST identify data validation mechanisms from validation code or annotations
- You MUST document data transformation patterns from transformer classes or functions
- You MUST trace data flow based on function parameters and return values
- You MUST clearly indicate when schema information is incomplete
- You MUST suggest specific places to look for missing schema information
- You MUST append the analysis results to the output file with proper formatting

## 7. Dependencies and External Integrations Analysis
Identify external dependencies and integrations and map them to entry points.

### Constraints:

- You MUST catalog all third-party libraries and their purposes from package manager files
- You MUST identify external APIs consumed from API client implementations
- You MUST document services the application depends on from service client code
- You MUST identify integration patterns used
- You MUST document configuration management for external services
- You MUST analyze any files named "Config" or similar in detail
- You MUST create a dependency map for each entry point identified in Step 4
- You MUST create a dependency matrix showing shared dependencies
- You MUST cite specific file paths and line numbers for each dependency reference
- You MUST clearly state when a dependency's purpose isn't clear from the code
- You MUST append the analysis results to the output file with proper formatting

## 8. Error Handling and Logging Analysis
Analyze the error handling and logging approach.

### Constraints:

- You MUST identify error handling patterns from try/catch blocks and error handlers
- You MUST document exception hierarchies from exception class definitions
- You MUST analyze the logging strategy from logger usage and configuration
- You MUST identify log output destinations and storage mechanisms
- You MUST document log levels and filtering mechanisms
- You MUST identify structured logging patterns
- You MUST document monitoring hooks and alerting mechanisms
- You MUST cite specific configuration files for each logging mechanism
- You MUST note when logging destinations vary by environment
- You MUST append the analysis results to the output file with proper formatting

## 9. Testing Strategy Analysis
Explain the testing approach based on test files and infrastructure.

### Constraints:

- You MUST identify types of tests present from test files and directories
- You MUST document test coverage from coverage reports or tooling configuration
- You MUST identify mocking strategies from mock implementations
- You MUST document test data management from test data files or fixtures
- You MUST analyze CI/CD integration for tests from CI configuration files
- You MUST objectively note when testing appears incomplete
- You MUST append the analysis results to the output file with proper formatting

## 10. Security Mechanisms Analysis
Identify security mechanisms in the codebase.

### Constraints:

- You MUST document authentication and authorization approaches from auth code
- You MUST identify input validation and sanitization mechanisms
- You MUST document protection against common vulnerabilities
- You MUST analyze sensitive data handling approaches
- You MUST document security-related configurations
- You MUST cite specific implementations for each security mechanism
- You MUST note when important security aspects appear to be handled externally
- You MUST append the analysis results to the output file with proper formatting

## 11. Performance Considerations Analysis
Analyze performance-related aspects of the code.

###Constraints:

- You MUST identify caching strategies from cache implementations
- You MUST document resource optimization techniques
- You MUST analyze concurrency handling from threading or async code
- You MUST identify scalability approaches from scaling-related configuration
- You MUST document performance bottlenecks and optimizations from comments
- You MUST state when performance considerations are not explicitly addressed
- You MUST append the analysis results to the output file with proper formatting

## 12. Code Organization and Standards Analysis
Evaluate the code organization based on observable patterns.

### Constraints:

- You MUST analyze the directory structure and its rationale
- You MUST identify naming conventions from file and symbol names
- You MUST document coding standards followed from patterns or linter configurations
- You MUST evaluate modularity and separation of concerns
- You MUST analyze documentation practices from comments and documentation files
- You MUST only describe what is directly observable without speculation
- You MUST append the analysis results to the output file with proper formatting

## 13. Development Workflow Analysis
Determine the development workflow from workflow-related files.

### Constraints:

- You MUST analyze the build system and configuration from build files
- You MUST identify deployment mechanisms from deployment scripts
- You MUST document environment management from configuration files
- You MUST identify feature flagging or toggling mechanisms
- You MUST document release process indicators
- You MUST note when aspects of the workflow are not evident in the codebase
- You MUST append the analysis results to the output file with proper formatting

## 14. Technical Debt Assessment
Identify potential technical debt based on objective indicators.

### Constraints:

- You MUST identify code complexity hotspots from files with high line count or nested logic
- You MUST document duplicated code blocks
- You MUST identify outdated dependencies from version numbers
- You MUST catalog TODOs or FIXMEs from comments
- You MUST document areas with explicit comments about needed refactoring
- You MUST avoid subjective judgments about code quality
- You MUST cite specific files and line numbers for each observation
You MUST append the analysis results to the output file with proper formatting

## 15. Domain-Specific Analysis
Analyze the codebase from a domain perspective.

### Constraints:

- You MUST document how domain concepts are represented from domain model classes
- You MUST identify domain-specific patterns or algorithms
- You MUST analyze business logic implementation
- You MUST document domain language usage from naming and comments
- You MUST analyze domain requirements implementation
- You MUST note when the domain is unclear from the code alone
- You MUST append the analysis results to the output file with proper formatting

## 16. Dependency Graph Analysis
Generate a dependency graph based on import statements and function calls.

### Constraints:

- You MUST show major components and their relationships
- You MUST identify circular dependencies from import cycles
- You MUST document architectural boundaries from package organization
- You MUST document architectural boundaries from package organization
- If creating dependency graphs, you MUST use Mermaid diagram syntax and include the diagram directly in the markdown document
- You MUST use appropriate Mermaid diagram types (flowchart or graph) for dependency visualization
- You MUST note when the dependency structure is too complex to represent accurately
- You MUST append the analysis results to the output file with proper formatting

## 17. Code Quality Metrics Analysis
Analyze code quality metrics based on observable characteristics.

### Constraints:

- You MUST identify files with high cyclomatic complexity from nested control structures
- You MUST document methods with unusually high line counts
- You MUST analyze class coupling from dependency counts
- You MUST identify deep inheritance hierarchies
- You MUST calculate comment-to-code ratio from comment density
- You MUST present observations rather than judgments
- You MUST cite specific examples for each metric
- You MUST append the analysis results to the output file with proper formatting

## 18. Summary and Recommendations
Summarize findings and provide recommendations based on the analysis.

### Constraints:

- You MUST summarize the codebase's strengths from well-implemented features
- You MUST summarize areas that may need attention from TODOs or other indicators
- You MUST provide 3-5 recommendations based directly on analysis findings
- You MUST suggest next steps for developers focused on documentation or clarity improvements
- You MUST cite specific analysis findings for each recommendation
- You MUST acknowledge limitations when there isn't enough information for confident recommendations
- You MUST append the analysis results to the output file with proper formatting

- You MUST save the final document to the specified output file
- You SHOULD inform the user that the analysis is complete and where to find the results
