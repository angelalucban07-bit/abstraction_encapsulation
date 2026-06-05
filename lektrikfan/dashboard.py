import time

class Dashboard:

    WIDTH = 34
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    WHITE = "\033[97m"
    RESET = "\033[0m"

    def __init__(self):
        pass

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
        print("╔" + "═" * self.WIDTH + "╗")

    def middle(self):
        print("╠" + "═" * self.WIDTH + "╣")

    def bottom(self):
        print("╚" + "═" * self.WIDTH + "╝" + self.RESET)

    def line(self, text=""):
        print(f"║ {text:<{self.WIDTH - 2}} ║")

    def show_header(self):

        self.top()
        print(self.MAGENTA, end="")
        self.line("🌪️ ELEKTRIKFAN 🌪️")
        self.bottom()
        print(self.RESET)
        print()

        time.sleep(1)

    def display_fan(self, fan, number):

        status = "ON" if fan.get_on() else "OFF"

        if fan.get_color().lower() == "yellow":
            box_color = self.YELLOW
        elif fan.get_color().lower() == "blue":
            box_color = self.BLUE
        else:
            box_color = self.WHITE

        print(box_color, end="")

        self.top()
        self.line(f"FAN #{number}")
        self.middle()
        self.line(f"Speed : {self.speed_name(fan.get_speed())}")
        self.line(f"Radius: {fan.get_radius()}")
        self.line(f"Color : {fan.get_color().upper()}")
        self.line(f"Status: {status}")
        self.bottom()

        print(self.RESET)
        print()
        time.sleep(0.7)
