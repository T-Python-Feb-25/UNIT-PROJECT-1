import curses
import pygame
import json
import time
from rich.table import Table
from rich.console import Console


pygame.mixer.init()

move_sound = pygame.mixer.Sound("game-bonus-144751.mp3")
win_sound = pygame.mixer.Sound("game-start-6104.mp3")

def load_scores():
    try:
        with open("scores.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_scores(scores):
    with open("scores.json", "w") as file:
        json.dump(scores, file, indent=4)


maze = [
    "MMMMMMMMM",
    "M.......M",
    "M.MMMM..M",
    "M.M..M..E",
    "M.MMMMMMM",
    "M.......M",
    "MMMMMMMMM"
]

player_x, player_y = 1, 1

username = input("enter your user name for the score: ")

scores = load_scores()

start_time = time.time()

def play(movememt):
    global player_x, player_y
    curses.curs_set(0)
    movememt.nodelay(1)
    movememt.timeout(100)

    while True:
        movememt.clear()

        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if x == player_x and y == player_y:
                    movememt.addstr(y, x * 2, "P")
                elif cell == "M":
                    movememt.addstr(y, x * 2, "#")
                elif cell == "E":
                    movememt.addstr(y, x * 2, "X")
                else:
                    movememt.addstr(y, x * 2, ".")

        movememt.refresh()

        key = movememt.getch()
        new_x, new_y = player_x, player_y

        if key == ord('w'):
            new_y -= 1
        elif key == ord('s'):
            new_y += 1
        elif key == ord('a'):
            new_x -= 1
        elif key == ord('d'):
            new_x += 1

        if maze[new_y][new_x] != "M":
            player_x, player_y = new_x, new_y
            move_sound.play()

        if maze[player_y][player_x] == "E":
            win_sound.play()
            end_time = time.time()
            elapsed_time = round(end_time - start_time, 2)

            scores[username] = elapsed_time
            save_scores(scores)

            movememt.clear()
            movememt.addstr(5, 5, f"🎉 congra\n{elapsed_time} sec.", curses.A_BOLD)
            movememt.refresh()
            pygame.time.delay(2000)
            break

curses.wrapper(play)
console = Console()
table = Table(title="\nGAME BEST SCORE!!🏆", title_justify="center")
table.add_column("RANK", justify="right")
table.add_column("NAME")
table.add_column("TIME", justify="right")

sorted_scores = sorted(scores.items(), key=lambda x: x[1])  

for rank, (user, time_taken) in enumerate(sorted_scores, 1):
    table.add_row(str(rank), user, str(time_taken))

console.print(table)