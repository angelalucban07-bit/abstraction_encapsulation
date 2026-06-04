class Dashboard:

    def __init__(self):
        pass

    def show_header(self):
        print("=" * 30)
        print("      FAN STATUS")
        print("=" * 30)

    def display_fan(self, fan):

        print("Speed :", fan.get_speed())
        print("Radius:", fan.get_radius())
        print("Color :", fan.get_color())
        print("On    :", fan.get_on())