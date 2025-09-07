import json, sys

P = "fogbreaker-app/pulse/rankings/top10.json"
try:
    data = json.load(open(P))
except Exception as e:
    print(f"Invalid JSON in {P}: {e}")
    sys.exit(1)

problems = []
for k in ("generated_at", "preset", "ranked", "providers"):
    if k not in data:
        problems.append(f"missing key: {k}")

if not isinstance(data.get("ranked"), list) or not data["ranked"]:
    problems.append("ranked[] must be a non-empty list")

if not isinstance(data.get("providers"), list) or not data["providers"]:
    problems.append("providers[] must be a non-empty list")

pids = {x.get("provider_id") for x in data.get("providers", []) if isinstance(x, dict)}
for r in data.get("ranked", []):
    if r not in pids:
        problems.append(f"ranked id '{r}' missing from providers[]")

if problems:
    print("\n".join(["❌ Top-10 issues:"] + problems))
    sys.exit(1)

print("✅ top10.json OK")
