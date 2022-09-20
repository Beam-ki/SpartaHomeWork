class Person:
    name="안범기"  
    gender ="male"
    age = 20
    

    def __init__(self,name):
        print("이닛 메소드 안 입니다.")
        self.name=name


person1 = Person("김규현")
person2= Person("zxc")
print(person1.name)
person2.name ="안범기123"
person2.gender ="asdgg"
print(person2.name)