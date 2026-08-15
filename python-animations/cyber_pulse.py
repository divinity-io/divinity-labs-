import os
import random
import shutil
import sys
import time
import math

# ANSI colors
RESET = "\033[0m"
CYAN = "\033[96m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
WHITE = "\033[97m"

CHARS = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ#$@*+"
COLORS = [CYAN, BLUE, PURPLE, WHITE]


def clear():
    os.system("clear")


def hide_cursor():
    sys.stdout.write("\033[?25l")


def show_cursor():
    sys.stdout.write("\033[?25h")


def main():
    hide_cursor()

    try:
        while True:
            width, height = shutil.get_terminal_size()
            center_x = width // 2
            center_y = height // 2

            particles = []

            for _ in range(90):
                angle = random.uniform(0, math.pi * 2)
                distance = random.uniform(3, max(width, height))
                speed = random.uniform(0.15, 0.7)

                particles.append({
                    "angle": angle,
                    "distance": distance,
                    "speed": speed,
                    "char": random.choice(CHARS),
                    "color": random.choice(COLORS)
                })

            for frame in range(120):
                screen = [[" " for _ in range(width)] for _ in range(height)]

                # Center logo
                logo = "DIVINITY"
                start = max(0, center_x - len(logo) // 2)

                if 0 <= center_y < height:
                    for i, char in enumerate(logo):
                        x = start + i
                        if 0 <= x < width:
                            screen[center_y][x] = char

                for p in particles:
                    p["distance"] -= p["speed"] * 3

                    if p["distance"] < 1:
                        p["angle"] = random.uniform(0, math.pi * 2)
                        p["distance"] = max(width, height)
                        p["speed"] = random.uniform(0.15, 0.7)

                    x = int(center_x + math.cos(p["angle"]) * p["distance"])
                    y = int(center_y + math.sin(p["angle"]) * p["distance"] * 0.45)

                    if 0 <= x < width and 0 <= y < height:
                        screen[y][x] = p["color"] + p["char"] + RESET

                clear()

                sys.stdout.write("\n".join("".join(row) for row in screen))
                sys.stdout.flush()

                time.sleep(0.03)

    except KeyboardInterrupt:
        pass

    finally:
        show_cursor()
        clear()
        print(f"{CYAN}🚀 Divinity Python Lab{RESET}")
        print("Animation stopped.")


if __name__ == "__main__":
    main()
