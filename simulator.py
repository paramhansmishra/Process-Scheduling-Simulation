import tkinter as tk
import time
import threading

from process import Process
from fifo import FIFO
from rr import RoundRobin
from lrsf import LRSF

class SchedulerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Scheduling Simulator")

        # Title label (fancy and readable)
        self.title_label = tk.Label(
            root,
            text="⚙️ Process Scheduling Simulator ⚙️",
            font=("Helvetica", 20, "bold"),
            bg="#283593",   # Indigo background
            fg="white",     # White text
            padx=20,
            pady=10
        )
        self.title_label.pack(fill="x", pady=10)

        # Canvas for drawing
        self.canvas = tk.Canvas(root, width=1100, height=400, bg="white")
        self.canvas.pack(pady=10)

        # Buttons
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        tk.Button(self.btn_frame, text="Run FIFO", command=self.run_fifo,
                  font=("Arial", 12), bg="#64b5f6").pack(side=tk.LEFT, padx=10)

        tk.Button(self.btn_frame, text="Run RR", command=self.run_rr,
                  font=("Arial", 12), bg="#81c784").pack(side=tk.LEFT, padx=10)

        tk.Button(self.btn_frame, text="Run LRSF", command=self.run_lrsf,
                  font=("Arial", 12), bg="#ffb74d").pack(side=tk.LEFT, padx=10)

        # Processes
        self.processes = [
            Process("P1", 5, 0),
            Process("P2", 3, 1),
            Process("P3", 8, 2),
            Process("P4", 6, 3),
        ]

    # (rest of the code stays the same: draw_block, animate, run_fifo, run_rr, run_lrsf)
    def draw_block(self, pid, start, duration, x, color):
        """Draws a process block with its time duration and Burst Time above."""
        y = 120
        width = duration * 40  # scale burst/duration visually

        # Process rectangle
        rect = self.canvas.create_rectangle(x, y, x + width, y + 40, fill=color)

        # Process ID inside block
        text = self.canvas.create_text(x + width / 2, y + 20, text=pid, fill="white", font=("Arial", 12, "bold"))

        # Burst Time above the block
        self.canvas.create_text(x + width / 2, y - 10, text=f"BT: {duration}", 
                                fill="darkred", font=("Arial", 10, "italic"))

        # Time labels below
        self.canvas.create_text(x, y + 60, text=str(start), fill="black")
        self.canvas.create_text(x + width, y + 60, text=str(start + duration), fill="black")

        return rect, text, x + width

    def animate(self, schedule):
        """Accumulates blocks like a Gantt chart with Start and End symbols."""
        x = 60  # leave space for 'Start'
        y = 120
        colors = {"P1":"red", "P2":"blue", "P3":"green", "P4":"orange"}

        # Start marker
        self.canvas.create_text(20, y + 20, text="START", font=("Arial", 10, "bold"), fill="black")

        for pid, start, duration in schedule:
            rect, text, x = self.draw_block(pid, start, duration, x, colors.get(pid, "gray"))
            self.root.update()
            time.sleep(duration)

        # End marker
        self.canvas.create_text(x + 40, y + 20, text="END", font=("Arial", 10, "bold"), fill="black")

    def run_fifo(self):
        self.canvas.delete("all")
        scheduler = FIFO(self.processes)
        threading.Thread(target=self.animate, args=(scheduler.schedule(),), daemon=True).start()

    def run_rr(self):
        self.canvas.delete("all")
        scheduler = RoundRobin(self.processes, quantum=2)
        threading.Thread(target=self.animate, args=(scheduler.schedule(),), daemon=True).start()

    def run_lrsf(self):
        self.canvas.delete("all")
        scheduler = LRSF(self.processes)
        threading.Thread(target=self.animate, args=(scheduler.schedule(),), daemon=True).start()


if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()
