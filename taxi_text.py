from taxi import Taxi


def main():

    new_texi = Taxi("Prius 1", 100)
    new_texi.drive(40)
    print(f"odometer is {new_texi.odometer}")
    new_texi = Taxi("Prius 1", 100)
    print(f"New taxi name is {new_texi.name}, {new_texi.fuel} units of fuel and price of ${new_texi.price_per_km}km")
    new_texi.start_fare()
    new_texi.drive(100)
    print(f"New taxi name is {new_texi.name}, {new_texi.fuel} units of fuel and price of ${new_texi.price_per_km}km, "
          f"fare is {new_texi.get_fare(Taxi.price_per_km)}")


main()
