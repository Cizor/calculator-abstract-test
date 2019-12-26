from calculator import Calculator

class CalculatorImpl(Calculator):

    def mul(self, a, b):
        return a * b



# Test main
if __name__ == '__main__':
    c = CalculatorImpl()

    # Test line for mul here
    print(c.mul(3, 6))
