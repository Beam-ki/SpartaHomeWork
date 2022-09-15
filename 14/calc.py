class Calc():
    def set_number(self,number1,number2):
        self.number1=number1
        self.number2=number2
    def plus(self):
        return number1+number2
    def minus(self):
        return number1-number2
    def multiply(self):
        return number1*number2
    def divide(self):
        try: 
            return number1/number2
        except ValueError:
            print("0으로 나눌수 없습니다.")
        except ZeroDivisionError:
            print("0으로 나눌수 없습니다.")
calc = Calc()
while True:
    try:
        # number1 = int(input())
        # number2 = int(input())
        number1,number2=[int(x) for x in input().split(" ")]

    except ValueError:
            print("숫자를 입력해주세요.")

    print(calc.plus()) # 더한 값
    print(calc.minus()) # 뺀 값
    print(calc.multiply()) # 곱한 값
    print(calc.divide()) # 나눈 값

# if number2==0
    #print("0으로 나눌수 없습니다.")
# try: int(number1) and int(number2)
#   except ValueError:
#  print("숫자를 입력해주세요.")
