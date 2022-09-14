class Calc():
    def set_number(number1,number2):
        number1=number1
        number2=number2
    def plus(self):
        return number1+number2
    def minus(self):
        return number1-number2
    def multiply(self):
        return number1*number2
    def divide(self):
        try: 
            number2==0
            print("0으로 나눌수 없습니다.")
        except:
            return
calc = Calc()
try:
    number1 = int(input())
    number2 = int(input())

    int(number1) and int(number2)
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
