##############
# Bloks 1
##############

# Speles ekrana izmers pikselos
WIDTH = 640
HEIGHT = 480

# Kartes iestatijumi
TILE_COLUMNS = 20
TILE_ROWS = 15

# Speletajs
player = Actor('alien')
player.pos = (100, 100) # Sakuma pozicija

# Fizikas variables
vy = 0 # Vertikalais atrums
dx = 0 # Horizontalais atrums
on_ground = False

# TODO: Pieliec iespeju glabat punktus
# TODO: Pievieno nepieciesamos mainigos prieks double jump 

##############
# Bloks 2
##############

# Speles karte
level = [
    "....................",
    "....................",
    ".............#......",
    "....................",
    ".......#####........",
    "..................#.",
    "......###...........",
    "....................",
    ".................##.",
    "####...###....#..####",
    "....................",
    "....................",
    ".........##.........",
    "....##.............",
    "....................",
]

platforms = [] # Platformu list
# TODO: Pievieno monetu list

# Paligfunkcijas
def tile_width():
    return WIDTH / TILE_COLUMNS

def tile_height():
    return HEIGHT / TILE_ROWS

# Izveido speles karti
for y, row in enumerate(level):
    for x, tile in enumerate(row):
        sx = x * tile_width()
        sy = y * tile_height()
        if tile == '#':
            platforms.append(Rect((sx, sy), (tile_width(), tile_height())))
        # TODO: Ja simbols sakrit ar monetu, pievieno monetu

##############
# Bloks 3
##############

# Draw cikls
def draw():
    screen.clear()
    screen.fill((135, 206, 235))  # Background krasa (R, G, B)
    for plat in platforms:
        screen.draw.filled_rect(plat, (100, 100, 100)) # Platformu krasa (R, G, B)
    # TODO: Zimet monetas
    
    player.draw() #Zime speletaju

##############
# Bloks 4
##############

# Update cikls
def update():
    global vy, on_ground, score, dx

    # Kustiba pa labi/ kreisi
    dx = 0
    if keyboard.left: dx = -3
    if keyboard.right: dx = 3
    player.x += dx
    
    horizontal_collision_helper()

    # Gravity
    vy += 0.5   
    if vy > 10: vy = 10
    player.y += vy

    vertical_collision_helper()

    # TODO: Monetu vaksana
    # TODO: Vieta kur pielikt iespeju speli uzvaret
    # TODO: Vieta kur pielikt iespeju speli zaudet

# Paligfunkcijas
def horizontal_collision_helper():
    global dx
    for plat in platforms:
        if player.colliderect(plat):
            if dx > 0: player.right = plat.left
            elif dx < 0: player.left = plat.right

def vertical_collision_helper():
    global vy, on_ground
    on_ground = False
    for plat in platforms:
        if player.colliderect(plat):
            if vy > 0:
                player.bottom = plat.top
                vy = 0
                on_ground = True
                # TODO: Vieta kur pielikt Double Jump
            elif vy < 0:
                player.top = plat.bottom
                vy = 0

##############
# Bloks 5
##############

# Leksana, nospiesta poga event
def on_key_down(key):
    global vy, on_ground
    if key == keys.SPACE:
        if  on_ground:
            vy = -15
            on_ground = False
        # TODO: Vieta kur pielikt Double Jump
