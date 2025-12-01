"""
Demo script showing how to use the calculator library.

© 2025 Pau Erola, University of Bristol
"""

from calc_lib import add, subtract, multiply, divide, power


print("Calculator Demo")
print("=" * 40)
print("=" * 40)
    
# Subtraction
result = subtract(10, 5)
print(f"10 - 5 = {result}")
    
# Multiplication
result = multiply(10, 5)
print(f"10 × 5 = {result}")
    
# Division
result = divide(10, 5)
print(f"10 ÷ 5 = {result}")

# Power
result = power(25,0.5)
print(f"25 ^ 0.5 = {result}")    

print("=" * 40)
print("=" * 40)
print("Demo completed!")

