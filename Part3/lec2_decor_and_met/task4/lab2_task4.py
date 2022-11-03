from lab3_task1 import G
from lab3_task1 import c
class Planet:
    square = 0
    def  __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        Planet.square = (Planet.square + 1) ** 2

    @staticmethod
    def diameter(radius):
        return radius * 2
    
    @classmethod
    def number(cls):
      return cls.square

    @property
    def grav_radius(self):
        return 2 * G * self.mass / (c ** 2)

print(Planet.diameter(10000))
print(Planet.number())
planet1 = Planet(6371 * 1000, 6 * 10 ** 24)
planet2 = Planet(25 * 10 ** 7, 2 * 10 ** 15)
print(Planet.number())
print(f"Гравитационный радиус чёрной дыры подобной массы равен {planet2.grav_radius} м")
