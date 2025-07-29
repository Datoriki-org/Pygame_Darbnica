# ==============================
# Spēles papildinājumi
# ==============================

# ==== Papildinājums: Monētu vākšana ====

# 1) Bloks 2: Monētu saraksts
coins = []

# 2) Bloks 2, kartes parsing cilpa:
if tile == 'c':
    coins.append(Actor('Monētas-Atēls', (sx + tile_width()/2, sy + tile_height()/2)))

# 3) Bloks 3 (funkcija draw):
for c in coins:
    c.draw()

# 4) Bloks 4 (funkcija update), pēc fizikas aprēķiniem:
for c in coins:
    if player.colliderect(c):
        coins.remove(c)
        score += 1

# ==== Papildinājums: Uzvara / Zaudējums ====

# 1) Bloks 1: Spēles stāvokļa mainīgie
win = False
lose = False
TARGET_SCORE = 10

# 2) Bloks 4 (funkcija update): pārbaudīt nokrišanu zem ekrāna
if player.y > HEIGHT:
    lose = True

# 3) Bloks 4 (funkcija update): pārbaudīt punktu skaitu
if score >= TARGET_SCORE:
    win = True

# 4) Bloks 3 (funkcija draw): ziņojumu attēlošana
if win:
    screen.draw.text("Tu uzvari!", center=(WIDTH/2, HEIGHT/2), fontsize=60)
if lose:
    screen.draw.text("Spēle beigusies", center=(WIDTH/2, HEIGHT/2), fontsize=60)


# ==== Papildinājums: Elastīgs lēcienu skaits ====

# 1) Bloks 1: Mainīgie
max_jumps = 2         # Cik lēcienus var izpildīt kopā (2 = dubultlēciens)
jumps_made = 0        # Cik lēcieni jau veikti kopš pēdējās saskares ar zemi

# 2) Bloks 4b (funkcija vertical_collision_helper), kad spēlētājs pieskaras platformai:
jumps_made = 0        # Atiestata lēcienu skaitītāju, jo spēlētājs atkal uz zemes

# 3) Bloks 5 (funkcija on_key_down): lēciena loģika ar ierobežojumu
if key == keys.SPACE or key == keys.UP:
    if jumps_made < max_jumps:
        vy = -15
        jumps_made += 1
        on_ground = False

# (NB! Dzēs vai komentē sākotnējo if on_ground bloku, lai neaizkavētu atkārtotus lēcienus)

# ==== Papildinājums: Skaņas efekti ====

# 1) Bloks 1: Pievieno skaņas
jump_sound = sounds.jump   # failā 'sounds/jump.wav'
coin_sound = sounds.coin   # failā 'sounds/coin.wav'

# Atskaņo skaņu izmantojot funkciju

jump_sound.play()
coin_sound.play()