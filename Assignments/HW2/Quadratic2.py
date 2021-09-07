import math

is_discriminate_negative = True
while(is_discriminate_negative):
    a,b,c = int(input("a:")), int(input("b:")), int(input("c:"))

    try:
        is_discriminate_negative = False
        quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
        quadratic_m = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)
        print(f"Postive Roots: x={quadratic_p, quadratic_m}")
    except ValueError:
        is_discriminate_negative = True
        print("Please enter values that will give a positive discriminant")
