import random

def generate_path(maze, N, M):
    path = []
    i, j = 0, 0
    while i < N and j < M:
        maze[(i, j)] = 2
        path.append((i, j))
        if i == N - 1:
            j += 1
        elif j == M - 1:
            i += 1
        else:
            if random.choice([True, False]):
                i += 1
            else:
                j += 1
    return path


def add_obstacles(maze, min_obstacles, N, M):
    count = 0
    while count < min_obstacles:
        i, j = random.randint(0, N-1), random.randint(0, M-1)
        if maze.get((i, j), 0) == 0:
            maze[(i, j)] = 1
            count += 1
    

def set_obstacle(maze, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to set an obstacle (i, j): ").split())
        if (i, j) in maze and maze[(i, j)] == 2:
            print("Error: Cannot place an obstacle on the path.")
        elif (i < 0 or i >= N or j < 0 or j >= M):
            raise KeyError
        else:
            maze[(i, j)] = 1
    except ValueError:
        print("Error: Invalid input. Please enter valid coordinates.")
    except KeyError:
        print("Error: Coordinates out of bounds.")



def remove_obstacle(maze, N, M):
    try:
        i, j = map(int, input("Enter the coordinates to remove an obstacle (i, j): ").split())
        if (i, j) in maze and maze[(i, j)] == 2:
            print("Error: Cannot remove the path.")
        elif (i < 0 or i >= N or j < 0 or j >= M):
            raise KeyError
        elif (i, j) not in maze or maze[(i, j)] != 1:
            print("Error: No obstacle at given coordinates.")
        else:
            maze[(i, j)] = 0
    except ValueError:
        print("Error: Invalid input. Please enter valid coordinates.")
    except KeyError:
        print("Error: Coordinates out of bounds.")


def print_maze(maze, N, M):

    print("+---" * M + "+")
    for i in range(N):
        print("|", end ="")
        for j in range(M):
            if (i, j) in maze:
                if maze[(i, j)] == 0:
                    print("   " + "|"  , end ="")
                elif maze[(i, j)] == 1:
                    print(" X " + "|" , end ="")
                elif maze[(i, j)] == 2:
                    print(" O " + "|" , end ="")
            else:
                print(" " + "   " + " |", end ="")
        print()
        print("+---" * M + "+")
    print() 

def main():
    file_name = input("Enter the file name: ")
    while True:
        try:
            with open(file_name, 'r') as file:
                maze_data = [list(line.strip()) for line in file.readlines()]
            break
        except FileNotFoundError:
            print("File not found. Please enter a valid file name.")
            file_name = input("Enter the file name: ")

    N = len(maze_data)
    M = len(maze_data[0])
    maze = {(i, j): 0 if maze_data[i][j] == ' ' else 1 for i in range(N) for j in range(M)}

    path = generate_path(maze, N, M)
    print_maze(maze, N, M)

    while True:
        try:
            min_obstacles = int(input("Enter the minimum number of obstacles(0-55): "))
            if min_obstacles < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid number of obstacles.")

    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)

    while True:
        print("\nOptions: ")
        print("1. Add Obstacle")
        print("2. Remove Obstacle")
        print("3. Print Maze")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '4':
            break
        elif choice == '1':
            set_obstacle(maze, N, M)
        elif choice == '2':
            remove_obstacle(maze, N, M)
        elif choice == '3':
            print_maze(maze, N, M)
        else:
            print("Invalid choice. Please try again.")
        
        print_maze(maze, N, M)

if __name__ == "__main__":
    main()
