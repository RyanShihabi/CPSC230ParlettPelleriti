# importing math for square root
import math

# setting an assumption that the discriminant will be negative
is_discriminate_negative = True
# continue to check is discriminant still negative
while(is_discriminate_negative):
    # prompts for variables a to c
    a,b,c = int(input("a:")), int(input("b:")), int(input("c:"))

    # Using a try catch to detect the square root value error
    try:
        # with no negative discriminant
        is_discriminate_negative = False
        # calculate both positive and negative roots
        quadratic_p = ((-1*b) + math.sqrt(b**2 - 4*a*c))/(2*a)
        quadratic_m = ((-1*b) - math.sqrt(b**2 - 4*a*c))/(2*a)
        # print roots in a formated string
        print(f"Roots: x={quadratic_p, quadratic_m}")
    except ValueError:
        # with a negative discriminant
        is_discriminate_negative = True
        # prompt for negative discriminant
        print("Please enter values that will give a positive discriminant")
