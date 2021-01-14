from Practical8.car import Car
import random


class UnreliableCar(Car):
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        number = (random.randint(0, 100))
        if number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
