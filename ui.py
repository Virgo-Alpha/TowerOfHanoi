import tkinter as tk
from logic import TowerOfHanoi
import time

class HanoiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower of Hanoi")
        # self.root.attributes('-fullscreen', True)  # Launch in full screen

        self.paused = False  # Flag for pause functionality
        self.stopped = False  # Flag for stop functionality

        self.disc_count = 3
        self.delay = 1  # Delay in seconds
        self.start_time = None  # Start time for tracking duration
        self.total_moves = 0  # Total moves for calculation
        self.current_move = 0  # Current move counter
        self.status = "Not Initiated"  # Game status

        # UI setup
        self.create_widgets()

    def create_widgets(self):
        # Main frame for layout
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Left frame for controls
        control_frame = tk.Frame(main_frame, width=400, bg="#f0f0f0")
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Right frame for canvas
        self.canvas = tk.Canvas(main_frame, width=600, height=600, bg="white")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Control panel for discs, delay, and buttons
        self.create_control_widgets(control_frame)

        # Initialize discs on canvas
        self.update_discs()

        # Add minimize and maximize buttons to the title bar
        self.add_title_buttons()

    def create_control_widgets(self, control_frame):
        # Status label
        self.status_label = tk.Label(control_frame, text="Status: " + self.status, bg="#f0f0f0")
        self.status_label.pack(pady=20)

        # Disc count controls
        disc_frame = tk.Frame(control_frame, bg="#f0f0f0")
        disc_frame.pack(pady=(10, 0))

        tk.Label(disc_frame, text="Discs:", bg="#f0f0f0").pack(side=tk.LEFT)

        self.disc_label = tk.Label(disc_frame, text=str(self.disc_count), bg="#f0f0f0")
        self.disc_label.pack(side=tk.LEFT, padx=(10, 0))

        disc_decrease_button = tk.Button(disc_frame, text="-", command=self.decrease_discs)
        disc_decrease_button.pack(side=tk.LEFT, padx=5)

        disc_increase_button = tk.Button(disc_frame, text="+", command=self.increase_discs)
        disc_increase_button.pack(side=tk.LEFT, padx=5)

        # Delay controls
        delay_frame = tk.Frame(control_frame, bg="#f0f0f0")
        delay_frame.pack(pady=(10, 0))

        tk.Label(delay_frame, text="Delay (s):", bg="#f0f0f0").pack(side=tk.LEFT)

        self.delay_label = tk.Label(delay_frame, text=str(self.delay), bg="#f0f0f0")
        self.delay_label.pack(side=tk.LEFT, padx=(0, 5))

        delay_decrease_button = tk.Button(delay_frame, text="-", command=self.decrease_delay)
        delay_decrease_button.pack(side=tk.LEFT, padx=5)

        delay_increase_button = tk.Button(delay_frame, text="+", command=self.increase_delay)
        delay_increase_button.pack(side=tk.LEFT, padx=5)

        # Control buttons
        control_frame_buttons = tk.Frame(control_frame, bg="#f0f0f0")
        control_frame_buttons.pack(pady=(10, 10))

        start_button = tk.Button(control_frame_buttons, text="Start", command=self.start_game)
        start_button.pack(side=tk.LEFT, padx=5)

        pause_button = tk.Button(control_frame_buttons, text="Pause", command=self.pause_game)
        pause_button.pack(side=tk.LEFT, padx=5)

        stop_button = tk.Button(control_frame_buttons, text="Stop", command=self.stop_game)
        stop_button.pack(side=tk.LEFT, padx=5)

        quit_button = tk.Button(control_frame_buttons, text="Quit", command=self.root.quit)
        quit_button.pack(side=tk.LEFT, padx=5)

        # Timer labels
        self.timer_label = tk.Label(control_frame, text="Time Elapsed: 0s", bg="#f0f0f0")
        self.timer_label.pack(pady=5)

        self.remaining_label = tk.Label(control_frame, text="Estimated Time: N/A", bg="#f0f0f0")
        self.remaining_label.pack(pady=5)

    def add_title_buttons(self):
        # Title bar buttons for minimize and maximize
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit)
        self.root.bind("<Control-n>", self.root.iconify)
        self.root.bind("<Control-m>", lambda: self.root.attributes('-fullscreen', False))

    def update_discs(self):
        """Update the discs visually on the canvas."""
        self.canvas.delete("all")  # Clear existing discs and poles

        # Create the rods/poles with labels
        self.canvas.create_line(200, 100, 200, 500, width=5)  # Pole A
        self.canvas.create_text(200, 70, text="Start", font=("Arial", 12, "bold"))
        self.canvas.create_line(400, 100, 400, 500, width=5)  # Pole B
        self.canvas.create_text(400, 70, text="Transition", font=("Arial", 12, "bold"))
        self.canvas.create_line(600, 100, 600, 500, width=5)  # Pole C
        self.canvas.create_text(600, 70, text="Final", font=("Arial", 12, "bold"))

        # Draw the discs with markings
        for i in range(self.disc_count):
            width = 160 - i * 20
            # Calculate y position based on the index of the disc
            y_position = 500 - (i + 1) * 20  # Ensure that the smallest disc is on top
            self.canvas.create_rectangle(
                200 - width // 2, y_position, 200 + width // 2, y_position + 20, fill="gray"
            )
            self.canvas.create_text(
                200, y_position + 10, text=str(i + 1), fill="black", font=("Arial", 10, "bold")
            )

    def increase_discs(self):
        """Increase the number of discs, up to a maximum of 30."""
        if self.disc_count < 30:
            self.disc_count += 1
            self.disc_label.config(text=str(self.disc_count))
            self.update_discs()

    def decrease_discs(self):
        """Decrease the number of discs, down to a minimum of 3."""
        if self.disc_count > 3:
            self.disc_count -= 1
            self.disc_label.config(text=str(self.disc_count))
            self.update_discs()

    def increase_delay(self):
        """Increase the delay."""
        self.delay += 0.1
        self.delay_label.config(text=f"{self.delay:.1f}")

    def decrease_delay(self):
        """Decrease the delay but not below 0.1 seconds."""
        if self.delay > 0.1:
            self.delay -= 0.1
            self.delay_label.config(text=f"{self.delay:.1f}")

    def start_game(self):
        self.stopped = False
        self.status = "Running"
        self.status_label.config(text="Status: " + self.status)

        # Clear the canvas and update with initial discs
        self.canvas.delete("all")
        self.update_discs()
        
        # Initialize start time
        self.start_time = time.time()
        self.total_moves = 2 ** self.disc_count - 1  # Total moves required
        self.current_move = 0

        hanoi = TowerOfHanoi(self.disc_count, self.canvas, self.delay)
        self.solve_hanoi(hanoi, self.disc_count, 'A', 'C', 'B')

    def solve_hanoi(self, hanoi, n, source, target, auxiliary):
        if n == 0 or self.stopped:
            return
        if not self.paused:
            self.solve_hanoi(hanoi, n - 1, source, auxiliary, target)
            if not self.stopped:
                hanoi.move_disc(source, target)
                self.current_move += 1
                time.sleep(self.delay)
                elapsed_time = int(time.time() - self.start_time)
                remaining_time = self.total_moves - self.current_move
                self.timer_label.config(text=f"Time Elapsed: {elapsed_time}s")
                self.remaining_label.config(text=f"Estimated Time: {remaining_time}s")
            self.solve_hanoi(hanoi, n - 1, auxiliary, target, source)
        else:
            self.root.after(100, lambda: self.solve_hanoi(hanoi, n, source, target, auxiliary))

    def pause_game(self):
        # Toggle pause/resume
        self.paused = not self.paused
        self.status = "Paused" if self.paused else "Running"
        self.status_label.config(text="Status: " + self.status)

    def stop_game(self):
        # Stop the process and reset the flags
        self.stopped = True
        self.paused = False
        self.status = "Terminated"
        self.status_label.config(text="Status: " + self.status)
        self.canvas.delete("all")
        self.update_discs()
        self.timer_label.config(text="Time Elapsed: 0s")
        self.remaining_label.config(text="Estimated Time: N/A")

if __name__ == "__main__":
    root = tk.Tk()
    app = HanoiApp(root)
    root.mainloop()
