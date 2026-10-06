# Changelog

## 2026-10-06 — optional Index proposal handoff profile v1.0

- Added `research-intelligence-proposal/1.0` as an optional, unaccepted proposal representation.
- Added a read-only mapping to The Index at commit `d5e45d275cb301d9684b543e93b05997991d1cf2`.
- Added synthetic fixtures for rejected transfer, contradictory evidence, unexecuted experiment, negative result revision, and supported-but-unaccepted proposal.
- Added Draft 7 JSON Schema instance validation plus semantic proposal/link validation and a behavioral evaluation specification.
- Added positive/negative regression tests and CI for the five published fixtures, including malformed types/enums, undeclared fields, component/kind boundaries, experiment-result rules, and Discovery/AoA abstraction boundaries.
- Added explicit `executed` + `result_status: unavailable` handling so missing results are recorded rather than fabricated.
- Preserved Research Intelligence Protocol v1.0, Discovery/AoA separation, standalone use, and public IP boundaries.
