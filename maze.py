def print_maze(maze, player_pos):
    for i, row in enumerate(maze):
        line = ""
        for j, cell in enumerate(row):
            if (i, j) == player_pos:
                line += "P "
            else:
                line += cell + " "
        print(line)
    print()

def move_player(maze, player_pos, move):
    x, y = player_pos
    if move == "w" and x > 0:  
        return (x - 1, y)
    elif move == "s" and x < len(maze) - 1:  
        return (x + 1, y)
    elif move == "a" and y > 0:  
        return (x, y - 1)
    elif move == "d" and y < len(maze[0]) - 1:  
        return (x, y + 1)
    return player_pos

def maze_game():
    maze = [
        ["#", "#", "#", "#", "#", "#"],
        ["#", " ", " ", "#", " ", "#"],
        ["#", " ", "#", " ", " ", "#"],
        ["#", " ", "#", "#", " ", "#"],
        ["#", " ", " ", " ", " ", "#"],
        ["#", "#", "#", "#", "#", "#"],
    ]
    player_pos = (1, 1)
    goal = (4, 4)

    while player_pos != goal:
        print_maze(maze, player_pos)
        move = input("Use w/a/s/d to move: ")
        player_pos = move_player(maze, player_pos, move)

    print("You have reached the end!")

if __name__ == "__main__":
    maze_game()