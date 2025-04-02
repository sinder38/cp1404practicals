"""
CP1404/CP5632 Practical
UnreliableCar class test
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar class functionality"""

    good_car = UnreliableCar("Good enough™", 100, 99)
    mid_car = UnreliableCar("60% of the time works every time", 100, 60)
    bad_car = UnreliableCar("S*** Box™", 100, 3)                                                      # The censored word is "scam" of course :)

    print(good_car)
    print(mid_car)
    print(bad_car)

    for i in range(1, 20):
        print(f"Attempting to drive {i}km:")
        print(f"{good_car.name} drove {good_car.drive(i):2}km")
        print(f"{mid_car.name} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name} drove {bad_car.drive(i):2}km")


if __name__ == "__main__":
    main()
