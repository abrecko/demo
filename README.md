# abrecko__demo

A simple Python calculator library providing basic arithmetic operations with type annotations.

## Overview

This repository contains a lightweight calculator module (`calc.py`) that implements fundamental mathematical operations. The library is designed with simplicity and type safety in mind, using Python's type hints for better code clarity and IDE support.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division
- **Type Annotations**: Full type hint support for better code quality
- **Safe Division**: Dedicated safe division function with clear documentation
- **Simple API**: Easy-to-use functions with intuitive naming

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd abrecko__demo
```

## Module: calc.py

The `calc.py` module provides the following functions:

### safe_div(a: float, b: float) -> float

Perform division of a by b.

**Parameters:**
- `a` (float): The dividend
- `b` (float): The divisor

**Returns:**
- float: The result of a / b

**Raises:**
- `ZeroDivisionError`: If b is zero

**Example:**
```python
from calc import safe_div

result = safe_div(10, 2)
print(result)  # Output: 5.0
```

### multiply(a: float, b: float) -> float

Return the product of a and b.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:**
- float: The product of a and b

**Example:**
```python
from calc import multiply

result = multiply(10, 2)
print(result)  # Output: 20
```

### divide(a: float, b: float) -> float

Return the result of dividing a by b.

**Parameters:**
- `a` (float): The dividend
- `b` (float): The divisor

**Returns:**
- float: The result of a / b

**Example:**
```python
from calc import divide

result = divide(10, 2)
print(result)  # Output: 5.0
```

### plus(a: float, b: float) -> float

Return the sum of a and b.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number

**Returns:**
- float: The sum of a and b

**Example:**
```python
from calc import plus

result = plus(10, 2)
print(result)  # Output: 12
```

### minus(a: float, b: float) -> float

Return the difference of a and b (a - b).

**Parameters:**
- `a` (float): The number to subtract from
- `b` (float): The number to subtract

**Returns:**
- float: The difference of a and b

**Example:**
```python
from calc import minus

result = minus(10, 2)
print(result)  # Output: 8
```

## Usage Examples

### Basic Usage

```python
from calc import multiply, divide, plus, minus, safe_div

# Multiplication
result = multiply(10, 2)
print(f"multiply(10, 2) = {result}")  # Output: multiply(10, 2) = 20

# Division
result = divide(10, 2)
print(f"divide(10, 2) = {result}")  # Output: divide(10, 2) = 5.0

# Addition
result = plus(10, 2)
print(f"plus(10, 2) = {result}")  # Output: plus(10, 2) = 12

# Subtraction
result = minus(10, 2)
print(f"minus(10, 2) = {result}")  # Output: minus(10, 2) = 8

# Safe Division
result = safe_div(10, 2)
print(f"safe_div(10, 2) = {result}")  # Output: safe_div(10, 2) = 5.0
```

### Running the Examples

The repository includes an `examples.py` file that demonstrates all available functions:

```bash
python examples.py
```

**Output:**
```
multiply(10, 2) = 20
divide(10, 2) = 5.0
plus(10, 2) = 12
minus(10, 2) = 8
safe_div(10, 2) = 5.0
```

## File Structure

```
abrecko__demo/
├── calc.py          # Main calculator module with arithmetic functions
├── examples.py      # Example usage of all calculator functions
└── README.md        # This file
```

## API Reference

### calc.py

| Function | Parameters | Returns | Description |
|----------|-----------|---------|-------------|
| `safe_div(a, b)` | a: float, b: float | float | Safely divides a by b |
| `multiply(a, b)` | a: float, b: float | float | Multiplies a and b |
| `divide(a, b)` | a: float, b: float | float | Divides a by b |
| `plus(a, b)` | a: float, b: float | float | Adds a and b |
| `minus(a, b)` | a: float, b: float | float | Subtracts b from a |

## Code Examples

### Example 1: Simple Calculator

```python
from calc import plus, minus, multiply, divide

def calculate(a, b, operation):
    """Perform calculation based on operation."""
    if operation == '+':
        return plus(a, b)
    elif operation == '-':
        return minus(a, b)
    elif operation == '*':
        return multiply(a, b)
    elif operation == '/':
        return divide(a, b)
    else:
        raise ValueError(f"Unknown operation: {operation}")

# Usage
print(calculate(10, 5, '+'))   # Output: 15
print(calculate(10, 5, '-'))   # Output: 5
print(calculate(10, 5, '*'))   # Output: 50
print(calculate(10, 5, '/'))   # Output: 2.0
```

### Example 2: Using with Error Handling

```python
from calc import safe_div

def safe_calculate(a, b):
    """Safely divide two numbers with error handling."""
    try:
        result = safe_div(a, b)
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Usage
print(safe_calculate(10, 2))   # Output: Result: 5.0
print(safe_calculate(10, 0))   # Output: Error: Cannot divide by zero
```

### Example 3: Chaining Operations

```python
from calc import plus, multiply, minus

# Calculate: (10 + 5) * 2 - 3
step1 = plus(10, 5)        # 15
step2 = multiply(step1, 2) # 30
result = minus(step2, 3)   # 27

print(f"Result: {result}")  # Output: Result: 27
```

## Requirements

- Python 3.6 or higher (for type annotations support)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Alexander Brecko

## Version History

- **Latest**: Added safe_div function with proper division implementation
- **Initial Release**: Basic arithmetic operations (multiply, divide, plus, minus)
