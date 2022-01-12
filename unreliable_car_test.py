
from unreliable_car import UnreliableCar


def main():
    fastest_car = UnreliableCar("Fastest car", 100, 99)
    print(f"{fastest_car.name} drove {fastest_car.drive(99)}km")
    print(fastest_car)

main()