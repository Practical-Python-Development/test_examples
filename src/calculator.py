"""Some function to calculate something."""

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def divide(a: int, b: int) -> float:
    """Divide two integers."""
    if b == 0:
        raise ValueError('Division by zero!')
    return a / b
