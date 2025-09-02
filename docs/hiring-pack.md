# Torchline Pilgrim Hiring Pack (v1.1)

**Ladder:** Micro-grants (A$1k, 1–3w) → Trialships (A$2.5k, 2–4w) → Fellowships (A$7.5k, 8–12w, 10–15h/w).  
**Young Scholars (<18):** 6×A$500 scholarships; synthetic/public data only; guardian consent; WWCC mentors.

## Micro-Grants (copy-paste scopes)
1) **Fee-Math (TRIDENT):** RAD↔DAP, partial RAD, caps, rounding; MPIR passed in; ±$0.01; <200ms; idempotent; receipts.  
2) **Provider-Pack Harvester (TRIDENT):** 10 homes × 4 docs; registry JSON with SHA-256; QA sheet; public links only.  
3) **Cited-Answer Templates (TRIDENT):** 5 answers using Date→Number→Citation→Explain→Verify; ≥95% citation correctness.

## Trialships
- Engineer: fee-math + retrieval + 50-Q eval.  
- Frontend: chat UI with inline citations/date; 2-home compare; share link.  
- Data & Automation: expand registry 10→150; staleness flags; coverage dashboard.  
- Facility Ops (SENTINEL): nudge receipts (sterile-cockpit, hydration, duress) with timing & compliance.

## Hiring KPIs
CQ ≥ 8/10; Purge Meter ≥80%; Micro-grant→Trial ≥30%; Trial→Fellow ≥25%; decision time ≤7 days; diversity targets.

## Privacy Checklist (attach to every artifact)
Provenance URLs + SHA-256; consent status (grants must be public-only); no audio/video; determinism proof (5×); red-team notes.

## Appendix — Fee-Math Unit Tests (12)
Use DAP = outstanding_RAD × (MPIR/100) ÷ 365; round half-up to $0.01.
1) 550,000 @ 7.78% → 117.23; 2) 1,000,000 @ 7.78% → 213.15; 3) 400,000 @ 7.78% → 85.26; 4) 400,000 @ 8.17% → 89.53;  
5) 123,456 @ 7.78% → 26.31; 6) 999,999 @ 7.78% → 213.15; 7) 0 → 0.00; 8) 500,000 @ 7.78% → 106.58;  
9) 500,000 @ 8.17% → 111.92; 10) 50,000 @ 7.78% → 10.66; 11) 1,500,000 @ 7.78% → 319.73; 12) 275,000 @ 7.78% → 58.62.
