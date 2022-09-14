import random
import time

import datetime
# length= 5
# number_list = [x for x in range(10)]
# # print(number_list)
# # random_number = number_list.pop(5)
# random_numbers = []

# for _ in range(length):
#     number_list.pop(random_numbers.randrange(0.len(number_list)))

# print(number_list)
# print(random_numbers)

#case3
def main():
    length= 5
    random_numbers= set()
    while len(random_numbers) < length:
        random_numbers.add(random.randint(0,9))

    random_numbers = list(random_numbers)
    random.shuffle(random_numbers)
    print(random_numbers)

    start_time =time.time()
    try_count =0


while Ture:
    input_number =input("값을 입력해주세요")
    try_count += 1
    ball_count =0
    out_count =0
    strike_count = 0

for i, v in enumerate(input_number):
    v= int(v)
    print(i,v)
    if v not in random_numbers: #포함되어있지않는경우
        out_count +=1
        
    else:
        if random_numbers[i] ==v:
            strike_count += 1
        else:
            ball_count +=1

    if strike_count == length:
        print("#################")
        print("정답입니다!")
        print(f'소요시간 : {time.time()-start.time}')
        print(f'소요시간 : {time.time()-start.time}')
        print(f'소요시간 : {time.time()-start.time}')