"""abrecko__demo package

This package provides simple calculator functions in the calc module.
The presence of this file makes the directory importable as a package
(e.g. `import abrecko__demo.calc`).
"""

# Re-export common names for convenience
from .calc import plus, minus, multiply, divide, safe_div

__all__ = ["plus", "minus", "multiply", "divide", "safe_div"]
