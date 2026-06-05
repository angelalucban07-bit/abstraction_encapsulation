from fan import Fan
from dashboard import Dashboard

def main():

    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    dashboard = Dashboard()

    dashboard.show_header()

    dashboard.display_fan(fan1, 1)
    dashboard.display_fan(fan2, 2)

if __name__ == "__main__":
    main()