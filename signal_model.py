class TrafficSignal:

    def __init__(self, direction, vehicles, timer, color):

        self.direction = direction

        self.vehicles = vehicles

        self.timer = timer

        self.color = color

    def set_green(self):
        self.color = "Green"

    def set_red(self):
        self.color = "Red"

    def set_yellow(self):
        self.color = "Yellow"

    def decrease_timer(self):

        if self.timer > 0:
            self.timer -= 1

    def reset_timer(self, value):

        self.timer = value

    def calculate_dynamic_timer(self):

        if self.vehicles <= 15:
            return 15

        elif self.vehicles <= 30:
            return 25

        elif self.vehicles <= 45:
            return 35

        else:
            return 45