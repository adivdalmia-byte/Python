class FamilyVehicle:
    def __init__(self, colour, brand):
        self.colour=colour
        self.brand=brand
    def show_traits(self):
        print("colour:", self.colour)
        print("brand:", self.brand)

class Kidcar(FamilyVehicle):
    def __init__(self, colour,brand,length_cm):
        self.length_cm = length_cm
        self.colour=colour
        super(). __init__(brand, colour)

    def show_traits(self):
        print("length:", self.length_cm)
        print("brand:", self.brand)
        print("length:", self.length_cm, "cm")
        super().show_traits()

    def favorite_speed(self,speed):
        print(self.brand, "favorite speed is", speed)

car = Kidcar("tesla", "blue", 200)
car.show_traits()
car.favorite_speed("180")

print(" Is Kidcar a subclass of FamilyVehicle?", issubclass(Kidcar, FamilyVehicle))
        