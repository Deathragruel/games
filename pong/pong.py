# This is a simple pong game as my first project.
import pygame, sys, time

class PongBoard():
    """ Simple class for the moving pong boards. """
    def __init__(self, rect_dimensions):
        self.rect = pygame.Rect(rect_dimensions)
        self.speed = 10 
        self.moving_up = False
        self.moving_down = False
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect, width=3)
    def update(self):
        if self.moving_up:
            self.rect.y -= self.speed
        if self.moving_down:
            self.rect.y += self.speed
        if self.rect.top <= 15:
            self.rect.top = 15
        if self.rect.bottom >= 585:
            self.rect.bottom = 585
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(498, 292, 15, 15)
        self.x_direction = 1
        self.y_direction = 1
        self.speed = 5
    def draw(self, b, ball):
        pygame.draw.rect(screen, 'Red', self.rect)
        if self.rect.right <= 0:
            reset(b, ball)
        elif self.rect.left >= 1000:
            reset(b, ball)
    def update(self):
        self.rect.x -= self.speed * self.x_direction
        self.rect.y -= self.speed * self.y_direction

def check_collisions(pb_1, pb_2, border_1, border_2, ball):
    # last_touched indicates by which pong board the ball last bounced off off.
    if pygame.Rect.colliderect(pb_1.rect, ball.sprite.rect):
        ball.sprite.x_direction *= -1
    if pygame.Rect.colliderect(pb_2.rect, ball.sprite.rect):
        ball.sprite.x_direction *= -1
    if pygame.Rect.colliderect(border_1, ball.sprite.rect):
        ball.sprite.y_direction *= -1
    if pygame.Rect.colliderect(border_2, ball.sprite.rect):
        ball.sprite.y_direction *= -1

def reset(b, ball):
    b = Ball()
    b.add(ball)

# Basic setup
pygame.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# Classes initializations and rectangles
pb_1 = PongBoard((100, 25, 20, 80))
pb_2 = PongBoard((900, 495, 20, 80))
border_1 = pygame.Rect(0, 5, 1000, 10)
border_2 = pygame.Rect(0, 585, 1000, 10)
b = Ball()
ball = pygame.sprite.GroupSingle()
b.add(ball)

# For scores
score_1 = 0
score_2 = 0

def display_score(score, dimensions):
    # For putting text on the screen or numbers.
    font = pygame.font.SysFont(None, 64)
    font_surface = font.render(score, True, (255, 255, 255))
    font_rect = pygame.Rect(dimensions)
    screen.blit(font_surface, font_rect)

while True:
    # animate the bg_color later
    screen.fill((00, 00, 12))
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pb_1.moving_up = True
            if event.key == pygame.K_s:
                pb_1.moving_down = True
            if event.key == pygame.K_UP:
                pb_2.moving_up = True
            if event.key == pygame.K_DOWN:
                pb_2.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame. K_w:
                pb_1.moving_up = False
            if event.key == pygame.K_s:
                pb_1.moving_down = False
            if event.key == pygame.K_UP:
                pb_2.moving_up = False
            if event.key == pygame.K_DOWN:
                pb_2.moving_down = False
 
    # For displaying the scores
    if ball.sprite.rect.right <= 0:
        score_1 += 1
    elif ball.sprite.rect.left >= 1000:
        score_2 += 1

    display_score(str(score_1), (450, 50, 30, 50))
    display_score(str(score_2), (525, 50, 30, 50))

    # Drawing stuff to the screen
    pygame.draw.line(screen, (255, 255, 255), (500, 15), (500, 585), width=2)
    pygame.draw.rect(screen, (255, 255, 255), border_1, width=1)
    pygame.draw.rect(screen, (255, 255, 255), border_2, width=1)
    pb_1.draw()
    pb_2.draw()
    ball.sprite.draw(b, ball)
    
    # collisions
    check_collisions(pb_1, pb_2, border_1, border_2, ball)
    
    # Updates
    pb_1.update()
    pb_2.update()
    ball.update()

    pygame.display.update()
    clock.tick(60)
