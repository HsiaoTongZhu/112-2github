import curses
import random

# Constants
NORMAL_FOOD = 'π'
SPECIAL_FOOD = 'X'
OBSTACLE = '#'

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = stdscr.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

# Initial snake setup
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# Initial food setup
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], NORMAL_FOOD)

special_food = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
w.addch(special_food[0], special_food[1], SPECIAL_FOOD)

# Initial obstacle setup
obstacles = []
num_obstacles = (sh * sw) // 20
while len(obstacles) < num_obstacles:
    if random.choice([True, False]):
        # Horizontal obstacle
        row = random.randint(1, sh - 2)
        col = random.randint(1, sw - 7)
        for i in range(5):
            obstacles.append([row, col + i])
            w.addch(row, col + i, OBSTACLE, curses.A_REVERSE)
    else:
        # Vertical obstacle
        row = random.randint(1, sh - 7)
        col = random.randint(1, sw - 2)
        for i in range(5):
            obstacles.append([row + i, col])
            w.addch(row + i, col, OBSTACLE, curses.A_REVERSE)

# Snake's initial direction
key = curses.KEY_RIGHT
score_normal = 0
score_special = 0
paused = False

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if key == ord(' '):
        paused = not paused

    if paused:
        continue

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ord(' ')]:
        key = prev_key

    # Calculate new head position
    head = snake[0]
    if key == curses.KEY_RIGHT:
        new_head = [head[0], head[1] + 1]
    elif key == curses.KEY_LEFT:
        new_head = [head[0], head[1] - 1]
    elif key == curses.KEY_UP:
        new_head = [head[0] - 1, head[1]]
    elif key == curses.KEY_DOWN:
        new_head = [head[0] + 1, head[1]]

    # Wrap around the screen
    new_head[0] = (new_head[0] + sh) % sh
    new_head[1] = (new_head[1] + sw) % sw

    # Check for collision with self
    if new_head in snake:
        break

    # Check for collision with obstacles
    if new_head in obstacles:
        break

    # Check for collision with food
    if new_head == food:
        score_normal += 1
        food = None
        while food is None:
            nf = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            food = nf if nf not in snake and nf not in obstacles else None
        w.addch(food[0], food[1], NORMAL_FOOD)
    else:
        snake.pop()

    # Check for collision with special food
    if new_head == special_food:
        score_special += 1
        if len(snake) > 1:
            snake.pop()
        special_food = None
        while special_food is None:
            sf = [random.randint(1, sh - 2), random.randint(1, sw - 2)]
            special_food = sf if sf not in snake and sf not in obstacles else None
        w.addch(special_food[0], special_food[1], SPECIAL_FOOD)

    snake.insert(0, new_head)

    # Draw snake
    w.clear()
    for o in obstacles:
        w.addch(o[0], o[1], OBSTACLE, curses.A_REVERSE)
    for part in snake:
        w.addch(part[0], part[1], '*')

    w.addch(food[0], food[1], NORMAL_FOOD)
    w.addch(special_food[0], special_food[1], SPECIAL_FOOD)

# End of game
curses.endwin()
print(f"Game Over! Normal food eaten: {score_normal}, Special food eaten: {score_special}")
