import random

possible_valuse= ['가위','바위','보']
computer_number = random.randint(0,2)
while True:
    player_value = input("가위,바위,보 중에서 내주세요")

    if player_value in possible_valuse:
        break
    else:
        print("제대로 입력하세요")
while True:
    print(player_value,"를 선택했습니다")
    print("게임 진행")
    random_value= possible_valuse[computer_number]
    print('컴퓨터는 ',random_value,'선택하였습니다')

    if random_value == player_value:
        print('비겼습니다')
    elif (random_value == '바위' and player_value =='가위') or (random_value == '가위' and player_value =='보') or (random_value == '보' and player_value =='묵')   :
        print('컴퓨터가 이겼습니다.')
    else:
        print('플레이어가 이겼습니다')
    break
    