class TrafficController:

    def __init__(self, north, south, east, west):

        self.signals = [
            north,
            south,
            east,
            west
        ]

        self.current = 0

    def get_current_signal(self):

        return self.signals[self.current]

    # def countdown(self):

    #     signal = self.get_current_signal()

    #     signal.decrease_timer()


    def countdown(self):

        signal = self.get_current_signal()

        print("Countdown running")

        signal.decrease_timer()

        if signal.timer <= 0:

            signal.set_red()

            signal.reset_timer(20)

            self.current = (self.current + 1) % 4

            next_signal = self.get_current_signal()

            next_signal.set_green()

            next_signal.reset_timer(40)