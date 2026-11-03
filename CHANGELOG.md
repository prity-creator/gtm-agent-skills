# Changelog

All notable changes to this project are listed here. Versions follow semantic versioning.

## [1.0.0] - 2026-11-03

### Added
- 10 skills: icp-builder, signal-scout, account-research, opener-writer, follow-up-writer, reply-handler, campaign-builder, inbox-analyzer, post-from-call, pipeline-report.
- Plugin manifest (`.claude-plugin/plugin.json`) and marketplace catalog (`.claude-plugin/marketplace.json`).
- Scripts (Python 3 standard library only): `analyze.py` (inbox analysis), `check_opener.py` (opener self-check), `propose_times.py` (two call times across time zones), `report.py` (weekly pipeline report).
- Synthetic samples: `sample_threads.csv` (30 fake threads) and `sample_leads.csv` (40 fake leads).
- Templates: `icp.md`, `voice.md`, `offer.md`, `campaign-template.md`.
