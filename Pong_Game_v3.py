import pygame
import random

# problems with paddle freezing and ball hitting on the top/bottom

pygame.init()
pygame.font.init()

# colors
Tan = (210, 180, 140)
Black = (0, 0, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)

# Paddle Info
paddle_Width = 10
paddle_Height = 80
paddle_spawning_yposition = 248  # using spawning positions to make it easier to reset
player_Paddle_Xposition = 450
player_Paddle_Yposition = paddle_spawning_yposition
computer_Paddle_Xposition = 50
computer_Paddle_Yposition = paddle_spawning_yposition
Velocity = 5.0
computer_paddle_Velocity = Velocity
player_paddle_Velocity = Velocity

# ball info
ball_radius = 10
ball_Spawning_Xposition = 250  # set as a constant to revert back to
ball_Spawning_Yposition = 288  # middle of the game screen, can't be a float
ball_Xposition = ball_Spawning_Xposition
ball_Yposition = ball_Spawning_Yposition

# velocity algorithm
sym = random.choice(['1', '-1'])
sign = int(sym)
sym_2 = random.choice(['1', '-1'])
sign_2 = int(sym_2)
ball_spawning_xVelocity = sign * 1
ball_spawning_yVelocity = sign_2 * 1

ball_xVelocity = ball_spawning_xVelocity
ball_yVelocity = ball_spawning_yVelocity

# window
display_width = 500
display_height = 550
win = pygame.display.set_mode((display_width, display_height))  # creates the game window size
pygame.display.set_caption("Pong")
win.fill(Tan)

ending = ".jpg"
# Clock
clock = pygame.time.Clock()
frame_rate = 60
clock.tick(frame_rate)  # 60 frames per second

# scoreboard info
computer_score = 0
computer_score_string = str(computer_score)
player_score = 0
player_score_string = str(player_score)
myfont = pygame.font.SysFont('arial', 60)
computer_score_surface = myfont.render(computer_score_string, False, (Blue))
player_score_surface = myfont.render(computer_score_string, False, (Blue))
# Scoreboard
win.blit(computer_score_surface, (100, 0))  # call the string name and then the position(x,y)
win.blit(player_score_surface, (350, 0))
pygame.draw.rect(win, Black, (0, 65, 500, 10))


# paddle

class paddle:
    def __init__(self, color, width, height, xposition, yposition, velocity):
        self.color = color
        self.width = width
        self.height = height
        self.xposition = xposition
        self.yposition = yposition
        self.velocity = velocity

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.xposition, self.yposition, self.width, self.height))


# ball
class ball:
    def __init__(self, color, radius, xposition, yposition):
        self.color = color
        self.radius = radius
        self.xposition = xposition
        self.yposition = yposition

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.xposition, self.yposition), self.radius)

#picture information
image_number = 1

image_directory = "/home/n8dogg/PycharmProjects/Neurofeedback_Game/Game_images/"
def takePic(x):
    image_number_string = str(x)
    pygame.image.save(win, image_directory + image_number_string + ".jpg") #use directory to control where pics save




