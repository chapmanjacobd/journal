Scan the repo for any confusing logic or things that don't seem quite right
Check for unfinished scaffolding beyond simple TODO checks
Create a report that lists all the incomplete, contradictory, or redundant features
Make a decision table for all the states and outputs. Think about possible edge-cases and suggest guarding strategies
Do a PR review of git show HEAD
Lets get `make lint` passing by strictly following linting recommendations. don't add ignores or modify lint config
Remove any change-oriented phrasing and rewrite *.md documentation as stable present-tense behavior.
Break down these tasks into user decision artifact plans where structural changes happen first. Include context for a future agent as each plan will be executed independently
Take a look at the workflow tests and other tests to see where there are gaps in UX (eg. a common task requiring more than 2 CLI commands); as well as duplicated functionality (ignore different names for things--like if there's two different commands but they both have the same type signature). Identify candidates for subcommand merging or core API refactoring. reverse compatibility is not needed anywhere at this time as everything is alpha
lets rewrite .md to be better technical writing but don't get too crazy. try to keep things concise

Adhere the documentation and application interfaces to the ADS-STE100 standard. Clarify confusing or duplicated synonyms as distinct before conflating / coalescing.

## Golang
Use t.Errorf instead of t.Failf
Use table-driven tests https://go.dev/wiki/TableDrivenTests
