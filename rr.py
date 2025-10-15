from scheduler import Scheduler
from collections import deque

class RoundRobin(Scheduler):
    def __init__(self, processes, quantum=2):
        super().__init__(processes)
        self.quantum = quantum

    def schedule(self):
        for p in self.processes:
            p.reset()

        queue = deque(self.processes)
        time, schedule = 0, []

        while queue:
            p = queue.popleft()
            run_time = min(p.remaining, self.quantum)
            schedule.append((p.pid, time, run_time))
            time += run_time
            p.remaining -= run_time
            if p.remaining > 0:
                queue.append(p)

        return schedule
