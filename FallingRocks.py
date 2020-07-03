import pygame
import random
import math

pygame.init()

# CONSTANT VARIABLES
WIDTH = 1280
HEIGHT = 720
CLOCK = pygame.time.Clock()
FPS = 60
WN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Rocks")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (242, 232, 202)
WHITE = (255, 255, 255)
BG1 = pygame.image.load("bg1.png")
heart = pygame.image.load("heart.png")
shield = pygame.image.load("shield.png")
hitsound = pygame.mixer.Sound("hitsound.wav")
shieldsound = pygame.mixer.Sound("shieldsound.wav")
shieldsound.set_volume(0.35)
healthsound = pygame.mixer.Sound("healthsound.wav")
font1 = pygame.font.SysFont("arial", 35, True)
font3 = pygame.font.SysFont("arial", 85, True)


class Player:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
        self.x = (WIDTH//2 - self.radius)
        self.y = 650
        self.vel = 6

    def draw(self, WN):
        pygame.draw.circle(WN, self.color, (self.x, self.y), self.radius)
        pygame.draw.circle(WN, BLACK, (self.x, self.y), self.radius + 1, 1)

    def armordraw(self, WN):
        WN.blit(shield, (self.x - 15, self.y - 15))


class Rocks:
    def __init__(self, color):
        self.color = color
        self.radius = random.randint(10,30)
        self.x = random.randint(0, WIDTH)
        self.y = -100
        self.vel = random.randint(3,10)
    def draw(self, WN):
        pygame.draw.circle(WN, self.color, (self.x, self.y), self.radius)


class AddHealth:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = -100
        self.vel = random.randint(3, 10)
        self.radius = 10

    def draw(self, WN):
        if health < 5:
            pygame.draw.circle(WN, RED, ((self.x + 16), (self.y + 15)), self.radius)
            WN.blit(heart, (self.x, self.y))


class AddShield:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = -100
        self.vel = random.randint(3,10)
        self.radius = 10

    def draw(self, WN):
            pygame.draw.circle(WN, RED, ((self.x + 16), (self.y + 15)), self.radius)
            WN.blit(shield, (self.x, self.y))


def healtharmorStatus():
    if health == 5:
        WN.blit(heart, (1230, 15))
        WN.blit(heart, (1230, 45))
        WN.blit(heart, (1230, 75))
        WN.blit(heart, (1230, 105))
        WN.blit(heart, (1230, 135))
    if health == 4:
        WN.blit(heart, (1230, 15))
        WN.blit(heart, (1230, 45))
        WN.blit(heart, (1230, 75))
        WN.blit(heart, (1230, 105))
    if health == 3:
        WN.blit(heart, (1230, 15))
        WN.blit(heart, (1230, 45))
        WN.blit(heart, (1230, 75))
    if health == 2:
        WN.blit(heart, (1230, 15))
        WN.blit(heart, (1230, 45))
    if health == 1:
        WN.blit(heart, (1230, 15))
    if armor == 5:
        WN.blit(shield, (1190, 15))
        WN.blit(shield, (1190, 45))
        WN.blit(shield, (1190, 75))
        WN.blit(shield, (1190, 105))
        WN.blit(shield, (1190, 135))
    if armor == 4:
        WN.blit(shield, (1190, 15))
        WN.blit(shield, (1190, 45))
        WN.blit(shield, (1190, 75))
        WN.blit(shield, (1190, 105))
    if armor == 3:
        WN.blit(shield, (1190, 15))
        WN.blit(shield, (1190, 45))
        WN.blit(shield, (1190, 75))
    if armor == 2:
        WN.blit(shield, (1190, 15))
        WN.blit(shield, (1190, 45))
    if armor == 1:
        WN.blit(shield, (1190, 15))

def game_intro():
    intro = True
    while intro:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            intro = False
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        WN.blit(BG1, (0, 0))
        introtext1 = font3.render("Welcome to Falling Rocks!", 1, BLACK)
        introtext2 = font1.render("The objective of the game is to dodge the Falling Rocks.", 1, BLACK)
        introtext3 = font1.render("You can control your character using arrow keys.", 1, BLACK)
        introtext4 = font1.render("Please, press ENTER to start the game, P to pause or ESCAPE to exit.", 1, BLACK)
        WN.blit(introtext1, (100, 100))
        WN.blit(introtext2, (100, 300))
        WN.blit(introtext3, (100, 400))
        WN.blit(introtext4, (100, 500))
        pygame.display.update()


def pause():
    pauze = True
    while pauze:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            pauze = False
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        WN.blit(BG1, (0, 0))
        pause1 = font3.render("PAUSE", 1, BLACK)
        pause2 = font1.render("Press R to resume or ESCAPE to exit.", 1, BLACK)
        WN.blit(pause1, (100, 100))
        WN.blit(pause2, (100, 400))
        pygame.display.update()


def game_over():
    global score, health
    over = True
    while over:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            score = 1
            health = 5
            over = False
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            quit()
        WN.blit(BG1, (0, 0))
        overtext1 = font3.render("GAME OVER!", 1, BLACK)
        overtext2 = font1.render("You have been hit!", 1, BLACK)
        overtext3 = font1.render("Your score is: ", 1, BLACK)
        overscore = font1.render(str(score), 1, RED)
        overtext4 = font1.render("Press ENTER to play again or ESCAPE to exit.", 1, BLACK)
        WN.blit(overtext1, (100, 100))
        WN.blit(overtext2, (100, 300))
        WN.blit(overtext3, (100, 400))
        WN.blit(overscore, (365, 400))
        WN.blit(overtext4, (100, 500))
        pygame.display.update()


def redrawGameWindow():
    WN.blit(BG1, (0, 0))
    player.draw(WN)
    scoreboard = font1.render("Score: " + str(score), 1, WHITE)
    WN.blit(scoreboard, (15, 15))
    for rock in rocks:
        rock.draw(WN)
    if health < 5:
        for heartobj in heartsobj:
            heartobj.draw(WN)
    if health == 5 and armor < 5:
        for shieldobj in shieldsobj:
            shieldobj.draw(WN)
    if armor > 0:
        player.armordraw(WN)
    healtharmorStatus()
    pygame.display.update()


# OTHER VARIABLES
player = Player(YELLOW, 25)
rocks = []
heartsobj = []
shieldsobj = []
max_rocks = 10
health = 5
armor = 0
score = 1
# MAIN GAME LOOP
game_intro() # MAIN MENU
run = True
while run:
    CLOCK.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    # PLAYER KEYBOARD & MOUSE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player.x > 0:
            player.x -= player.vel
    if keys[pygame.K_RIGHT]:
        if player.x < WIDTH:
            player.x += player.vel
    if keys[pygame.K_UP]:
        if player.y > 0:
            player.y -= player.vel
    if keys[pygame.K_DOWN]:
        if player.y < HEIGHT:
            player.y += player.vel
    #player.x, player.y = pygame.mouse.get_pos() # in case you want to move your character with mouse instead of keyboard uncomment this line and comment lines in range(244, 255)
    # ADD HEALTH
    if len(heartsobj) < 1:
        if score % 50 == 0:
            if health < 5:
                heartsobj.append(AddHealth())
    for heartobj in heartsobj:
        if heartobj.y > -101 and heartobj.y < 800:
            heartobj.y += heartobj.vel
        else:
            heartsobj.pop(heartsobj.index(heartobj))
        # Health collision mechanics
        distance1 = math.hypot(heartobj.x - player.x, heartobj.y - player.y)
        if distance1 < heartobj.radius + player.radius:
            healthsound.play()
            health += 1
            heartsobj.pop(heartsobj.index(heartobj))
    # ADD SHIELD
    if len(shieldsobj) < 1:
        if score % 50 == 0:
            if health == 5:
                shieldsobj.append(AddShield())
    for shieldobj in shieldsobj:
        if shieldobj.y > -101 and shieldobj.y < 800:
            shieldobj.y += shieldobj.vel
        else:
            shieldsobj.pop(shieldsobj.index(shieldobj))
        # Shield collision mechanics
        distance1 = math.hypot(shieldobj.x - player.x, shieldobj.y - player.y)
        if distance1 < shieldobj.radius + player.radius:
            shieldsound.play()
            armor += 1
            shieldsobj.pop(shieldsobj.index(shieldobj))
    # ROCKS
    if len(rocks) < max_rocks:
        rocks.append(Rocks(BLACK))
    for rock in rocks:
        # Rocks falling
        if rock.y > -101 and rock.y < 800:
            rock.y += rock.vel
        else:
            rocks.pop(rocks.index(rock))
            score += 1
            # difficulty progression
            if score % 33 == 0:
                max_rocks += 1
        # Rock collision mechanics
        distance = math.hypot(rock.x - player.x, rock.y - player.y)
        if distance < rock.radius + player.radius:
            hitsound.play()
            if armor > 0:
                armor -= 1
            else:
                health -= 1
            rocks.pop(rocks.index(rock))
    # Pause loop
    if keys[pygame.K_p]:
        pause()
    # Game over loop
    if health == 0:
        game_over()

    redrawGameWindow()
pygame.quit()