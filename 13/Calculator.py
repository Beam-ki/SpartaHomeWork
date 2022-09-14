class Calc():
    def set_number(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def plus(self):
        return self.number1+self.number2
    def minus(self):
        return self.number1-self.number2
    def multiply(self):
        return self.number1*self.number2
    def divide(self):
        return self.number1/self.number2
calc = Calc()

calc.set_number(20, 10)


print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiply()) # 곱한 값
print(calc.divide()) # 나눈 값
