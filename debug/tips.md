# Tips for debugging code with Kiro CLI and Q Developer

Here are some current good practices to help you use Kiro CLI and Q Developer to more effectively troubleshoot and resolve bugs in your code.

I have written about this publicly, which you can read [here](https://dev.to/aws/amazon-q-developer-tips-no23-debugging-with-amazon-q-11ee)

## Keep debug task small

- Keep the debugging tasks small - when you have several bugs that might come at you at once, the temptation is to just ask Kiro/Q to "fix the bugs". Whilst this might be effective in small, less complex issues, your results will vary as size and complexity increase. The trick is to use your skill as a developer and identify discrete issues and then debug those one at a time.

## Keeping on task

- Create an issue-log.md and add issues (with additional info) to this. Ask Kiro/Q to go through one at a time to resolve issues. This way you have a log which can be used as context. Make sure you ask it to document the issue, fix so you have the right info.

- Time box debugging activity - if you are spending more than 30 mins on an issue, you should pause and take a step back. If you have already tried the other techniques in this doc, then you might want to use checkpoints or git to revert code changes (if debugging is down to changes you have mode).

## Try different models

- Kiro/Q offer different models - If you are struggling to get to a resolution, you should try different models. Starting with Auto, work to increasingly more sophisticated models.

## Prompt design

- Prompt design matters - When I am trying to fix errors that come up, I have found that I re-use certain prompts/phrases that seem to work well. This is useful in conjunction with providing the right context (next section). Make sure you start to collect as an organisation useful prompts that work within your developer communication channels.

## Provide the right context

The most effective way to get better debugging results from using Kiro/Q is to make sure you are providing the right context. Here are some pointers.

- What is happening when the error occurs - the biggest failure from using Kiro/Q is to provide only part of the information needed to help provide a good solution. For example, just providing a stack trace and asking for Kiro/Q to fix the issue. You should always provide situational awareness when asking for a fix. For example, "when I do x in the web browser, I expect y, but get z and this is an error/stack trace that is produced". The same applies for non user issues, for example "when the system x is running, y event happens, and this stack error is produced".

- Provide details about changes you made - If you made changes, then add the change you made as context. Be specific: what files did you change and why. Add the previous state if you can (this is where providing git diff as context can be helpful)

- Provide the right context within your project - Kiro/Q provide lots of ways to provide specific context about the projects you are working on. These are very effective and helping Kiro/Q prioritise where to look. For example, open up the specific file in the editor if you suspect that is where the issue is. Sometimes it might be easier to copy down logs and make them available, other times and if possible, you can use MCP servers to "connect" to a system. (e.g. CloudWatch)

- What was the expected behaviour - Make sure you add what the expected behaviour is supposed to be as context. I often see this as a miss.


```
k --agent debug
"review the cloudwatch log group "kiro-clo-debugging-demo" for any anomalies in eu-west-1"
```

- Kiro/Q love patterns - we no longer need to print to console.log to help us debug. We have over instrument our applications (use your favorite logging framework), and make it configurable.  Whilst you don't want to go through all logs generated, AIs love this as context. Observability is very useful in this use case, and you can turn it on/off as needed. This extends to debugging systems that might centralise logs (CloudWatch)


- Use more than logs and stack traces to help you debug issues - You can  attach screenshots (and annotate them), providing text to explain what the issue is. This can be useful when other ways of trying to explain an issue are imprecise.

- Don't forget browser logs! - Using browser debugging tools, you can use the output of these (Inspector/Console) to provide lots great context and errors that might be missing from the server side.

- Clearing context and starting again - Sometimes context can get confused, so open a new chat window and try again. There can be lots of reasons for this, so using /clear and re-starting is something to try if everything else has failed. This technique tends to work better when combined with other tips in this doc (for example, maintaining an issue log)



---

Example of an issue-log.md

```
## Issues log

## Overview

This issue list outlines issues with the application that have been identified by user testing. When reviewing this list:

- ALWAYS run tests after making any code changes - if updates break tests, undo and try again
- NEVER alter/change tests - EVER!
- AFTER completing each issue, ASK FOR A REVIEW and confirmation of the fix
- DO NOT PROCEED to the next task until the application is in a working state
- Fix ONLY ONE ISSUE at a time
- Do NOT delete/remove the existing planning docs - always APPEND/ADD

## Notes

- Virtual environment: venv
- Application code location: src/ directory
- Data model: data_model/complete_schema.sql
- PyTests location: src/tests/ directory
- End to End Tests with addition tests: testing/

### Issues


[ ] - When you open a fact, when you click on the view history link it generates - jinja2.exceptions.TemplateNotFound: fact/history.html - **FIXED**: Created comprehensive fact/history.html template with timeline-based edit history display, showing previous versions, edit reasons, timestamps, and proper navigation. Also fixed UndefinedError by using fact.author instead of fact.user to match the database relationship structure.
[ ] - When you view a fact, the pull down menu (Edit Fact, View History, Delete Fact) is initially hidden behind the Fact Statitistic widget

### Fixed Issues


[x] - When voting on a claim, whilst the voting works successfully, an error message is displayed "An error occurred when submitting your vote" which you can see in the screen shot (images/issue-1.png). I can also see the following in the logs "[2025-08-22 17:22:33,098] ERROR in services: Vote blocking check error: 'AuditLog' object has no attribute 'action_type'"
[x] - Two failing unit tests in src/tests/ directory - **FIXED**: Updated test expectations to match correct authentication behavior (401 for JSON requests instead of 302 redirect)
[x] - When logged in as a user, when trying to comment on a fact, the screen generates a "Failed to create comment" message and I can see that the POST /comments/create generates an HTTP 500 error - **FIXED**: Updated comment creation route to properly handle authentication and fixed attribute references (nesting_level vs depth). Cleaned up all debugging code.
[x] - When you view a fact, there is an error about not be able to display comments - **FIXED**: Updated comment route to handle Comment model attributes correctly
[x] - Trying to edit a fact generates an error jinja2.exceptions.TemplateNotFound: fact/edit.html - **FIXED**: Created missing fact/edit.html template with full editing functionality
[x] - From the "/facts" page, the correct number of votes for fact or fake for a give claim is not correctly displayed. - **FIXED**: Updated facts list template to load actual vote counts via AJAX and enable voting functionality
```




