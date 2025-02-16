
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

walls = []

# Ajouter les murs en haut et en bas
for x in range(0, 1280, wall_size):
    walls.append(pygame.Rect(x, 0, wall_size, wall_size))  # Haut
    walls.append(pygame.Rect(x, 720 - wall_size, wall_size, wall_size))  # Bas

# Ajouter les murs à gauche et à droite
for y in range(0, 720, wall_size):
    walls.append(pygame.Rect(0, y, wall_size, wall_size))  # Gauche
    walls.append(pygame.Rect(1280 - wall_size, y, wall_size, wall_size))  # Droite

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    for wall_rect in walls:
        screen.blit(wall, wall_rect.topleft)

    

    

    player_rect = pygame.Rect(player_pos.x, player_pos.y, 50, 50)


    keys = pygame.key.get_pressed()

    new_pos= player_pos.copy() #sauvegarder la position actuelle
    if keys[pygame.K_w]:
        new_pos.y -= 300 * dt
        current_player=player_down
    if keys[pygame.K_s]:
        new_pos.y += 300 * dt
        current_player=player_up
    if keys[pygame.K_a]:
        new_pos.x -= 300 * dt
        current_player=left_player
    if keys[pygame.K_d]:
        new_pos.x += 300 * dt
        current_player=right_player

    # Vérifier si la nouvelle position entre en collision avec un mur
    new_rect = pygame.Rect(new_pos.x, new_pos.y, 50, 50)
    if not any(new_rect.colliderect(wall) for wall in walls):
        player_pos = new_pos  # Mise à jour de la position si pas de collision


    # Dessiner le personnage (blit = coller une image)
    screen.blit(current_player, player_pos)


    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()