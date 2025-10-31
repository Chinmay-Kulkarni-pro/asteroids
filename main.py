import pygame
from constants import  *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock_object = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0),rect=None, special_flags=0)

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock_object.tick(60)/1000

        updatable.update(dt)

if __name__ == "__main__": 
    main()
