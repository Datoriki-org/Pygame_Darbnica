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
score = 0
max_jumps = 2         # Cik lēcienus var izpildīt kopā (2 = dubultlēciens)
jumps_made = 0        # Cik lēcieni jau veikti kopš pēdējās saskares ar zemi
win = False
lose = False
TARGET_SCORE = 1 # Cik monetas jasavac lai uzvaretu

jump_sound = sounds.splat   # failā 'sounds/jump.wav'
coin_sound = sounds.meow1

##############
# Bloks 2
##############

# Speles karte
level = [
    "....................",
    "....................",
    "............c#......",
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
coins = []

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
        if tile == 'c':
            coins.append(Actor('cat3', (sx + tile_width()/2, sy + tile_height()/2)))

##############
# Bloks 3
##############

# Draw cikls
def draw():
    screen.clear()
    screen.fill((135, 206, 235))  # Background krasa (R, G, B)
    for plat in platforms:
        screen.draw.filled_rect(plat, (100, 100, 100)) # Platformu krasa (R, G, B)
    for c in coins:
        c.draw()    
    screen.draw.text("Score: " + str(score), (0, 0))
    if win:
        screen.draw.text("Tu uzvari!", center=(WIDTH/2, HEIGHT/2), fontsize=60)
    elif lose:
        screen.draw.text("Spēle beigusies", center=(WIDTH/2, HEIGHT/2), fontsize=60)


    player.draw() #Zime speletaju

##############
# Bloks 4
##############

# Update cikls
def update():
    global vy, on_ground, score, dx, lose, win

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

    for c in coins:
        if player.colliderect(c):
            coins.remove(c)
            coin_sound.play()
            score += 1

    if player.y > HEIGHT:
        lose = True

    if score >= TARGET_SCORE:
        win = True
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
                jumps_made = 0   
            elif vy < 0:
                player.top = plat.bottom
                vy = 0

##############
# Bloks 5
##############

# Leksana, nospiesta poga event
def on_key_down(key):
    global vy, on_ground, jumps_made
    if key == keys.SPACE or key == keys.UP:
        if jumps_made < max_jumps:
            vy = -15
            jumps_made += 1
            jump_sound.play()
            on_ground = False