import time

class TrafficController:

    def __init__(self):

        self.current_signal = "North"

        self.timer = 40

        self.signals = [
            "North",
            "South",
            "East",
            "West"
        ]

    def next_signal(self):

        current_index = self.signals.index(self.current_signal)

        next_index = (current_index + 1) % len(self.signals)

        self.current_signal = self.signals[next_index]

        if self.current_signal in ["North", "West"]:
            self.timer = 40
        else:
            self.timer = 20

    def countdown(self):

        if self.timer > 0:
            self.timer -= 1
        else:
            self.next_signal()