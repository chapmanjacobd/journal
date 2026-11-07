# AI Prompts

## Code review
- Scan the repo for any confusing logic or things that don't seem quite right
- Check for unfinished scaffolding beyond simple TODO checks; and any incomplete, contradictory, or redundant features. Any blocking ambiguities?
- which of the following critiques are valid?
- Do a PR review of git show HEAD

## Data and state design
- Interrogate the data types and schema we plan to use for its performance and data storage costs, as well as any existing data and schema that will be as-of-yet unchanged by our plans.
- Make a decision table for all the states and outputs. Think about possible edge-cases and suggest guarding strategies

## Testing and diagnostics
- play around with this site in playwright and note any bugs or strange behavior
- Take a look at the workflow tests and other tests to see where there are gaps in UX (eg. a common task requiring more than 2 CLI commands); as well as duplicated functionality (ignore different names for things--like if there's two different commands but they both have the same type signature). Identify candidates for subcommand merging or core API refactoring. reverse compatibility is not needed anywhere at this time as everything is alpha
- aggregate the most common (with at least repeat qty >5) lines in journalctl from the last 25 hours

## Conventions and tooling
- verify that this codebase is following modern linux conventions and note any Unix/POSIX irregularities
- Lets get `make lint` passing by strictly following linting recommendations. don't add ignores or modify lint config

## Documentation and technical writing
- Remove any change-oriented phrasing and rewrite *.md documentation as stable present-tense behavior.
- lets rewrite .md to be better technical writing but don't get too crazy. try to keep things concise
- Adhere the documentation and application interfaces to the ADS-STE100 standard. Ensure confusing or duplicated synonyms are not distinct before conflating / coalescing. But don't add a definition or terms section literally to the document.

## Planning
- Break down these tasks into user decision artifact plans where structural changes happen first. Include context for a future agent as each plan will be executed independently

## Golang
- Use t.Errorf instead of t.Failf
- Use table-driven tests https://go.dev/wiki/TableDrivenTests
