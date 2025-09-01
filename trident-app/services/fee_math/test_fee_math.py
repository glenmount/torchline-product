from decimal import Decimal
from fee_math import compute_dap

CASES = [
    (550000, 7.78, Decimal("117.23")),
    (1000000, 7.78, Decimal("213.15")),
    (400000, 7.78, Decimal("85.26")),
    (400000, 8.17, Decimal("89.53")),
    (123456, 7.78, Decimal("26.31")),
    (999999, 7.78, Decimal("213.15")),
    (0, 7.78, Decimal("0.00")),
    (500000, 7.78, Decimal("106.58")),
    (500000, 8.17, Decimal("111.92")),
    (50000, 7.78, Decimal("10.66")),
    (1500000, 7.78, Decimal("319.73")),
    (275000, 7.78, Decimal("58.62")),
]

def test_fee_math_cases():
    for rad, mpir, expected in CASES:
        got = compute_dap(rad, mpir)
        assert got == expected, f"RAD={rad} MPIR={mpir}: got {got}, expected {expected}"
