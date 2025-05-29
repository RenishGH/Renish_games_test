from random import choice
from turtle import *
from freegames import floor, vector

state = {'score': 0}
aim = vector(5, 0)
pacman = vector(-40, -80)
ghosts = []
speed = 100  # default normal speed

path = Turtle(visible=False)
writer = Turtle(visible=False)
pen = Turtle(visible=False)

initial_ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

original_tiles = tiles.copy()

def square(x, y):
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()
    for _ in range(4):
        path.forward(20)
        path.left(90)
    path.end_fill()

def offset(point):
    x = int((floor(point.x, 20) + 200) / 20)
    y = int((180 - floor(point.y, 20)) / 20)
    if x < 0 or x >= 20 or y < 0 or y >= 20:
        return -1
    return x + y * 20

def valid(point):
    index = offset(point)
    if index == -1 or tiles[index] == 0:
        return False
    index = offset(point + 19)
    if index == -1 or tiles[index] == 0:
        return False
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    bgcolor('black')
    path.color('blue')
    for index in range(len(tiles)):
        tile = tiles[index]
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    writer.undo()
    writer.write(state['score'])
    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)
    if index != -1 and tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [vector(5, 0), vector(-5, 0), vector(0, 5), vector(0, -5)]
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')

    update()

    for point, _ in ghosts:
        if abs(pacman - point) < 20:
            up()
            goto(0, -10)
            color('white')
            write("GAME OVER - Press R to Restart", align="center", font=("Arial", 16, "bold"))
            return

    ontimer(move, speed)

def change(x, y):
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

def start_game():
    pen.clear()
    move()

def reset_game():
    global pacman, aim, ghosts, tiles, state
    aim.x, aim.y = 5, 0
    pacman.x, pacman.y = -40, -80
    ghosts.clear()
    for ghost in initial_ghosts:
        ghosts.append([ghost[0].copy(), ghost[1].copy()])
    state['score'] = 0
    for i in range(len(original_tiles)):
        tiles[i] = original_tiles[i]
    clear()
    world()
    pen.clear()
    pen.color('white')
    pen.up()
    pen.goto(0, 0)
    pen.write("RENISH GAMES", align="center", font=("Arial", 24, "bold"))
    ontimer(start_game, 2000)  # Show splash for 2 seconds
    move()

def set_speed_fast(): global speed; speed = 50
def set_speed_normal(): global speed; speed = 100
def set_speed_slow(): global speed; speed = 150

setup(420, 460, 370, 0)
hideturtle()
tracer(False)

writer.goto(160, 180)
writer.color('white')
writer.write(state['score'])

listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
onkey(reset_game, 'r')
onkey(set_speed_slow, '1')
onkey(set_speed_normal, '2')
onkey(set_speed_fast, '3')

reset_game()
done()
