Scan the repo for any confusing logic or things that don't seem quite right
Check for unfinished scaffolding beyond simple TODO checks
Create a report that lists all the incomplete, contradictory, or redundant features
Make a decision table for all the states and outputs. Think about possible edge-cases and suggest guarding strategies
Do a PR review of git show HEAD
Lets get `make lint` passing by strictly following linting recommendations. don't add ignores or modify lint config
Remove any change-oriented phrasing and rewrite *.md documentation as stable present-tense behavior.
break down these tasks into user decision artifact plans where structural changes happen first. Include context for a future agent as each plan will be executed independently

## Golang
Use t.Errorf instead of t.Failf
Use table-driven tests https://go.dev/wiki/TableDrivenTests
