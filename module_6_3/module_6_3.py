from random import randint


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, cords=None):
        if cords is None:
            self.cords = [0, 0, 0]
        else:
            self.cords = cords
        self.speed = speed

    def move(self, dx, dy, dz):
        if self.cords[2] + dz * self.speed >= 0:
            self.cords[0] += dx * self.speed
            self.cords[1] += dy * self.speed
            self.cords[2] += dz * self.speed
        else:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f"X: {self.cords[0]}, Y: {self.cords[1]}, Z: {self.cords[2]}")

    def attack(self):
        print(
            "Sorry, i'm peaceful :)"
            if self._DEGREE_OF_DANGER < 5
            else "Be careful, i'm attacking you 0_0"
        )

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("^__^")


class Bird(Animal):
    def __init__(self, speed, cords=None):
        super().__init__(speed, cords)
        self.beak = True

    def lay_eggs(self):
        print(f"Here are(is) {randint(1, 4)} eggs for you")


class AquaticAnimal(Animal):
    def __init__(self, speed, cords=None):
        super().__init__(speed, cords)
        self._DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        new_z = int(self.cords[2] - dz * (self.speed / 2))
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self.cords[2] = new_z


class PoisonousAnimal(Animal):
    
    def __init__(self, speed, cords=None):
        super().__init__(speed, cords)
        self._DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed, cords=None):
        super().__init__(speed, cords)
        self.sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

