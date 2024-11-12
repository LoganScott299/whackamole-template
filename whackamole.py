import pygame
import random

def findSquare(x,y):
    return x // 32, y // 32

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        moleX, moleY = 0, 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            moleSquare = findSquare(moleX, moleY)
            screen.blit(mole_image, mole_image.get_rect(topleft=(moleX, moleY)))
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))
            for j in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, j), (640, j))
            if event.type == pygame.MOUSEBUTTONDOWN:
                eventX,eventY = event.pos
                eventSquare = findSquare(eventX, eventY)
                if eventSquare == moleSquare:
                    moleX = random.randrange(0,20+1) * 32
                    moleY = random.randrange(0, 16+1) * 32
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