TAKEPIC = 25
pygame.time.set_timer(TAKEPIC, 10) #change the frequency of event queue here, in milliseconds
# game loop
run = True
while (run):

    win.fill((Tan))  # or else rectangles grow. this is color tan
    for event in pygame.event.get():  # event is anything that happens from user, this gets a list of anything that happens
        if event.type == pygame.QUIT:  # if you hit the red quit X button
            run = False


    if (event.type == pygame.MOUSEMOTION):
        mouse_position = pygame.mouse.get_pos()
        if(mouse_position[1] < player_Paddle_Yposition):
            player_Paddle_Yposition -= player_paddle_Velocity
        if(mouse_position[1] > player_Paddle_Yposition):
            player_Paddle_Yposition += player_paddle_Velocity
    #keys = pygame.key.get_pressed()
    # player's paddle
    Player_Paddle = paddle(Red, paddle_Width, paddle_Height, player_Paddle_Xposition, player_Paddle_Yposition,
                           player_paddle_Velocity)
    paddle.draw(Player_Paddle, win)
    if (player_Paddle_Yposition >= 420):  # restricts movement of paddles-lower bound
        player_paddle_Velocity = 0
        if (event.type == pygame.MOUSEMOTION):
            mouse_position = pygame.mouse.get_pos()
            if (mouse_position[1] < player_Paddle_Yposition):
                player_paddle_Velocity = Velocity
                player_Paddle_Yposition -= player_paddle_Velocity

    if (player_Paddle_Yposition <= 75):  # restricts movement of paddles-upper bound
        player_paddle_Velocity = 0
        if (event.type == pygame.MOUSEMOTION):
            mouse_position = pygame.mouse.get_pos()
            if (mouse_position[1] > player_Paddle_Yposition):
                player_paddle_Velocity = Velocity
                player_Paddle_Yposition += player_paddle_Velocity

    # computer's paddle
    Computer_Paddle = paddle(Red, paddle_Width, paddle_Height, computer_Paddle_Xposition, computer_Paddle_Yposition,
                             computer_paddle_Velocity)
    paddle.draw(Computer_Paddle, win)
    computer_Paddle_Yposition += computer_paddle_Velocity  # this allows the paddle to run up and down in bounds
    if (computer_Paddle_Yposition >= 420):
        computer_paddle_Velocity = random.randrange(1, 7, 1) ##between 0.5 and 2
        computer_paddle_Velocity *= -1
    if (computer_Paddle_Yposition <= 75):
        computer_paddle_Velocity = -random.randrange(1, 7, 1) #randomizes the speed of paddle
        computer_paddle_Velocity *= -1

    # ball
    computer_ball = ball(Blue, ball_radius, ball_Xposition, ball_Yposition)
    ball.draw(computer_ball, win)

    # ball motion

    ball_Xposition += ball_xVelocity
    ball_Yposition += ball_yVelocity * 3

    # collisions
    if (ball_Yposition >= 500): #controls bouncing off of the bottom
        ball_yVelocity = -ball_yVelocity
    if (ball_Yposition <= 75):
        ball_yVelocity = -ball_yVelocity #controls bouncing off the top
    if (ball_Xposition == 440):
        if (ball_Yposition >= player_Paddle_Yposition and ball_Yposition <= player_Paddle_Yposition + 80):
            ball_xVelocity = -ball_xVelocity
    if (ball_Xposition == 70):
        if (ball_Yposition >= computer_Paddle_Yposition and ball_Yposition <= computer_Paddle_Yposition + 80):
            ball_xVelocity = -ball_xVelocity

        # scoring
    if (ball_Xposition >= 500):  # meaning the computer scored, resets ball position, velocity, paddle position
        ball_Xposition = ball_Spawning_Xposition
        ball_Yposition = ball_Spawning_Yposition
        sym = random.choice(['1', '-1'])
        sign = int(sym)
        sym_2 = random.choice(['1', '-1'])
        sign_2 = int(sym_2)
        ball_spawning_xVelocity = sign * 1
        ball_spawning_yVelocity = sign_2 * 1
        ball_yVelocity = ball_spawning_yVelocity
        ball_xVelocity = ball_spawning_xVelocity
        computer_Paddle_Yposition = paddle_spawning_yposition
        player_Paddle_Yposition = paddle_spawning_yposition

        computer_score = computer_score + 1

    if (ball_Xposition <= 0):  # meaning the player scored
        ball_Xposition = ball_Spawning_Xposition
        ball_Yposition = ball_Spawning_Yposition
        sym = random.choice(['1', '-1'])
        sign = int(sym)
        sym_2 = random.choice(['1', '-1'])
        sign_2 = int(sym_2)
        ball_spawning_xVelocity = sign * 1
        ball_spawning_yVelocity = sign_2 * 1
        ball_yVelocity = ball_spawning_yVelocity
        ball_xVelocity = ball_spawning_xVelocity
        computer_Paddle_Yposition = paddle_spawning_yposition
        player_Paddle_Yposition = paddle_spawning_yposition

        player_score = player_score + 1

    # Scoreboard
    computer_score_surface = myfont.render("{}".format(computer_score), False, Blue)
    player_score_surface = myfont.render("{}".format(player_score), False, Blue)

    win.blit(computer_score_surface, (100, 0))  # call the string name and then the position(x,y)
    win.blit(player_score_surface, (350, 0))
    pygame.draw.rect(win, Black, (0, 65, 500, 10))
    pygame.draw.rect(win, Black, (0, 500, 500, 10))  # bottom line


    if (event.type == TAKEPIC):
        takePic(image_number)
        image_number = image_number + 1
        mouse_position = pygame.mouse.get_pos()
        if (mouse_position[1] < player_Paddle_Yposition):
            player_Paddle_Yposition -= player_paddle_Velocity
        if (mouse_position[1] > player_Paddle_Yposition):
            player_Paddle_Yposition += player_paddle_Velocity
    if(event.type == TAKEPIC and event.type == pygame.MOUSEMOTION):
        mouse_position = pygame.mouse.get_pos()
        if (mouse_position[1] < player_Paddle_Yposition):
            player_Paddle_Yposition -= player_paddle_Velocity
        if (mouse_position[1] > player_Paddle_Yposition):
            player_Paddle_Yposition += player_paddle_Velocity
        takePic(image_number)
        image_number = image_number + 1
    clock.tick(frame_rate)  # controls frame rate--60 is a good number for smoothness
    pygame.display.update()  # need to refresh display so everything shows----this must happen after everything. ORDER MATTERS

