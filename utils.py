
"""
Functaion takes in a numpy array and prints it out to the console as a maze
The maze is color coded
"""
def print_colored_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == -1:
                # print black if value is -1
                print("\u001b[40m  \u001b[0m", end="")
            elif maze[i][j] == 0:
                # print white if value is 0
                print("\u001b[47m  \u001b[0m", end="")
            elif maze[i][j] == 1:
                # print red if value is 1
                print("\u001b[41m  \u001b[0m", end="")
            elif maze[i][j] == 2:
                # print green if value is 2
                print("\u001b[42m  \u001b[0m", end="")
            elif maze[i][j] == 3:
                # print blue if value is 3
                print("\u001b[44m  \u001b[0m", end="")
            elif maze[i][j] == 4:
                # print yellow if value is 4
                print("\u001b[43m  \u001b[0m", end="")
            elif maze[i][j] == 5:
                # print magenta if value is 1
                print("\u001b[45m  \u001b[0m", end="")
        print()