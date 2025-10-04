import pygame
from constants import *
from player import Player

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    pygame.init()
    all_updatable = pygame.sprite.Group()
    all_drawable = pygame.sprite.Group()
    Player.containers = all_updatable, all_drawable


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)



    
    infinite_loop = True
    while infinite_loop:
        dt = clock.tick(60) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        all_updatable.update(dt)


        screen.fill((0, 0, 0))
        for sprite in all_drawable:
            sprite.draw(screen)
            
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()