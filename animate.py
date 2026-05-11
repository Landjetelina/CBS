import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import matplotlib.patches as patches


class MultiAgentAnimator:
    def __init__(self, paths, grid_size, forbidden_nodes=None):
        if forbidden_nodes is None:
            forbidden_nodes = []
        self.paths = paths
        self.grid_size = grid_size
        self.forbidden_nodes = forbidden_nodes

        self.current_step = 0
        self.playing = False
        self.max_steps = max(len(p) for p in paths.values())
        self.speed_levels = [0.1, 0.25, 0.5, 1, 2, 5, 10, 20]
        self.speed_index = 3
        self.speed_multiplier = self.speed_levels[self.speed_index]

        self.colors = ["red", "blue", "green", "orange", "purple", "brown", "pink", "cyan", "magenta", "gold"]
        self.agent_colors = {}
        for i, agent in enumerate(paths.keys()):
            self.agent_colors[agent] = self.colors[i % len(self.colors)]
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        plt.subplots_adjust(bottom=0.2)
        self.agent_drawings = {}
        self.setup_plot()
        self.ani = FuncAnimation(
            self.fig,
            self.animate,
            interval=100,
            blit=False,
            cache_frame_data=False
        )
    def setup_plot(self):
        self.ax.set_xlim(-0.5, self.grid_size - 0.5)
        self.ax.set_ylim(-0.5, self.grid_size - 0.5)

        self.ax.set_xticks(range(self.grid_size))
        self.ax.set_yticks(range(self.grid_size))

        if self.grid_size > 10:
            self.ax.set_xticks(range(self.grid_size))
            self.ax.set_yticks(range(self.grid_size))

            self.ax.set_xticklabels([''] * self.grid_size)
            self.ax.set_yticklabels([''] * self.grid_size)

        self.ax.grid(True)
        self.ax.invert_yaxis()

        # obstacles
        for node in self.forbidden_nodes:
            rect = patches.Rectangle(
                (node.col - 0.5, node.row - 0.5), 1, 1, color='black')
            self.ax.add_patch(rect)
        # goals
        for agent_name, path in self.paths.items():
            goal = path[-1]
            self.ax.plot(goal[1], goal[0], marker='X', markersize=15, color=self.agent_colors[agent_name])
        # agents
        self.agent_trails = {}
        for agent_name, path in self.paths.items():
            start = path[0]
            circle = patches.Circle(
                (start[1], start[0]),
                radius=0.25,
                color=self.agent_colors[agent_name]
            )
            self.ax.add_patch(circle)

            text = self.ax.text(start[1], start[0], agent_name, color="white",
                ha="center", va="center", fontsize=8)
            trail_line, = self.ax.plot([], [], color=self.agent_colors[agent_name],
                linewidth=2, marker='o', alpha=0.6)
            self.agent_drawings[agent_name] = (circle, text)
            self.agent_trails[agent_name] = trail_line
        self.create_buttons()
        self.speed_text = self.ax.text(
            0,
            -1,
            f"Speed: {self.speed_multiplier}x",
            fontsize=12,
            fontweight='bold'
        )

    def create_buttons(self):
        # PREV
        ax_prev = plt.axes([0.45, 0.05, 0.1, 0.075])
        self.btn_prev = Button(ax_prev, 'Prev')
        # PLAY
        ax_play = plt.axes([0.57, 0.05, 0.12, 0.075])
        self.btn_play = Button(ax_play, 'Play')
        # NEXT
        ax_next = plt.axes([0.71, 0.05, 0.1, 0.075])
        self.btn_next = Button(ax_next, 'Next')
        # RESTART
        ax_restart = plt.axes([0.83, 0.05, 0.12, 0.075])
        self.btn_restart = Button(ax_restart, 'Restart')
        # SLOWER
        ax_slower = plt.axes([0.01, 0.05, 0.12, 0.075])
        self.btn_slower = Button(ax_slower, 'Slower')
        # FASTER
        ax_faster = plt.axes([0.15, 0.05, 0.12, 0.075])
        self.btn_faster = Button(ax_faster, 'Faster')

        self.btn_prev.on_clicked(self.prev_step)
        self.btn_play.on_clicked(self.toggle_play)
        self.btn_next.on_clicked(self.next_step)
        self.btn_restart.on_clicked(self.restart_animation)
        self.btn_slower.on_clicked(self.slower_speed)
        self.btn_faster.on_clicked(self.faster_speed)

        self.update_play_button_color()

    def update_play_button_color(self):
        if self.playing:
            self.btn_play.ax.set_facecolor("red")
            self.btn_play.ax.patch.set_facecolor("red")
            self.btn_play.color = "red"
            self.btn_play.hovercolor = "darkred"
            self.btn_play.label.set_text("Pause")
            self.btn_play.label.set_color("white")
        else:
            self.btn_play.ax.set_facecolor("lightgray")
            self.btn_play.ax.patch.set_facecolor("lightgray")
            self.btn_play.color = "lightgray"
            self.btn_play.label.set_text("Play")
            self.btn_play.label.set_color("black")
        # self.fig.canvas.draw_idle()

    def update_speed_text(self):
        self.speed_text.set_text(f"Speed: {self.speed_multiplier}x")
        # self.fig.canvas.draw_idle()

    def faster_speed(self, event):

        if self.speed_index < len(self.speed_levels) - 1:
            self.speed_index += 1
            self.speed_multiplier = self.speed_levels[self.speed_index]
            self.update_speed_text()

    def slower_speed(self, event):
        if self.speed_index > 0:
            self.speed_index -= 1
            self.speed_multiplier = self.speed_levels[self.speed_index]
            self.update_speed_text()

    def update_agents(self):
        for agent_name, path in self.paths.items():
            idx = min(int(self.current_step), len(path) - 1)
            pos = path[idx]
            circle, text = self.agent_drawings[agent_name]
            circle.center = (pos[1], pos[0])
            text.set_position((pos[1], pos[0]))
            # TRAIL
            trail_positions = path[:idx + 1]

            xs = [p[1] for p in trail_positions]
            ys = [p[0] for p in trail_positions]

            self.agent_trails[agent_name].set_data(xs, ys)
        # self.fig.canvas.draw_idle()

    def animate(self, frame):
        self.update_play_button_color()
        if self.playing:
            if int(self.current_step) < self.max_steps - 1:
                step_size = self.speed_multiplier * 0.1
                self.current_step += step_size
                self.update_agents()
            else:
                self.playing = False
                self.update_play_button_color()
        return []
    def next_step(self, event):
        if self.current_step < self.max_steps - 1:
            self.current_step += 1
            self.update_agents()

    def prev_step(self, event):
        if self.current_step > 0:
            self.current_step -= 1
            self.update_agents()
    def toggle_play(self, event):
        self.playing = not self.playing
        self.update_play_button_color()

    def show(self):
        manager = plt.get_current_fig_manager()
        window = manager.window
        window.update_idletasks()
        window.geometry(f"+{0}+{0}")
        plt.show(block=True)

    def restart_animation(self, event):
        self.playing = True
        self.current_step = 0
        # reset trailova
        for trail in self.agent_trails.values():
            trail.set_data([], [])
        self.update_agents()
        self.update_play_button_color()