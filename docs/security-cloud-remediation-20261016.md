# Security Cloud remediation — 2026-10-16

Scan: https://chatgpt.com/codex/cloud/security/runs/wfr_69668854857176aa5b5000ad4cfda499dcbde22d9ffaec64a16187a32185a252

Scanned/base revision: `cbf190c2b3fcf367c12a294d1802fcf339eacc67`. Proposed repair, not publication or production authorization.

The Discovery, AoA and main routing instructions explicitly classify source content as untrusted evidence. Embedded instructions cannot authorize tools, alter the task or redirect reporting. This is a policy correction; it is not evidence that prompt injection is universally prevented. Validation actions now use immutable commit IDs. CI installs an exact Python 3.12 Linux dependency lock with enforced SHA-256 hashes; all six distributions were downloaded and hashed locally.

Validation: published proposal validator passed all five fixtures; 13 unittest tests passed using dependencies installed from the hash lock. No paid agent trials or external communications ran.

No selected hub pin changed. Scan findings remain open pending PR review and source-bound verification.
