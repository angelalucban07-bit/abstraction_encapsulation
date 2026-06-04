import time

class Dashboard:

    WIDTH = 54

    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    def __init__(self, car):
        self.car = car

    def box_top(self):
        print("┌" + "─" * self.WIDTH + "┐")

    def box_bottom(self):
        print("└" + "─" * self.WIDTH + "┘")

    def box_line(self, text=""):
        print(f"│{text:<{self.WIDTH}}│")

    def header(self, title):
            print("╔" + "═" * self.WIDTH + "╗")
            print(f"║{title:^{self.WIDTH}}║")
            print("╚" + "═" * self.WIDTH + "╝")

    def show_header(self):
        print(self.CYAN)

        print("╔" + "═" * self.WIDTH + "╗")
        print(f"║{'🚗 CAR SIMULATOR 🚗':^{self.WIDTH}}║")
        print("╠" + "═" * self.WIDTH + "╣")
        print(
            f"║{f'MODEL : {self.car._Car__year_model} {self.car._Car__make}':<{self.WIDTH}}║"
        )
        print(f"║{'STATUS : READY':<{self.WIDTH}}║")
        print("╚" + "═" * self.WIDTH + "╝")

        print(self.RESET)

    def start_engine(self):

        print(self.YELLOW)
        print("\nENGINE STARTING...\n")
        print(self.RESET)

    def show_acceleration(self, speed, stage):
        if stage == 1:
            print(self.GREEN)
            self.header("🚀 ACCELERATION MODE")
            print(self.RESET)

        filled = stage * 4
        bar = "█" * filled + "░" * (20 - filled)

        print(self.GREEN)

        self.box_top()
        self.box_line(f"STAGE {stage}/5")
        self.box_line()
        self.box_line(f"CURRENT SPEED : {speed} MPH")
        self.box_line()
        self.box_line(f"[{bar}]")
        self.box_line()
        self.box_line("ACCELERATING...")
        self.box_bottom()

        print(self.RESET)

    def show_braking(self, speed, stage):
        if stage == 1:
            print(self.RED)
            self.header("🛑 BRAKE MODE")
            print(self.RESET)

        filled = (5 - stage) * 4
        bar = "█" * filled + "░" * (20 - filled)

        print(self.RED)

        self.box_top()
        self.box_line(f"STAGE {stage}/5")
        self.box_line()
        self.box_line(f"CURRENT SPEED : {speed} MPH")
        self.box_line()
        self.box_line(f"[{bar}]")
        self.box_line()
        self.box_line("BRAKING...")
        self.box_bottom()

        print(self.RESET)

    def show_footer(self):
        print(self.CYAN)

        print("╔" + "═" * self.WIDTH + "╗")
        print(f"║{'🏁 DRIVE COMPLETE 🏁':^{self.WIDTH}}║")
        print("╠" + "═" * self.WIDTH + "╣")
        print(f"║{'':<{self.WIDTH}}║")
        print(f"║{'        ______':<{self.WIDTH}}║")
        print(f"║{'   ____/[] [] \\____':<{self.WIDTH}}║")
        print(f"║{f'  |_ {self.car._Car__year_model} {self.car._Car__make} _|':<{self.WIDTH}}║")
        print(f"║{'    O--------------O':<{self.WIDTH}}║")
        print(f"║{'':<{self.WIDTH}}║")
        print("╚" + "═" * self.WIDTH + "╝")

        print(self.RESET)