# Fogbreaker — Micro Grant #2 (ELI5)
Watch public docs → write a DeltaReceipt to `fogbreaker-app/pulse/events.jsonl` → re-rank → publish `fogbreaker-app/pulse/rankings/top10.json` → (optional) daily digest `pulse/ledger/digest-YYYY-MM-DD.json`.

**DeltaReceipt (JSONL, one per line)**  
{"observed_at":"2025-09-06T02:15:10Z","kind":"pricing_pdf","provider_id":"ACME-123","source":"fogbreaker-app/corpus/packs/ACME-123/pricing/2025-08.pdf","sha256":"...","size_bytes":184232,"rank_effect":2,"notes":"new pricing"}

**Top-10 (minimal)**
{"generated_at":"2025-09-06T02:15:55Z","preset":"Balanced","ranked":["ACME-123"],"providers":[{"provider_id":"ACME-123","score":87.4,"factors":{"cost":null,"cost_fit":0.5,"transparency":0,"quality":0,"policy":0}}]}

**Rails:** allowed edits `fogbreaker-app/pulse/**`; no network; no PII; deterministic (same inputs → same bytes).  
**Enter:** fork → checkout `reset/scaffold` → implement under `pulse/**` → PR with a 150–200 word “Crusade Selfie.”  
**Acceptance:** re-rank provable (viewer “Updated” **or** new `generated_at` + order change), valid receipts, daily digest when receipts exist, determinism, path-confinement.  
**Scoring (20):** Accuracy 8 • Receipts 4 • Determinism/Perf 4 • Code 4.  
*Note: stale-stars penalty is out of scope for MG2 (Watchtowers phase).*
