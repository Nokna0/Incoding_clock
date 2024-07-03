# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
 
# Set the height and width of the screen
size   = [512, 512]
screen = pygame.display.set_mode(size)
  
pygame.display.set_caption("BOOOOOOM")
  
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:
  
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we`` will use all CPU we can.
    clock.tick(10)
    
    # Main Event Loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
  
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
      
    # Clear the screen and set the screen background
    screen.fill(BLACK)
    
    pygame.draw.rect(screen, WHITE, [64, 64, 384, 384], 5)
    pygame.draw.line(screen, WHITE, [64, 128], [448-5, 128], 5)
    pygame.draw.line(screen, WHITE, [128, 128], [128, 448-5], 5) # x좌표 절반으로 낮추기 (그냥 알아서 알아들어)


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()