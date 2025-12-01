import pygame
import sys
from constants import  *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_state, log_event

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0),rect=None, special_flags=0)

        for d in drawable:
            d.draw(screen)

        log_state()

        pygame.display.flip()
        dt = clock_object.tick(60)/1000

        updatable.update(dt)


        for ast in asteroids:
            if ast.circles_collision(player):
                print("Game Over!")
                sys.exit()
        
        for ast in asteroids:
            for shot in shots:
                if ast.circles_collision(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    ast.split()





if __name__ == "__main__": 
    main()
