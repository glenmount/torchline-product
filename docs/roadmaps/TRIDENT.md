# TRIDENT Roadmap (Families)

**Outcome:** Source-linked copilot for fees/rights/safety with date-aware answers and a deterministic fee engine.

## Phase 0 — Definition of Done
1) 150 NSW homes with provider packs (agreement/admissions, pricing/additional services, ACQSC report, complaints policy).  
2) Canonical national set loaded (fees, MPIR, subsidies, care-minutes, star methodology, Charter, SIRS, restrictive practices, infection control, admissions, ACP).  
3) Date-aware retrieval; fee-math uses **agreement-date MPIR**; rounding to $0.01.  
4) Demo UI: chat with inline citations & dates; RAD↔DAP calc; 2–3 home compare; p95 < 4s.  
5) Evals: 50 Qs; numeric ±$0.01; citations ≥95%; date-scope ≥90%.

## Services
- `fee_math` (RAD↔DAP; partial RAD; caps; deterministic receipts)
- Star explainer; compare; shareable answers

## Safety & Discipline
- No scraping of restricted sources; public docs or user-provided with consent
- Every answer: Date → Number → Citation → Explain → Verify
