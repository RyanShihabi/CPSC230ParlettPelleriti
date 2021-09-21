# importing math for square root
import math

# grabbing inputs for a, b, and c
a, b, c = int(input("a:")), int(input("b:")), int(input("c:"))

# continue to check if discriminant is still negative
while((4 * a * c) > (b**2)):
    # prmompt user of mistake
    print("Please enter values that will return a positive discriminant")

    # prompts for variables a to c
    a,b,c = int(input("a:")), int(input("b:")), int(input("c:"))

# calculate both positive and negative roots
quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
quadratic_m = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)
# print roots in a formated string
print(f"Roots: x={quadratic_p, quadratic_m}")
