"""
╔══════════════════════════════════════════════════════╗
║             CALC-X  |  Python Calculator             ║
║   Features: +−×÷ | Mean | Median | Mode | Avg | %   ║
╚══════════════════════════════════════════════════════╝
"""

import statistics
from collections import Counter


# ─────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────

def header(title: str) -> None:
    """Print a styled section header."""
    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")


def cast_number(raw: str) -> int | float:
    """
    Type-cast a string to int or float.
    - If the string represents a whole number → int
    - Otherwise                               → float
    Raises ValueError for non-numeric input.
    """
    raw = raw.strip()
    value = float(raw)          # raises ValueError if not numeric
    if value == int(value) and '.' not in raw:
        return int(value)       # keep as int when appropriate
    return value                # return as float


def parse_number_list(raw: str) -> list[int | float]:
    """
    Parse a comma/space-separated string into a typed number list.
    Each token is individually cast via cast_number().
    """
    tokens = raw.replace(',', ' ').split()
    if not tokens:
        raise ValueError("No numbers provided.")
    numbers = [cast_number(t) for t in tokens]
    return numbers


def show_type_info(numbers: list) -> None:
    """Print type info for each parsed number."""
    print("\n  [Type Casting Result]")
    for i, n in enumerate(numbers, 1):
        print(f"    [{i}] {n!r}  →  {type(n).__name__.upper()}")


# ─────────────────────────────────────────
#  ARITHMETIC  (+  -  *  /  %)
# ─────────────────────────────────────────

def basic_calculator() -> None:
    header("BASIC ARITHMETIC CALCULATOR  (+  -  *  /  %)")

    OPERATORS = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,   # always float division
        '%': lambda a, b: a % b,
    }

    while True:
        print("\n  Enter an expression like:  12 + 7.5   |  100 / 4   |  9 % 2")
        print("  (or type 'back' to return to the main menu)")
        raw = input("\n  >> ").strip()

        if raw.lower() == 'back':
            break

        # Split on operator (support negative numbers carefully)
        parsed = None
        for op in ['**', '//', '+', '-', '*', '/', '%']:
            # Find operator position (skip leading minus sign)
            idx = raw.find(op, 1)
            if idx != -1:
                left_str  = raw[:idx].strip()
                right_str = raw[idx + len(op):].strip()
                if left_str and right_str:
                    parsed = (left_str, op, right_str)
                    break

        if not parsed:
            print("  ✖  Could not parse expression. Use format: number operator number")
            continue

        left_str, op, right_str = parsed

        try:
            a = cast_number(left_str)
            b = cast_number(right_str)
        except ValueError as e:
            print(f"  ✖  Type casting error: {e}")
            continue

        # Show type casting info
        print(f"\n  Type cast:  '{left_str}' → {type(a).__name__}({a})")
        print(f"              '{right_str}' → {type(b).__name__}({b})")

        try:
            result = OPERATORS[op](a, b)
            # Auto-cast result to int if whole number
            display = int(result) if isinstance(result, float) and result == int(result) else result
            print(f"\n  ✔  {a} {op} {b}  =  {display}  ({type(display).__name__})")
        except ZeroDivisionError:
            print("  ✖  Error: Division by zero is undefined.")
        except Exception as e:
            print(f"  ✖  Error: {e}")


# ─────────────────────────────────────────
#  STATISTICS  (Mean, Median, Mode, Avg)
# ─────────────────────────────────────────

def compute_mean(numbers: list) -> float:
    return sum(numbers) / len(numbers)                   # same as avg

def compute_median(numbers: list) -> int | float:
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        avg = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
        return int(avg) if avg == int(avg) else avg

def compute_mode(numbers: list) -> list:
    freq = Counter(numbers)
    max_count = max(freq.values())
    if max_count == 1:
        return []  # no mode
    return sorted(k for k, v in freq.items() if v == max_count)


