##############
# Bloks 1
##############

# Spēles ekrāna izmērs pikseļos
WIDTH = 640
HEIGHT = 480

# Kartes iestatījumi
TILE_COLUMNS = 20
TILE_ROWS = 15

# Spēlētājs
player = Actor('alien')
player.pos = (100, 100) # Sākuma pozīcija

# Fizikas variables
vy = 0 # Vertikālais ātrums
dx = 0 # Horizontālais ātrums
on_ground = False

# TODO: Pieliec iespēju glabāt punktus
# TODO: Pievieno nepieciešamos mainīgos priekš double jump 

##############
# Bloks 2
##############

# Spēles karte
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
# TODO: Pievieno monētu list

# Palīgfunkcijas
def tile_width():
    return WIDTH / TILE_COLUMNS

def tile_height():
    return HEIGHT / TILE_ROWS

# Izveido spēles karti
for y, row in enumerate(level):
    for x, tile in enumerate(row):
        sx = x * tile_width()
        sy = y * tile_height()
        if tile == '#':
            platforms.append(Rect((sx, sy), (tile_width(), tile_height())))
        # TODO: Ja simbols sakrīt ar monētu, pievieno monētu

##############
# Bloks 3
##############

# Draw cikls
def draw():
    screen.clear()
    screen.fill((135, 206, 235))  # Background krāsa (R, G, B)
    for plat in platforms:
        screen.draw.filled_rect(plat, (100, 100, 100)) # Platformu krāsa (R, G, B)
    # TODO: Zīmēt monētas
    
    player.draw() #Zīmē spēlētāju

##############
# Bloks 4
##############

# Update cikls
def update():
    global vy, on_ground, score, dx

    # Kustība pa labi/ kreisi
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

    # TODO: Monētu vākšana
    # TODO: Vieta kur pielikt iespēju spēli uzvarēt
    # TODO: Vieta kur pielikt iespēju spēli zaudēt

# Palīgfunkcijas
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

# Lekšana, nospiesta poga event
def on_key_down(key):
    global vy, on_ground
    if key == keys.SPACE:
        if on_ground:
            vy = -15
            on_ground = False
        # TODO: Vieta kur pielikt Double Jump
