from constants import *
from player import *
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # setting up the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # setting both groups as containers
    Player.containers = (updatable, drawable)

    # initalize pygame
    pygame.init()
    # setting up the screen 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # for the fps initalize clock
    clock = pygame.time.Clock()
    # initalize a dt variable set to 0
    dt = 0
    # initalize a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # creating the game loop
    running = True
    while running :
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #update the method 
        updatable.update(dt)
            
        # fill the screen(Surface) with color black
        screen.fill("black")
       # draw the player
        for drawable_object in drawable:
            drawable_object.draw(screen)
        # refresh the screen
        pygame.display.flip()

        # at the end of the game loop initalize a tick() variable
        fps_timer = clock.tick(60)
        # converting miliseconds to seconds
        dt = fps_timer / 1000
        

if __name__ == "__main__":
    main()
