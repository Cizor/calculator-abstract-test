from calculator import Calculator

class CalculatorImpl(Calculator):

    def sum(self, a, b):
        return a + b




# Test main
if __name__ == '__main__':
    c = CalculatorImpl()
    
    # Testing sum here
    print(c.sum(6, 7))
