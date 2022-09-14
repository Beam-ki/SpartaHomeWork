import calculator
a,b=map(float,input().split())
Answer_Plus =calculator.plus(a,b)
Answer_Minus =calculator.minus(a,b)
Answer_Multiply =calculator.multiply(a,b)
Answer_Divide =calculator.divide(a,b)

Answer_Plus_Str=str(Answer_Plus)        #문자열과 같이 출력하기 위해서 float를 str로 형변환
Answer_Minus_Str=str(Answer_Minus)
Answer_Multiply_Str=str(Answer_Multiply)
Answer_Divide_Str=str(Answer_Divide)


print("a+b : " + Answer_Plus_Str)
print("a-b :"+ Answer_Minus_Str)
print("a*b :"+ Answer_Multiply_Str)
print("a/b :"+ Answer_Divide_Str)
# a b 엔터하게되면 더하기,빼기,곱하기,나누기 순서대로 출력 


# num1, num2 = map(int, input().split())
# operator = input()

# if operator == '+':
#     result = calculator.plus(num1, num2)
#     print(result)
# elif operator == '-':
#     result = calculator.minus(num1, num2)
#     print(result)
# elif operator == '*':
#     result = calculator.multiply(num1, num2)
#     print(result)
# elif operator == '/':
#     result = calculator.divide(num1, num2)
#     print(result)