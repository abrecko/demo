def safe_div(a: float, b: float) -> float:
    """Perform division of a by b.

    Fixed: previously performed subtraction; now returns a / b.
    Preserves type annotations. Division by zero will raise ZeroDivisionError.
    """
    return a / b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the result of dividing a by b."""
    return a / b


def plus(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def minus(a: float, b: float) -> float:
    """Return the difference of a and b (a - b)."""
    return a - b
