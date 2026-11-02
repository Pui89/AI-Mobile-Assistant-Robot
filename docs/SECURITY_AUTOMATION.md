# Security and Automation Plan

**Status: automation definitions added; execution results must be confirmed by GitHub Actions.**

## Automated checks

| Control | Trigger | Purpose |
|---|---|---|
| Tests | Push, pull request, manual CI | Detect functional regressions |
| Dependency audit | Push, pull request, weekly, manual | Identify known vulnerable installed Python packages |
| Bandit | Same security workflow | Flag selected Python security patterns |
| CodeQL | Same security workflow | Static analysis for supported Python code patterns |
| Gitleaks | Same security workflow | Detect likely secrets in repository history |
| Dependency review | Pull requests | Flag risky newly introduced dependencies |
| Dependabot | Weekly | Propose dependency and GitHub Actions updates |

## Security principles

1. Least-privilege workflow permissions; workflows should be read-only unless a specific reporting permission is required.
2. No secrets, API keys, passwords, private sensor credentials or personal data in source control, logs or test fixtures.
3. Validate and bound all incoming sensor data; reject malformed units, timestamps and impossible values.
4. Treat sensor readings, filenames, metadata and external messages as untrusted input.
5. Preserve provenance, timestamps, quality flags and uncertainty in every finding.
6. Fail visibly when evidence is missing, stale, contradictory or untrusted. Never silently convert missing data into a normal state.
7. No autonomous operation of locks, doors, lifts, breakers, valves, alarms or evacuation controls.
8. Review dependency ownership, provenance, licence, maintenance, permissions and cost before adoption.
9. Use synthetic data for automated tests; do not upload private building telemetry as CI artifacts.
10. Review workflow changes and security alerts before merging.

## Operational security backlog

- [ ] Enable GitHub secret scanning and push protection where available for this repository.
- [ ] Enable Dependabot security updates and alerts in repository settings.
- [ ] Enable private vulnerability reporting if available.
- [ ] Protect the default branch: require pull requests and passing checks; restrict force pushes and deletion.
- [ ] Require CODEOWNERS review for workflow and security-policy changes when maintainers are available.
- [ ] Pin third-party GitHub Actions to reviewed full commit SHAs before production-grade use.
- [ ] Add signed release provenance and an SBOM before distributing deployable builds.
- [ ] Add authenticated, encrypted sensor-gateway communication only when real integrations are designed.
- [ ] Define retention, access control, audit logging and incident-response procedures before any building pilot.

## Evidence and limitations

A green workflow means only that the configured checks passed for that commit. It does not prove absence of vulnerabilities, certify a building, validate sensors, or establish real-world hazard-detection performance. Record scan results, false positives, exceptions and remediation decisions. Do not claim a control is enabled until the corresponding GitHub setting or workflow result has been verified.
