from calculator import Calculator

class CalculatorImpl(Calculator):

    def sub(self, a, b):
        return a - b
    
    def sum(self, a, b):
        return a + b

      
# Test main
if __name__ == '__main__':
    c = CalculatorImpl()

    #Test line for sub here
    c.sub(8, 3)
    
    # Testing sum here
    print(c.sum(6, 7))
