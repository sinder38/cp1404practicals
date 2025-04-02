"""
CP1404/CP5632 Practical
SilverServiceTaxi class test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi"""


    taxi = SilverServiceTaxi("0-Star Rated", 200, 4)
    taxi.drive(20)
    assert taxi.get_fare() == 102.9, f"Expected fare 102.9 got {taxi.get_fare()}"

    # Lobster car ain't cheap
    taxi = SilverServiceTaxi("Lobster car", 100, 99)
    taxi.drive(20)
    assert taxi.get_fare() == 2439.9, f"Expected fare 2439.9, got {taxi.get_fare()}"

    print("All tests passed!")

if __name__ == "__main__":
    main()