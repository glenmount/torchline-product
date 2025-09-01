from decimal import Decimal, ROUND_HALF_UP, getcontext
import argparse
import json

def compute_dap(outstanding_rad: float, mpir_percent: float) -> Decimal:
    getcontext().prec = 28
    RAD = Decimal(str(outstanding_rad))
    MPIR = Decimal(str(mpir_percent)) / Decimal(100)
    daily = RAD * MPIR / Decimal(365)
    return daily.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def receipt(outstanding_rad: float, mpir_percent: float) -> dict:
    result = compute_dap(outstanding_rad, mpir_percent)
    return {
        "inputs": {"outstanding_rad": float(outstanding_rad), "mpir_percent": float(mpir_percent)},
        "formula": "DAP = outstanding_RAD × (MPIR/100) ÷ 365; round half-up to $0.01",
        "result": {"dap_per_day": float(result)}
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fee-Math: DAP calculator (deterministic)")
    parser.add_argument("--rad", type=float, required=True, help="Outstanding RAD (AUD)")
    parser.add_argument("--mpir", type=float, required=True, help="MPIR (%) to apply")
    args = parser.parse_args()
    print(json.dumps(receipt(args.rad, args.mpir), separators=(",", ":")))
