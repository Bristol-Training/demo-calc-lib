"""
A simple calculator library for basic arithmetic operations.

© 2025 Pau Erola, University of Bristol


"""

def add(a, b):
    """Add two numbers together."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power_function(a,b):
    """THE NEW FUNCTION... Power a^b"""
    return a**b

def calculate_total(items):
    total = sum(item.price * 1.2 for item in items)  # With 20% tax
    return total


