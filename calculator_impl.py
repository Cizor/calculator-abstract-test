from calculator import Calculator

class CalculatorImpl(Calculator):

    def sub(self, a, b):
        return a - b



# Test main
if __name__ == '__main__':
    c = CalculatorImpl()

    #Test line for sub here
    c.sub(8, 3)
