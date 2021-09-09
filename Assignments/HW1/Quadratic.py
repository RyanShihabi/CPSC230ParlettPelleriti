# using math module for square root function
import math

# prompting and storing values for variables a, b, and c
a,b,c = int(input("a:")), int(input("b:")), int(input("c:"))

# Calculating both sides of the delta for the discriminate
quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
quadratic_n = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)

# printing the calculated root values
print(f"Roots: x={quadratic_p, quadratic_n}")
