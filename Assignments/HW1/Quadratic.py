import math
a,b,c = int(input("a:")), int(input("b:")), int(input("c:"))

quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
quadratic_m = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)

print(f"Postive Roots: x={quadratic_p, quadratic_m}")
