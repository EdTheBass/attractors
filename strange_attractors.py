import pygame as game

game.init()

WIDTH = 800
HEIGHT = 800

SCALE = 150
OFFSET_X = 150
OFFSET_Y = -100


def _map(val, r1, r2, nr1, nr2):
    return ((val - r1) / (r2 - r1) ) * (nr2 - nr1) + nr1

def num2rgb(num):
    h = hex(int(num))[2:]
    h = "0"*(6-len(h))+h
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb

def fx(xy):
    x,y = xy
    a,b,c,d,e,f = -1.2, -0.6, -0.5, 0.1, -0.7, 0.2
    return a + b*x + c*x**2 + d*x*y + e*y + f*y**2

def fy(xy):
    x,y = xy
    a,b,c,d,e,f = -0.9, 0.9, 0.1, -0.3, -1, 0.3
    return a + b*x + c*x**2 + d*x*y + e*y + f*y**2

def centre(xy):
    x,y = xy
    return [x+(WIDTH//2)+OFFSET_X,-y+(HEIGHT//2)+OFFSET_Y]

window = game.display.set_mode((WIDTH, HEIGHT))
game.display.set_caption("Strange Attractors")

points = []

def generate_points(start):
    pos = start
    for x in range(iterations):
        if not (x+1)%1000: print(x+1)
        pos = [fx(pos), fy(pos)]
        d_pos = centre(scale(pos))
        points.append(d_pos)

def scale(point):
    x,y = point
    return [x*SCALE, y*SCALE]

def get_colour(i):
    num = int(_map(i, 0, iterations, 0, 16777215))
    rgb = num2rgb(num)
    return rgb

def draw_points():
    for i, p in enumerate(points):
        game.draw.line(window, get_colour(i), p, p, 7)
        
iterations = 100000

generate_points([0.1, 0.1])


running = True
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    window.fill((0, 0, 0))

    draw_points()

    game.display.update()
