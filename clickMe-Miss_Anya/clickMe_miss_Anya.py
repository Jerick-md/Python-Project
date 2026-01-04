import pygame as game
import os
import random

# Initialize Pygame
game.init()
os.chdir(os.path.dirname(__file__))

game.mixer.init()  # Initialize mixer
game.mixer.music.load("cute-music-26476.mp3")  # Load music file
game.mixer.music.play(-1)  # -1 makes it loop infinitely

# Window
WIDTH, HEIGHT = 500, 600
screen = game.display.set_mode((WIDTH, HEIGHT))
game.display.set_caption("AnyaCLick")

# Background
backgroundImg = game.image.load("backgroundimage.jpg")
backgroundImg = game.transform.scale(backgroundImg, (WIDTH, HEIGHT))

# Player/Target image
player_size = 100
playerImg = game.image.load("anya.png")
playerImg = game.transform.scale(playerImg, (player_size, player_size))

# Game variables
class Target:
    def __init__(self, image, speed):
        self.image = image
        self.speed = speed
        self.reset()
    
    def reset(self):
        self.x = random.randint(0, WIDTH - player_size)
        self.y = HEIGHT
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def move(self):
        self.y -= self.speed
        self.rect.topleft = (self.x, self.y)
        if self.y < -player_size:  # Reset if it goes off top
            self.reset()
            return True  # Indicates it was missed
        return False
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

target = Target(playerImg, speed=2)  # Starting speed

# Player health and score
health = 5

score = 0
font = game.font.SysFont(None, 36)

running = True
while running:
    screen.blit(backgroundImg, (0, 0))
    
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.MOUSEBUTTONDOWN:
            if target.rect.collidepoint(event.pos):
                score += 1
                target.speed += 0.5  # Increase speed slightly
                target.reset()
            else:
                health -= 1
                if health <= 0:
                    # Game over
                    screen.fill((0, 0, 0))
                    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
                    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
                    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 30))
                    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 10))
                    game.display.flip()
                    game.time.delay(3000)
                    running = False

    # Move target
    missed = target.move()
    if missed:
        health -= 1
        if health <= 0:
            # Game over
            screen.fill((0, 0, 0))
            game_over_text = font.render("GAME OVER", True, (255, 0, 0))
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 30))
            screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 10))
            game.display.flip()
            game.time.delay(3000)
            break

    # Draw target
    target.draw(screen)

    # Display score and health
    score_text = font.render(f"Score: {score}", True, (255, 255, 0))
    health_text = font.render(f"Health: {health}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))

    game.display.flip()
    game.time.delay(30)  # Control game speed

game.quit()
