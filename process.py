class Process:
    def __init__(self, pid, burst, arrival=0):
        self.pid = pid
        self.burst = burst
        self.arrival = arrival
        self.remaining = burst

    def reset(self):
        """Reset remaining time (for reruns)."""
        self.remaining = self.burst

    def __repr__(self):
        return f"{self.pid}(BT={self.burst}, AT={self.arrival})"
