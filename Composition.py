class engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.Engine = engine(horse_power)
        self.wheel = [Wheel(wheel_size)]

    def display_Car(self):
        return f"{self.make} {self.model} {self.Engine.horse_power}(hp)"

Car1 = car(make="Arisu", model="Yonder", horse_power=350, wheel_size=30)

print (Car1.display_Car())
