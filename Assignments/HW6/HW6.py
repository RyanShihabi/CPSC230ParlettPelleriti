# Creating class
class Complex:
    # constructor with real and imaginary parameters
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        # print(complex(self.real, self.imaginary))

    # add function with parameters for instance variables and another class object
    def add(self, other):
        # returning the complex values of real and imaginary instance and the other class variables
        return f"{self.real + other.real}+{self.imaginary + other.imaginary}i"

    # multiply function with parameters for instance variables and another class object
    def multiply(self, other):
        return f"{(self.real * other.real) - (self.imaginary * other.imaginary)}+{(self.real * other.imaginary) + (self.imaginary * other.real)}i"

    # sqaure function with parameters for instance variables
    def square(self):
        return f"{(self.real * self.real) - (self.imaginary * self.imaginary)}+{(self.real * self.imaginary) + (self.imaginary * self.real)}i"


def main():
    # declaring two class objects
    c1 = Complex(1, 2)
    c2 = Complex(3, 4)

    # demonstrating add, mulitply, and square functions
    print(c1.add(c2))
    print(c1.multiply(c2))
    print(c1.square())
    print(c2.square())

if __name__ == "__main__":
    main()
