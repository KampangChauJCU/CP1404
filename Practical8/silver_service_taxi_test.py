from Practical8.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(taxi)
    taxi.get_fare()
    taxi.drive(10)
    print("Cost of fare = ${:.2f}".format(taxi.get_fare()))

    taxi = SilverServiceTaxi("SilverServiceTaxi", 200, 2)
    print(taxi)
    taxi.get_fare()
    taxi.drive(18)
    print("Cost of fare = ${:.2f}".format(taxi.get_fare()))


main()
