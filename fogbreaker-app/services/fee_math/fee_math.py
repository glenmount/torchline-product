from decimal import Decimal, ROUND_HALF_UP
def dap_per_day(rad: Decimal, mpir: Decimal) -> Decimal:
    return (rad * (mpir / Decimal("100")) / Decimal("365")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
