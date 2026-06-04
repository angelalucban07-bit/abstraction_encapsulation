from car import Car
from dashboard import Dashboard


def main():

    car = Car(2024, "Toyota")
    dashboard = Dashboard(car)

    dashboard.show_header()

    dashboard.show_acceleration_header()

    for count in range(1, 6):
        car.accelerate()
        dashboard.show_acceleration(count)

    dashboard.show_braking_header()

    for count in range(1, 6):
        car.brake()
        dashboard.show_braking(count)

    dashboard.show_footer()


if __name__ == "__main__":
    main()