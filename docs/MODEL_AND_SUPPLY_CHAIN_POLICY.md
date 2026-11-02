# Model, Data and Software Supply-Chain Policy

This project excludes Chinese-origin AI models, Chinese model providers and Chinese model-hosting services from its approved stack. No such model or service is used by the initial foundation. This is a project-specific procurement constraint; every component still requires evidence-based review.

Starting posture: Python standard library core; pytest for tests; no model downloads, telemetry, remote inference, API keys, paid APIs, subscriptions or cloud GPUs; prefer offline reproducibility.

Before adding a model/dependency, record publisher/ownership/origin, release and checksums, licence, data provenance, runtime and transitive dependencies, vulnerabilities, network calls, telemetry, data residency, hardware/resource needs, costs, benchmark against non-ML baseline, failure modes, uncertainty calibration, rollback and human approval.

Open-source does not automatically mean safe. Review licence compatibility, maintainer health, release integrity, dependency provenance, security advisories and network behavior. Real building data requires documented permission, privacy review, retention limits, access controls and lawful basis. Do not upload private audio, indoor imagery or occupancy data to external model services by default.
