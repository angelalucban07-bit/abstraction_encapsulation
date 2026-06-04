from car import Car
from dashboard import Dashboard


def main():

    my_car = Car(2024, "Toyota")
    dashboard = Dashboard(my_car)

    dashboard.show_header()

    dashboard.start_engine()

    for count in range(1, 6):
        my_car.accelerate()
        dashboard.show_acceleration(my_car.get_speed(), count)

    for count in range(1, 6):
        car.brake()
        dashboard.show_braking(my_car.get_speed(), count)

    dashboard.show_footer()


if __name__ == "__main__":
    main()