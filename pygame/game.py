import pygame
import random
import pygame.mixer


# Define colors

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)


# Class represents ball, derives from Sprite class in pygame

class Block(pygame.sprite.Sprite):
    # Constructor. Pass in the color of the block and its x and y pos.
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


# Initialize Pygame
pygame.init()

pygame.mixer.init(44100, -16, 2, 2048)
winsound = pygame.mixer.Sound('8516.wav')
collectsound = pygame.mixer.Sound('8516.wav')

# Set width and height of screen

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Block Attack!')

# List of sprites. Each block is added to this list. List is managed by RenderPlain()

block_list = pygame.sprite.RenderPlain()

# List of every sprite

all_sprites_list = pygame.sprite.RenderPlain()

for i in range(50):
    # create instance of block
    block = Block(black, 20, 14)

    # set random location for the block
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)

# Create red player block
player = Block(red, 20, 15)
all_sprites_list.add(player)

done = False

clock = pygame.time.Clock()

score = 0

# -------Main Program Loop-------

while done == False:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear screen
    screen.fill(white)

    # Get current mouse position. This returns the position as a list of two numbers
    pos = pygame.mouse.get_pos()

    # Fetch x and y out of list, like letters out of strung, set player object
    # to location of the mouse

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    # Check if player block has collidied with anything...were still in a loop
    block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    # Check list of collisions.
    if len(block_hit_list) > 0:
        score += len(block_hit_list)
        print(score)
        collectsound.play()
    elif score == 50:
        print('YOU WIN!!\n')
        done = True
        winsound.play()

    # Draw all the sprites
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(10)

    # Update screen
    pygame.display.flip()

pygame.quit()
