"""
Fee Math Engine for Torchline Aged Care Platform
"""

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
    # Convert inputs to Decimal from strings for precision
    rad_decimal = Decimal(str(rad))
    mpir_decimal = Decimal(str(mpir))
    
    # Apply formula: DAP = RAD × (MPIR/100) ÷ 365
    dap = rad_decimal * (mpir_decimal / Decimal("100")) / Decimal("365")
    
    # Round to $0.01 using ROUND_HALF_UP
    return dap.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
