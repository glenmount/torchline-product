import json, sys, re, os

events_path = "fogbreaker-app/pulse/events.jsonl"
if not os.path.exists(events_path):
    print("events.jsonl not found (OK for scaffolds)")
    sys.exit(0)

allowed = {"pricing_pdf","admissions_pdf","audit_pdf","complaint_pdf","stars_extract","edit_pdf"}
ok = True
problems = []

with open(events_path, "r") as fh:
    for i, line in enumerate(fh, 1):
        line = line.strip()
        if not line:
            continue
        try:
            o = json.loads(line)
        except Exception as e:
            problems.append(f"line {i}: invalid JSON ({e})"); ok = False; continue
        req = ["observed_at","kind","provider_id","source","sha256","size_bytes"]
        for k in req:
            if k not in o:
                problems.append(f"line {i}: missing {k}"); ok = False
        if "kind" in o and o["kind"] not in allowed:
            problems.append(f"line {i}: kind '{o['kind']}' not in {sorted(allowed)}"); ok = False
        if "sha256" in o and not re.fullmatch(r"[0-9a-f]{64}", str(o["sha256"])):
            problems.append(f"line {i}: sha256 must be 64 hex chars"); ok = False

if not ok:
    print("\n".join(["❌ events.jsonl issues:"] + problems))
    sys.exit(1)

print("✅ events.jsonl OK or empty")
