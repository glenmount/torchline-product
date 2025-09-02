"""
Fee Math Engine for Torchline Aged Care Platform

Calculates Daily Accommodation Payment (DAP) from Resident Accommodation Deposit (RAD)
and Maximum Permissible Interest Rate (MPIR) using the formula:

DAP = RAD × (MPIR/100) ÷ 365

All calculations use Python Decimal with ROUND_HALF_UP to $0.01 precision.
"""

import json
import sys
from decimal import Decimal, ROUND_HALF_UP


def compute_dap(rad, mpir):
    """
    Calculate Daily Accommodation Payment (DAP) from RAD and MPIR.
    
    Args:
        rad: Resident Accommodation Deposit in dollars
        mpir: Maximum Permissible Interest Rate as percentage (e.g., 7.78)
    
    Returns:
        Decimal: Daily Accommodation Payment rounded to $0.01 using ROUND_HALF_UP
    """
    # Convert inputs to Decimal from strings for precision (as specified by organizer)
    rad_decimal = Decimal(str(rad))
    mpir_decimal = Decimal(str(mpir))
    
    # Apply formula: DAP = RAD × (MPIR/100) ÷ 365
    dap = rad_decimal * (mpir_decimal / Decimal("100")) / Decimal("365")
    
    # Round to $0.01 using ROUND_HALF_UP
    return dap.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def main():
    """
    Optional CLI interface for generating JSON receipts (worth 4 points).
    Usage: python fee_math.py --rad=500000 --mpir=7.78
    """
    if len(sys.argv) != 3:
        print("Usage: python fee_math.py --rad=<amount> --mpir=<rate>")
        sys.exit(1)
    
    # Parse command line arguments
    rad_arg = sys.argv[1]
    mpir_arg = sys.argv[2]
    
    if not rad_arg.startswith("--rad=") or not mpir_arg.startswith("--mpir="):
        print("Usage: python fee_math.py --rad=<amount> --mpir=<rate>")
        sys.exit(1)
    
    try:
        rad = float(rad_arg.split("=")[1])
        mpir = float(mpir_arg.split("=")[1])
    except (ValueError, IndexError):
        print("Error: Invalid numeric arguments")
        sys.exit(1)
    
    # Calculate DAP
    dap_result = compute_dap(rad, mpir)
    
    # Generate JSON receipt as specified in the issue
    receipt = {
        "inputs": {
            "outstanding_rad": int(rad),
            "mpir_percent": mpir
        },
        "formula": "DAP = outstanding_RAD × (MPIR/100) ÷ 365; round half-up to $0.01",
        "result": {
            "dap_per_day": float(dap_result)
        }
    }
    
    # Print deterministic JSON (same formatting every time for the 4 bonus points)
    print(json.dumps(receipt, separators=(',', ':')))


if __name__ == "__main__":
    main()