def statistics_calculator() -> None:
    header("STATISTICS CALCULATOR  (Mean | Median | Mode | Avg)")

    while True:
        print("\n  Enter numbers separated by commas or spaces:")
        print("  (or type 'back' to return to the main menu)")
        raw = input("\n  >> ").strip()

        if raw.lower() == 'back':
            break

        try:
            numbers = parse_number_list(raw)
        except ValueError as e:
            print(f"  ✖  {e}")
            continue

        # Show type casting
        show_type_info(numbers)

        # ── Calculations ──────────────────────────────────
        n          = len(numbers)
        total      = sum(numbers)
        mean_val   = compute_mean(numbers)
        median_val = compute_median(numbers)
        mode_vals  = compute_mode(numbers)
        min_val    = min(numbers)
        max_val    = max(numbers)
        range_val  = max_val - min_val

        # Format helper
        def fmt(v):
            return int(v) if isinstance(v, float) and v == int(v) else round(v, 6)

        print(f"""
  ┌─────────────────────────────────────┐
  │  RESULTS for {n} number(s)            
  ├─────────────────────────────────────┤
  │  Count      : {n}
  │  Sum        : {fmt(total)}
  │  Mean (Avg) : {fmt(mean_val)}
  │  Median     : {fmt(median_val)}
  │  Mode       : {', '.join(str(fmt(m)) for m in mode_vals) if mode_vals else 'No mode (all unique)'}
  │  Min        : {fmt(min_val)}
  │  Max        : {fmt(max_val)}
  │  Range      : {fmt(range_val)}
  └─────────────────────────────────────┘""")


# ─────────────────────────────────────────
#  PERCENTAGE CALCULATOR
# ─────────────────────────────────────────

def percentage_calculator() -> None:
    header("PERCENTAGE CALCULATOR")

    options = """
  Choose a percentage operation:
    [1] What is X% of Y?
    [2] X is what % of Y?
    [3] % increase / decrease from X to Y
    [4] Back to main menu
"""
    while True:
        print(options)
        choice = input("  >> ").strip()

        if choice == '4' or choice.lower() == 'back':
            break

        try:
            if choice == '1':
                x = cast_number(input("  Enter X (percentage): "))
                y = cast_number(input("  Enter Y (value):      "))
                result = (float(x) / 100) * float(y)
                print(f"\n  ✔  {x}% of {y}  =  {round(result, 6)}")

            elif choice == '2':
                x = cast_number(input("  Enter X (part):  "))
                y = cast_number(input("  Enter Y (whole): "))
                if y == 0:
                    print("  ✖  Cannot divide by zero.")
                    continue
                result = (float(x) / float(y)) * 100
                print(f"\n  ✔  {x} is  {round(result, 4)}%  of {y}")

            elif choice == '3':
                x = cast_number(input("  Enter FROM value (X): "))
                y = cast_number(input("  Enter TO   value (Y): "))
                if x == 0:
                    print("  ✖  Starting value cannot be zero for % change.")
                    continue
                change = ((float(y) - float(x)) / abs(float(x))) * 100
                direction = "increase" if change >= 0 else "decrease"
                print(f"\n  ✔  {x} → {y}  =  {round(abs(change), 4)}% {direction}  ({'+' if change>=0 else ''}{round(change,4)}%)")

            else:
                print("  ✖  Invalid choice. Enter 1–4.")

        except ValueError as e:
            print(f"  ✖  Type casting error — please enter a valid number. ({e})")


# ─────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────

MAIN_MENU = """
╔══════════════════════════════════════════════════════╗
║                     CALC-X                          ║
║            Python Advanced Calculator               ║
╠══════════════════════════════════════════════════════╣
║  [1]  Basic Arithmetic    ( + - * / % )             ║
║  [2]  Statistics          ( Mean / Median / Mode )  ║
║  [3]  Percentage          ( X% of Y / change )      ║
║  [4]  Exit                                          ║
╚══════════════════════════════════════════════════════╝
"""

def main() -> None:
    print(MAIN_MENU)

    ROUTES = {
        '1': basic_calculator,
        '2': statistics_calculator,
        '3': percentage_calculator,
    }

    while True:
        choice = input("  Select option (1–4): ").strip()

        if choice == '4' or choice.lower() in ('exit', 'quit'):
            print("\n  Goodbye! 👋\n")
            break
        elif choice in ROUTES:
            ROUTES[choice]()
            print(MAIN_MENU)
        else:
            print("  ✖  Invalid option. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
