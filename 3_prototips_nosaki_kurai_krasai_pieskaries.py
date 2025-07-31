import pygame

WIDTH = 600
HEIGHT = 600

# Background atels
background = pygame.image.load("images/cat1.png").convert()

player = Actor("alien", (100, 100))

def draw():
    screen.clear()
    screen.blit(background, (100, 100))
    player.draw()

dx = 0 # Atrums x ass
vy = 0 # Atrums y ass

def update():
    global dx, vy
    dx = 0
    vy = 0
    
    # Kustiba visos virzienos
    if keyboard.left: dx = -3
    if keyboard.right: dx = 3
    if keyboard.up: vy = -3
    if keyboard.down: vy = 3
    
    player.x += dx
    player.y += vy
    print(is_touching_color())

target_color = (0, 0, 0) # Black

def color_close(a, b, tolerance=10):
    return all(abs(a[i] - b[i]) <= tolerance for i in range(3))

def is_touching_color():
    global player, target_color, background
    x = int(player.x)
    y = int(player.y)
    try:
        pixel_color = background.get_at((x, y))[:3]  # get RGB, ignore alpha
        return color_close(target_color, pixel_color)
    except IndexError:
        return False
