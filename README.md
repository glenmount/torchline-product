# torchline-product

## Fogbreaker — Micro Grant #2 (Pulse v0.1)

**Build (tiny & exact):** detect public doc changes → write a `DeltaReceipt` to `fogbreaker-app/pulse/events.jsonl` → re-rank providers → publish `fogbreaker-app/pulse/rankings/top10.json` → (optional) daily digest under `fogbreaker-app/pulse/ledger/`.

**Contract**
- Allowed edits: `fogbreaker-app/pulse/**`
- `top10.json` must include `generated_at`, `preset`, non-empty `ranked[]`, and `providers[]`
- `events.jsonl` is JSON Lines with: `observed_at, kind (pricing_pdf|audit_pdf|stars_extract), provider_id, source, sha256, size_bytes`
- Deterministic: same inputs → same bytes
- PRs are scored and **closed** (not merged). No network calls. No PII.
