from Practical8.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Good car", 100, 90)
    another_car = UnreliableCar("Bad car", 100, 5)
    for i in range(1, 5):
        print("{:8} drove {}".format(car.name, car.drive(i)))
        print("{:8} drove {}".format(another_car.name, another_car.drive(i)))
    print(car)
    print(another_car)


main()
