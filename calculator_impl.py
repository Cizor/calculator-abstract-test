from calculator import Calculator

class CalculatorImpl(Calculator):

    def div(self, a, b):
        return a / b
    
    def mul(self, a, b):
        return a * b

    def sub(self, a, b):
        return a - b
    
    def sum(self, a, b):
        return a + b

      
# Test main
if __name__ == '__main__':
    c = CalculatorImpl()

    # Test line for div here
    print(c.div(4, 2))

    # Test line for mul here
    print(c.mul(3, 6))

    #Test line for sub here
    c.sub(8, 3)
    
    # Testing sum here
    print(c.sum(6, 7))
