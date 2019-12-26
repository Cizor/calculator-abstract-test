from calculator import Calculator

class CalculatorImpl(Calculator):

    def div(self, a, b):
        return a / b
    



# Test main
if __name__ == '__main__':
    c = CalculatorImpl()

    # Test line for div here
    print(c.div(4, 2))
