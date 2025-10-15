from scheduler import Scheduler
import heapq

class LRSF(Scheduler):
    def schedule(self):
        for p in self.processes:
            p.reset()

        procs = sorted(self.processes, key=lambda p: p.arrival)
        n, i, time = len(procs), 0, 0
        schedule, heap = [], []

        while i < n or heap:
            while i < n and procs[i].arrival <= time:
                heapq.heappush(heap, (procs[i].remaining, procs[i]))
                i += 1

            if not heap:
                time = procs[i].arrival
                continue

            rt, p = heapq.heappop(heap)
            run_time = 1
            schedule.append((p.pid, time, run_time))
            time += run_time
            p.remaining -= run_time
            if p.remaining > 0:
                heapq.heappush(heap, (p.remaining, p))

        return schedule
