from car import Car
import random


class UnreliableCar(Car):
    random_distance = random.uniform(1.0, 100.0)

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_distance = random.uniform(1.0, 100.0)
        if self.reliability >= random_distance:
            distance_driven = super().drive(distance)
            return distance_driven

        else:
            distance = 0
