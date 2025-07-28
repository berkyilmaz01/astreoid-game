from constants import *
import pygame

# initalize pygame
pygame.init()
# setting up the screen 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # creating the game loop
    running = True
    while running :

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # fill the screen(Surface) with color black
        screen.fill("black")
        # refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
