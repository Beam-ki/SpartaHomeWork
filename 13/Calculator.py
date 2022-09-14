# class Calculator(n1,n2):
def plus(n1,n2):
        return n1+n2
def minus(n1,n2):
        return n1-n2
def multiply(n1,n2):
        return n1*n2
def divide(n1,n2):
        return n1/n2
# print("계산기입니다. 두 정수를 입력해주세요. ")

n1,n2=map(int,(input(" 두 정수를 입력해주세요").split()))
print(plus(n1,n2)) # 더한 값
print(minus(n1,n2)) # 뺀 값
print(multiply(n1,n2)) # 곱한 값
print(divide(n1,n2)) # 나눈 값
Answer_Plus =plus(n1,n2)
Answer_Minus =minus(n1,n2)
Answer_Multiply =multiply(n1,n2)
Answer_Divide =divide(n1,n2)