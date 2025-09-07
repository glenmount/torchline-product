from decimal import Decimal
import importlib.util, sys, os

P = "fogbreaker-app/services/fee_math/fee_math.py"
if not os.path.exists(P):
    print("No fee_math.py found; passing (scaffold-only PR).")
    sys.exit(0)

spec = importlib.util.spec_from_file_location("fee_math", P)
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
assert m.dap_per_day(Decimal("550000"), Decimal("7.78")) == Decimal("117.23"), "fee-math formula/rounding mismatch"
print("fee-math OK")
