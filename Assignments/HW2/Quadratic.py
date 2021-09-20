import math
a,b,c = int(input("a:")), int(input("b:")), int(input("c:"))

if (4 * a * c) <= (b**2):
    quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
    quadratic_m = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)
    print(f"Roots: x={quadratic_p, quadratic_m}")
else:
    print("Please enter a positive discriminant")

# fun way

# try:
#     quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
#     quadratic_m = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)
#     print(f"Roots: x={quadratic_p, quadratic_m}")
# except ValueError:
#     print("Please enter a positive discriminant")
