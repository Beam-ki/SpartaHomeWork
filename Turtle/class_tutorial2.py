class Car:
    def __init__(self):
        self.handle = 0
        self.car_type = "normal"

    def turn_left(self):
        self.handle -= 90

    def turn_right(self):
        self.handle += 90

    def show_status(self):
        # print("owner:", self.owner)
        print("핸들 각도: ", self.handle)
        print("car_type:", self.car_type)


class Van(Car):

    def open_back_door(self):
        print("뒷문이 열렸습니다.")


myCar = Car()
myVan = Van()
myVan.open_back_door()
myVan.turn_right()
myVan.show_status()


# myVan.show_status()

# myVan.turn_left()
# myVan.turn_right()