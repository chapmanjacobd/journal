Scan the repo for any confusing logic or things that don't seem quite right
Make a decision table for all the states and outputs. Think about possible edge-cases and suggest guarding strategies
Do a PR review of git show HEAD
Lets get `make lint` passing by strictly following linting recommendations. don't add ignores or modify lint config

## Golang
Use t.Errorf instead of t.Failf
Use table-driven tests https://go.dev/wiki/TableDrivenTests
