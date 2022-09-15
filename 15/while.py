cnt=0
while True:
    a=input()
    cnt+=1
    if a=="exit":
        break

    try:
        print(int(a)*2)
    except ValueError:
        print(f"입력하신 문자는 '{a}' 입니다")
    if cnt>6:
        break
    