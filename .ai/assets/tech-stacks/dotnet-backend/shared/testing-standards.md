# Testing Standards Prompt (Dotnet)

General testing standards for .NET migration.

## Rules
- xUnit + BDDfy is the default profile; a target team may explicitly opt out of the BDDfy package
- Given-When-Then structure and naming are mandatory for unit, use-case, and integration tests even after a BDDfy opt-out; do not substitute Arrange-Act-Assert (3A)
- `.feature` files are optional/planned; support them when provided, explicitly requested, or selected with a project feature runner, without choosing a runner/package implicitly
- NSubstitute only
- No BaseTestClass
- Async-safe event verification required
