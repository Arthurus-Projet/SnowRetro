import pygame

pygame.init()
fenetre = pygame.display.set_mode((300,300))

nb_joysticks = pygame.joystick.get_count()
print(nb_joysticks)
if nb_joysticks > 0:
    manette_1 = pygame.joystick.Joystick(0)
    manette_1.init()
    pygame.joystick.init()


# manette de base
# saut touche : 2
# droite : 13
# gauche : 15


continuer = 1
while (continuer):


    for event in pygame.event.get():



        if event.type == pygame.JOYBUTTONDOWN:
            print(event.button)

        if event.type == pygame.JOYBUTTONDOWN and event.button == 3:
               print("manette 1")

        if event.type == pygame.JOYBUTTONDOWN and event.button == 3:
               print("manette 2")
    pygame.display.flip()


pygame.quit()
