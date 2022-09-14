from random import randint
import time
from datetime import datetime, timedelta
import sys
# Base = set()
# a=int(input())
# for i in range(a):
#     result=[]
#     Base =set()
#     while len(Base)<a:
#         Base.add(random.randint(0,9))
#         print(Base)
#     first = list(map(int,input().split()))
#     if sorted(first) == sorted(Base):
#         print("스트라이크")
#     else:
#         print("끝")
start_time = time.time() # 현재 시간 저장

time.sleep(1) # 1초간 대기

end_time = time.time()
now = datetime.now()
string_datetime = datetime.strftime(now, "%y/%m/%d %H:%M:%S")
a=int(input())
def BaseBall():
    Base = []
    i = 0
    new_Base =0
    while i <a :
        new_Base=randint(0,9)
        if new_Base not in Base:
            Base.append(new_Base)
            i +=1
    print(f"0과 9 사이의 서로 다른 숫자 {a}개를 랜덤한 순서로 뽑았습니다.\n")
    return Base

def inputs():
    print(f"숫자 {a}개를 입력하세요")
    i=0
    new_inputs=[]
    while i<a:
        inputs_number = int(input("{}번쨰 숫자를 입력하세요 ".format(i+1)))
        if inputs_number > 9:
            print("다시입력")
            continue
        if inputs_number in new_inputs:
            print("중복되는 숫자입니다")
        else:
            new_inputs.append(inputs_number)
            i +=1
    return new_inputs

def get_score(input,answer):
    strike_count=0
    ball_count=0
    i=0

    while i < len(input):
        if input[i] == answer[i]:
            strike_count += 1
            i += 1
        elif input[i] in answer:
            ball_count += 1
            i +=1
        else:
            i+=1
    return strike_count,ball_count

tAnswer =BaseBall()
ttry=0
while 1:
    tinput = inputs()
    strike,ball = get_score(tinput,tAnswer)
    print("{}s {}b".format(strike,ball))

    if strike == a :
        ttry +=1
        break
    else:
        ttry +=1
while True:
    print("게임을 계속 하시겠습니까?(Y/N) : ", end='')
    answer = input()
    if answer == "y" or answer == "Y":
        game()
    elif answer == "n" or answer == "N":
        print("게임을 종료합니다.")
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(ttry))
print(f"코드 실행 시간 : {end_time-start_time:.5f}")
print("현재시각은 "+string_datetime+"입니다")


### 요구조건

# - 프로그램이 시작되면 슷자야구 게임을 몇 자리 숫자로 할 건지 입력 받아 주세요
#     - 3을 입력할 경우 해당 숫자야구 게임은 3자릿수로 진행, 최대 10자리 
    # -완료-

# - 첫 번째 입력을 받은 자릿수 만큼 후 파이썬으로 중복 없는 랜덤한 수를 생성해 주세요
        # -완료-
# - 사용자가 숫자를 입력 했을 때 숫자야구 게임의 규칙에 맞게 ball / out count를 출력해 주세요
        # 완료
# - 사용자가 정답을 맞춘 경우 아래 항목들을 출력해 주세요
#     - 사용자가 정답을 맞추기까지 입력 한 횟수
    # -완료
#     - 사용자가 게임을 시작해서 정답을 맞추기까지 소요된 시간
    # 완료
#     - 정답을 맞춘 시점의 날짜/시간
    #  완료

# - 게임을 진행하던 도중, “exit”을 입력할 경우 프로그램을 종료해 주세요
#    어디다가 넣어야할지모르겠음