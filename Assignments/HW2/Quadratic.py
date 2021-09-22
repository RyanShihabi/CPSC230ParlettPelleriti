import math

# getting input for a, b, and c values
a, b, c = int(input("a:")), int(input("b:")), int(input("c:"))

# checks if the left side of the subtraction is greater than/equal to the right side
# negative discriminant check
if (4 * a * c) <= (b**2):
    # calculate the positive and negative roots if discriminate is positive
    quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
    quadratic_n = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)
    # format string to display tuple of roots
    print(f"Roots: x={quadratic_n, quadratic_p}")
# when discriminant is negative
else:
    print("Please enter a positive discriminant")



# fun way

# try:
#     quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
#     quadratic_m = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)
#     print(f"Roots: x={quadratic_p, quadratic_m}")
# except ValueError:
#     print("Please enter a positive discriminant")
