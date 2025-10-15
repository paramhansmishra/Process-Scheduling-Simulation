from abc import ABC, abstractmethod

class Scheduler(ABC):
    def __init__(self, processes):
        # clone processes so we don’t overwrite originals
        self.processes = [p for p in processes]

    @abstractmethod
    def schedule(self):
        """
        Must return a list of tuples:
        [(pid, start_time, duration), ...]
        """
        pass
