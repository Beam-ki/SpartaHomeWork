class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
        # self.area = radius * radius * self.pi

    def getCircumference(self):
        return self.radius * self.pi * 2
        
    def getarea(self):
        return  self.radius * self.radius * self.pi


c = Circle(6)

print("반지름은 : ", c.radius)
print("넓이는 : ", c.getarea())
print("둘레는 : ", c.getCircumference())


# getArea라는 메소드를 클래스 안에서 만들고, 6번줄은 지워주세요
# 6번줄의 기능을 getArea라는 메소드에서 할수있게끔 로직을 만들어주시고
# 15번줄도 수정해서 getArea라는 메소드를 통해서 넓이를 print 할 수 있게 수정해주세요!