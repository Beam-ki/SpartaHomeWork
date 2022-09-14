def area(n):
    if  n==1:
        rad=int(input("원의 반지름을 입력해주세요"))
        area=rad**2*3.14
        print("반지름 길이가 {}인 원의 넓이는 약 {:2f}입니다.".format(rad,area))
    elif n==2:
        height=int(input("삼각형의 높이를 입력해주세요"))
        length=int(input("삼각형의 밑변 길이를 입력해주세요"))
        area=height*length*1/2
        print("높이가 {},밑변의 길이가 {}인 삼각형의 넓이는 {}입니다".format(height,length,area))

    elif n==3:
        width=int(input("직사각형 가로길이를 입력해주세요"))
        length1=int(input("직사각형 세로길이를 입력해주세요"))
        area=width*length1
        print("가로가 {} ,세로가 {}인 직사각형의 넓이는 {} 입니다".format(width,length1,area))
    elif n==4:
        squere = int(input("정사각형 한 변의 길이를 입력해주세요"))
        area=squere**2
        print("한변의 길이가 {} 인 정사각형의 넓이는 {} 입니다".format(squere,area))

print("==========도형목록==========\n"
      "1.원\n"
      "2.삼각형\n"
      "3.직사각형\n"
      "4.정사각형\n"
      "===========================\n")
area(int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해주세요")))