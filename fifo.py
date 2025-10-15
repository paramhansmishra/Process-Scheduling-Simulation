from scheduler import Scheduler

class FIFO(Scheduler):
    def schedule(self):
        procs = sorted(self.processes, key=lambda p: p.arrival)
        time, schedule = 0, []
        for p in procs:
            if time < p.arrival:
                time = p.arrival
            schedule.append((p.pid, time, p.burst))
            time += p.burst
        return schedule
