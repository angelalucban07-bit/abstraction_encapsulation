class Dashboard:

    WIDTH = 34
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    def __init__(self):
        pass

    def show_header(self):
        print("=" * 30)
        print("      FAN STATUS")
        print("=" * 30)

    def speed_name(self, speed):

        if speed == 1:
            return "SLOW"

        elif speed == 2:
            return "MEDIUM"

        else:
            return "FAST"

    def line(self, text):
        print(f"║ {text:<{self.WIDTH-2}} ║")

    def top(self):
        print(self.CYAN + "╔" + "═" * self.WIDTH + "╗")

    def middle(self):
        print("╠" + "═" * self.WIDTH + "╣")

    def bottom(self):
        print("╚" + "═" * self.WIDTH + "╝" + self.RESET)

    def line(self, text=""):
        print(f"║ {text:<{self.WIDTH - 2}} ║")

    def show_header(self):

        self.top()
        print(self.MAGENTA)
        self.line("🌪️ ELEKTRIKFAN 🌪️")
        print(self.CYAN)
        self.bottom()

        print()

    def display_fan(self, fan, number):

        status = "ON" if fan.get_on() else "OFF"

        self.top()
        print(self.YELLOW)
        self.line(f"FAN #{number}")
        print(self.CYAN)
        self.line(f"Speed : {self.speed_name(fan.get_speed())}")
        self.line(f"Radius: {fan.get_radius()}")
        self.line(f"Color : {fan.get_color().upper()}")

        if fan.get_on():
            print(self.GREEN)
        else:
            print(self.RED)

        self.line(f"Status: {status}")
        print(self.CYAN)
        self.bottom()

        print()

    def show_footer(self):

        print(self.GREEN)
        print("✓CHECK COMPLETE")
        print(self.RESET)