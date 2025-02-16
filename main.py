
# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
collision=True
running = True
dt = 1

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
wall_size = 50  # Taille du mur


right_player= pygame.image.load("C:/Users/ayman/OneDrive/Desktop/kenney_sokoban-pack/PNG/Default_size/Player/player_11.png")
left_player= pygame.image.load("C:/Users/ayman/OneDrive/Desktop/kenney_sokoban-pack/PNG/Default_size/Player/player_20.png")
player_up= pygame.image.load("C:/Users/ayman/OneDrive/Desktop/kenney_sokoban-pack/PNG/Default_size/Player/player_07.png")
player_down= pygame.image.load("C:/Users/ayman/OneDrive/Desktop/kenney_sokoban-pack/PNG/Default_size/Player/player_08.png")

wall=pygame.image.load("C:/Users/ayman/OneDrive/Desktop/kenney_sokoban-pack/PNG/Default_size/Crates/crate_43.png")




right_player= pygame.transform.scale(right_player, (80,80))
left_player= pygame.transform.scale(left_player, (80,80))
player_up= pygame.transform.scale(player_up, (80,80))
player_down= pygame.transform.scale(player_down, (80,80))


current_player=right_player

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for x in range(0, 1280, wall_size):
        screen.blit(wall, (x, 0))  # Mur en haut
        screen.blit(wall, (x, 720 - wall_size))  # Mur en bas

    # Dessiner les murs à gauche et à droite
    for y in range(0, 720, wall_size):
        screen.blit(wall, (0, y))  # Mur à gauche
        screen.blit(wall, (1280 - wall_size, y))  # Mur à droite

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
        current_player=player_down
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
        current_player=player_up
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        current_player=left_player
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        current_player=right_player


    # Dessiner le personnage (blit = coller une image)
    screen.blit(current_player, player_pos)


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()