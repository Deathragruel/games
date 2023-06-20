# This is a simple pong game as my first project.
import pygame, sys, time

class PongBoard():
    """ Simple class for the moving pong boards. """
    def __init__(self, rect_dimensions):
        self.rect = pygame.Rect(rect_dimensions)
        self.velocity = 10 
        self.moving_up = False
        self.moving_down = False
    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
    def update(self):
        if self.moving_up:
            self.rect.y -= self.velocity
        if self.moving_down:
            self.rect.y += self.velocity
        if self.rect.top <= 15:
            self.rect.top = 15
        if self.rect.bottom >= 585:
            self.rect.bottom = 585
class Ball():
    def __init__(self, startdir):
        self.rect_dimensions = (498, 292, 15, 15)
        self.rect = pygame.Rect(self.rect_dimensions)
        # The startdir is for changing the direction according to score
        # but the normalize is used to change direction of vector while keeping magnitude 1
        self.direction = pygame.math.Vector2(startdir).normalize()
        self.velocity = 8
    def draw(self):
        pygame.draw.rect(screen, 'Red', self.rect)
        if self.rect.right <= 0:
            self.rect = pygame.Rect(self.rect_dimensions)
        elif self.rect.left >= 1000:
            self.rect = pygame.Rect(self.rect_dimensions)
    def update(self):
        self.rect.x -= self.velocity * self.direction.x
        self.rect.y -= self.velocity * self.direction.y


def check_collisions(pb_1, pb_2, border_1, border_2, ball):
    # The parameter of reflect is the normal vector for reflection
    br = ball.rect
    pb = pb_1
    if pygame.Rect.colliderect(pb_1.rect, br):
        ball.direction = ball.direction.reflect((1, 0))
    if pygame.Rect.colliderect(pb_2.rect, br):
        ball.direction = ball.direction.reflect((1, 0))
    if pygame.Rect.colliderect(border_1, br) or pygame.Rect.colliderect(border_2, br):
        ball.direction = ball.direction.reflect((0, 1))
        if ball.rect.y < border_1.bottom and not 1000 <= ball.rect.x <= 0:
            ball.rect.y = border_1.bottom
        elif ball.rect.y > border_2.top and not 1000 <= ball.rect.x <= 0:
            ball.rect.y = border_2.top

def color_animation(r, g, b, r_change, g_change, b_change):
    screen.fill((r, g, b))
    r += r_change
    if r == 255:
        r_change *= -1
        g += g_change
    if g == 255:
        g_change *= -1
        b += b_change
    if b == 255:
        b_change *= -1
    if r == 0:
        r_change *= -1
    if g == 0:
        g_change *= -1
        g += g_change
    if b == 0:
        b_change *= -1
        b += b_change
    return r, g, b, r_change, g_change, b_change

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
ball = Ball(-1)
r, g, b = 1, 1, 1
r_change, g_change, b_change = 1, 1, 1

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
    # animate the bg_color
    color_animation(r,g,b,r_change,g_change,b_change)

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
    if ball.rect.right <= 0:
        score_2 += 1
    elif ball.rect.left >= 1000:
        score_1 += 1

    display_score(str(score_1), (450, 50, 30, 50))
    display_score(str(score_2), (525, 50, 30, 50))

    # Drawing stuff to the screen
    pygame.draw.line(screen, (255, 255, 255), (500, 15), (500, 585), width=2)
    pygame.draw.rect(screen, (255, 255, 255), border_1, width=1)
    pygame.draw.rect(screen, (255, 255, 255), border_2, width=1)
    pb_1.draw()
    pb_2.draw()
    ball.draw()
    
    # collisions
    check_collisions(pb_1, pb_2, border_1, border_2, ball)
    
    # Updates
    pb_1.update()
    pb_2.update()
    ball.update()

    pygame.display.update()
    clock.tick(60)