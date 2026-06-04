class Dashboard:

    def __init__(self, car):
        self.car = car

    def show_header(self):
        print("=" * 35)
        print("         CAR SIMULATOR")
        print("=" * 35)
        print("Year Model :", 2024)
        print("Make       :", "Toyota")
        print("Initial Speed:", self.car.get_speed(), "mph")

    def show_acceleration(self, count):
        print(f"Step {count}: Speed = {self.car.get_speed()} mph")

    def show_braking(self, count):
        print(f"Step {count}: Speed = {self.car.get_speed()} mph")

    def show_acceleration_header(self):
        print("\n[ ACCELERATING ]")
        print("-" * 35)

    def show_braking_header(self):
        print("\n[ BRAKING ]")
        print("-" * 35)

    def show_footer(self):
        print("\n" + "=" * 35)
        print("      DRIVE COMPLETE")
        print("=" * 35)