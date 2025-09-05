from decimal import Decimal, ROUND_HALF_UP
import json, sys, hashlib

def dap_per_day(rad: Decimal, mpir: Decimal) -> Decimal:
    return (rad * (mpir / Decimal("100")) / Decimal("365")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: fee_math.py <RAD_dollars> <MPIR_percent> <pricing_pdf_path>", file=sys.stderr)
        sys.exit(1)
    rad = Decimal(str(sys.argv[1])); mpir = Decimal(str(sys.argv[2])); pdf = sys.argv[3]
    print(json.dumps({
        "inputs": {"rad": float(rad), "mpir": float(mpir)},
        "formula": "DAP = RAD × (MPIR/100) ÷ 365; Decimal ROUND_HALF_UP to $0.01",
        "result": {"dap_per_day": float(dap_per_day(rad, mpir))},
        "source": {"pricing_doc_path": pdf, "pricing_doc_sha256": hash_file(pdf)}
    }))
