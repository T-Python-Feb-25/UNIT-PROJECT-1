import curses
import pygame

# Initialize Pygame mixer
pygame.mixer.init()

try:
    start_sound = pygame.mixer.Sound("game-start-6104.mp3")
    end_sound = pygame.mixer.Sound("game-bonus-144751.mp3")
except pygame.error as e:
    print(f"Error loading sound: {e}")

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

def play(stdscr):
    global player_x, player_y
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    while True:
        stdscr.clear()

        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if x == player_x and y == player_y:
                    stdscr.addstr(y, x * 2, "P")
                elif cell == "M":
                    stdscr.addstr(y, x * 2, "#")
                elif cell == "E":
                    stdscr.addstr(y, x * 2, "X")
                else:
                    stdscr.addstr(y, x * 2, ".")

        stdscr.refresh()
        
        key = stdscr.getch()
        new_x, new_y = player_x, player_y
        
        if key == ord('w'):
            new_y -= 1
        elif key == ord('s'):
            new_y += 1
        elif key == ord('a'):
            new_x -= 1
        elif key == ord('d'):
            new_x += 1

        # Ensure new position is within the maze boundaries
        if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze):
            if maze[new_y][new_x] != "M":
                player_x, player_y = new_x, new_y

        if maze[player_y][player_x] == "E":
            stdscr.clear()
            stdscr.addstr(5, 5, "YOU WIN!!🎉", curses.A_BOLD)
            end_sound.play()
            stdscr.refresh()
            curses.napms(2000)
            break

# Start the game
curses.wrapper(play)