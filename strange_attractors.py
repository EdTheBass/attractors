import pygame as game

game.init()

WIDTH = 800
HEIGHT = 800

SCALE = 150
OFFSET_X = 150
OFFSET_Y = -100

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

def draw_points():
    for p in points:
        game.draw.line(window, (255, 255, 255), p, p, 1)
        
iterations = 1000000

generate_points([0.1, 0.1])


running = True
while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    window.fill((0, 0, 0))

    draw_points()

    game.display.update()
