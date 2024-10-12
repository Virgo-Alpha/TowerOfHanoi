import time

class TowerOfHanoi:
    def __init__(self, disc_count, canvas, delay):
        self.disc_count = disc_count
        self.canvas = canvas
        self.delay = delay
        self.poles = {'A': [], 'B': [], 'C': []}
        self.discs = []
        self.init_discs()

    def init_discs(self):
        # Create the rods/poles
        self.pole_positions = {
            'A': 200,
            'B': 400,
            'C': 600
        }
        self.canvas.create_line(200, 100, 200, 500, width=5)  # Pole A
        self.canvas.create_line(400, 100, 400, 500, width=5)  # Pole B
        self.canvas.create_line(600, 100, 600, 500, width=5)  # Pole C

        # Create the discs
        for i in range(self.disc_count):
            width = 160 - i * 20
            disc = self.canvas.create_rectangle(
                self.pole_positions['A'] - width//2, 500 - i*20, 
                self.pole_positions['A'] + width//2, 520 - i*20, 
                fill="gray"
            )
            self.poles['A'].append(disc)
            self.discs.append(disc)

    def move_disc(self, source, target):
        if self.poles[source]:
            disc = self.poles[source].pop()
            self.poles[target].append(disc)

            # Get target height based on number of discs in the target pole
            target_height = 500 - (len(self.poles[target]) - 1) * 20

            # Animate the movement
            x1, y1, x2, y2 = self.canvas.coords(disc)
            self.canvas.coords(disc, self.pole_positions[target] - (x2 - x1) // 2, target_height - 20,
                               self.pole_positions[target] + (x2 - x1) // 2, target_height)

            # Add a delay between moves
            time.sleep(self.delay)
            self.canvas.update()
