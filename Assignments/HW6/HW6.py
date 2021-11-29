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
        return complex(self.real, self.imaginary) + complex(other.real, other.imaginary)

    # multiply function with parameters for instance variables and another class object
    def multiply(self, other):
        return complex(self.real, self.imaginary) * complex(other.real, other.imaginary)

    # sqaure function with parameters for instance variables
    def square(self):
        return complex(self.real, self.imaginary)**2


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
