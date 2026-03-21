import pygame
from pygame.locals import *
import sys, pygame.mixer, time
from random import randint
import pygame.freetype # pour importer ses propres librairies
from copy import deepcopy

# import class :
from animations import *
from joueur import *
from menu import *
from neige import *
from pluie import *

# import fonction crée :
from fonctions_reseau import *

# import les maps :
from le_generator_map import *


pygame.init()
pygame.display.set_caption('SnowRetro')
clock = pygame.time.Clock()

# musique :
"""
pygame.mixer.music.load('image\musique\m1.wav')
pygame.mixer.music.set_volume(0.0)          # réglage du volume (facultatif)
pygame.mixer.music.play(-1)                 # joue le morceau en boucle
"""
#musique_mort = pygame.mixer.Sound('image\musique\mort.wav')

taille_bloc = 64
taille_joueur_x = 32
taille_joueur_y = 32

frame = 0


# partie pygame :
coef = 1
taille = largeur, hauteur = 1000 * coef, 576 * coef
print(largeur, hauteur)
fenetre = pygame.display.set_mode(taille)

perso = pygame.image.load('image/perso.png').convert_alpha()

Snow = snow(hauteur, largeur)
pluie = rain(hauteur, largeur)

perso_anime = animation(100, 32, 32, 5)

# fond :
fond = pygame.image.load('image/fond.png')
fond = pygame.transform.scale(fond, (1800 * 2 * coef, 576 * coef))

# acceuil :
home = pygame.image.load("image/home.jpg")
home = pygame.transform.scale(home, (1000, 576))

# bloc herbe :
bloc = pygame.image.load('image/bloc.png').convert_alpha()
bloc = pygame.transform.scale(bloc, (taille_bloc, taille_bloc))

# bloc terre :
terre = pygame.image.load('image/terre.png').convert_alpha()
terre = pygame.transform.scale(terre, (taille_bloc, taille_bloc))

# bloc haut :
bloc_haut = pygame.image.load("image/haut.png").convert_alpha()
bloc_haut = pygame.transform.scale(bloc_haut, (taille_bloc, taille_bloc))

# bloc milieu :
bloc_milieu = pygame.image.load("image/mileu.png").convert_alpha()
bloc_milieu = pygame.transform.scale(bloc_milieu, (taille_bloc, taille_bloc))

# bloc bas :
bloc_bas = pygame.image.load("image/bas.png").convert_alpha()
bloc_bas = pygame.transform.scale(bloc_bas, (taille_bloc, taille_bloc))

# nuage géré avec une classe pour l'animation :
image_nuage = pygame.image.load("image/nuage.png").convert_alpha()
test_nuage = animation( 200, 340, 142, 4)

nuage2 = pygame.image.load("image/nuage_2.png").convert_alpha()
nuage2_class = animation(300, 250, 110, 4)

# couleurs :
blanc = (255, 255, 255)
noir = (0, 0, 0)
rouge = (255, 0, 0)
bleu = (0, 0, 255)
mystère = (randint(0, 255), randint(0, 255), randint(0, 255))

print(mystère)
#mystère = (121, 96, 210)




# test si le jouer peut sauter :
def collision_haut(map, position_X, position_Y, perso_class):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != " ":
                Y = y * taille_bloc + perso_class.biais_y
                X = x * taille_bloc + perso_class.biais_x

                if Y <= position_Y  <=  Y + taille_bloc  and X <= position_X <=  X + taille_bloc:
                    if  X <= position_X + 1 <=  X + taille_bloc:
                        return True

                if Y <= position_Y <=  Y + taille_bloc  and X <= position_X + taille_joueur_x <=  X + taille_bloc:
                    if   X <= position_X + taille_joueur_x -1 <=  X + taille_bloc:
                        return True
    return False

# sert à tester si le jouer doit tomber ou si il est sur le sol :
def collision_bas(map, position_X, position_Y, perso_class):
    for y in range(len(map)):
        for x in range(len(map[y])):

            if map[y][x] != ' ':
                Y = y * taille_bloc + perso_class.biais_y
                X = x * taille_bloc + perso_class.biais_x

                if Y <= position_Y + taille_joueur_y <=  Y + taille_bloc  and X <= position_X <=  X + taille_bloc:
                    if  X <= position_X + 1 <=  X + taille_bloc: # bloc sur bloc
                        return True

                if Y <= position_Y + taille_joueur_y <=  Y + taille_bloc  and X <= position_X + taille_joueur_x <=  X + taille_bloc:
                    if   X <= position_X + taille_joueur_x -1 <=  X + taille_bloc:
                        return True
    return False


############ 2 FONCTIONS POUR TESTER SI LE JOUEUR PEUT SE DEPLACER AU NOUVEL ENDROIT ############


# REGARDE si la nouvelle position touche quelque chose :
def around_collision(position_joueur_x, position_joueur_y, bloc_x, bloc_y, taille_objet):
    around = [[1, 1], [-1, -1], [-1, 1], [1, -1]]

    for a in around:
        if False == (bloc_x <= position_joueur_x + a[0]  <= bloc_x + taille_objet and bloc_y <= position_joueur_y + a[1] <= bloc_y + taille_objet):
            return False
    return True



# FONCTION qui test si il y a une collision, c'est à dire
# si le joueur touche un mur :

def collision(map, position_X, position_Y, perso_class, taille_objet_bloc, joueur):
    value_Y = [0, joueur, 0, joueur]
    value_X = [0, 0, joueur, joueur]

    for y in range(len(map)):
        for x in range(len(map[y])):

            if map[y][x] != ' ':
                Y = (y * taille_objet_bloc) + perso_class.biais_y
                X = (x * taille_objet_bloc) + perso_class.biais_x

                for i in range(4):
                    if Y < position_Y + value_Y[i] <  Y + taille_objet_bloc  and X < position_X + value_X[i] <  X + taille_objet_bloc:
                        if around_collision(position_X  + value_X[i] , position_Y + value_Y[i], X, Y, taille_objet_bloc):
                            return True
    return False



##########################################################################################################
#                                             PYGAME                                                     #
##########################################################################################################



def jeu(map, fenetre):
    perso_class = Player(map, taille_bloc)



    """nb_joysticks = pygame.joystick.get_count()
    if nb_joysticks > 0:
        manette_1 = pygame.joystick.Joystick(0)
        manette_1.init()
        pygame.joystick.init()"""



    speed = 11 #vitesse déplacement droite ou gauche


    etat_jump = False

    stat_deplacement_droite = False
    stat_deplacement_gauche = False


    #variable pour l'orientation du personnage
    gauche_boolean = 0

    valeur_saut_par_frame = 16
    nombre_de_jump = 10
    jump = 0

    haut = False
    second_jump = 1
    time_long_saut = 100
    saut_long = False

    can_shoot = True
    count = 0
    number = 200


    pygame.key.set_repeat(1, 1) #truque à mettre pour rester appuyer sur une touche

    time_next_frame = 50
    bool_marche = False

    continuer = True
    while continuer:

        count -= 1

        if count < 0:
            can_shoot = True

        dt = clock.tick(50 * coef)
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN  :


                ################## CLAVIER ##################
                if event.key == K_ESCAPE:
                    fenetre = pygame.display.set_mode(taille)
                # Gestion du saut :
                if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_z]: # w = z
                    if collision_bas(map, perso_class.perso_x, perso_class.perso_y, perso_class) :
                        etat_jump = True
                        jump = nombre_de_jump

                        time_long_saut = 100
                        saut_long = True

                        haut = True
                        second_jump = 1

                    else:
                        if haut == False and second_jump == 1:
                            print("JUMP")

                            jump += 10
                            etat_jump = True

                            haut = True
                            second_jump -= 1

                    time_long_saut -= dt
                    if time_long_saut <= 0 and saut_long:
                        jump += 5
                        saut_long = False


                # DROITE
                if pygame.key.get_pressed()[pygame.K_d]:
                    stat_deplacement_droite = True
                    gauche_boolean = 0
                    bool_marche = True
                    perso_class.orientation_droite = True

                # GAUCHE
                if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_q]: # GAUCHE Q
                    stat_deplacement_gauche = True
                    gauche_boolean = 1
                    bool_marche = True
                    perso_class.orientation_droite = False

                if pygame.key.get_pressed()[K_UP]:
                    perso_class.biais_y += 8
                if pygame.key.get_pressed()[K_DOWN]:
                    #if  collision_bas(map, perso_class.perso_x, perso_class.perso_y, perso_class) == False:
                    perso_class.biais_y -= 8

                if event.key == pygame.K_LSHIFT or event.key == pygame.K_SPACE or event.key == pygame.K_LEFT:
                    print("shift")
                    if can_shoot:
                        perso_class.create_balle()
                        can_shoot = False
                        count = 6

            # Quand on lève le doigt d'une touche clavier
            if event.type == KEYUP:
                if event.key == pygame.K_d:
                    stat_deplacement_droite = False
                    bool_marche = False
                    gauche_boolean = 0

                if event.key == pygame.K_a or event.key == pygame.K_q: # GAUCHE Q
                    stat_deplacement_gauche = False
                    bool_marche = False
                    gauche_boolean = 1

                if event.key == pygame.K_w or event.key == pygame.K_z:
                    time_long_saut = 100
                    haut = False
            #if event.type == pygame.MOUSEBUTTONDOWN:

            boutton = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            if boutton[2]:
                map = perso_class.new_block( map, pos, 'x')
            elif boutton[0]:
                map = perso_class.new_block( map, pos, ' ')

            ########## MANETTE #########

            # quand on appui sur la manette
            if event.type == pygame.JOYBUTTONDOWN :
                if event.button == 13: # droite
                    stat_deplacement_droite = True
                    gauche_boolean = 0
                if event.button == 15: # gauche
                     stat_deplacement_gauche = True
                     gauche_boolean = 1
                if event.button == 2: # bouton saut
                    if collision(map, perso_class.perso_x, perso_class.perso_y - valeur_saut_par_frame, taille_bloc, 32) == False :
                        etat_jump = True
                        jump = nombre_de_jump

            # quand on lève la manette
            if event.type == pygame.JOYBUTTONUP :
                if event.button == 13: # droite
                    stat_deplacement_droite = False
                if event.button == 15: # gauche
                     stat_deplacement_gauche = False

            ############################################################################################################
            ################################### FIN GESTION TOUCHE #####################################################
            ############################################################################################################


        # Teste si le joueur tombe en bas de la map, si il tombe il respawn
        perso_class.player_fall(hauteur, map)





        """for trr in range(100_000):
            fre = 2 * 412"""

        # Initialisation du biais neige pour que la neige est une forme différente en fonction des mouvements du joueur
        BIAIS_NEIGE = 0

        if stat_deplacement_gauche:
            if collision(map, perso_class.perso_x - speed , perso_class.perso_y, perso_class, taille_bloc, 32) == False:
                if 185 <= perso_class.perso_x <= 312:
                    perso_class.perso_x -= speed
                else:
                    perso_class.biais_x += speed
                    BIAIS_NEIGE = speed

        if stat_deplacement_droite:
            if collision(map, perso_class.perso_x + speed , perso_class.perso_y, perso_class, taille_bloc, 32) == False: # droite D
                if 182 <= perso_class.perso_x  <= 311:
                    perso_class.perso_x += speed
                else:
                    perso_class.biais_x -= speed
                    BIAIS_NEIGE = -speed


        BIAIS_NEIGE_Y = 0

        # gère les saut
        if jump > 0 and etat_jump == True:
            if collision_haut(map, perso_class.perso_x, perso_class.perso_y - valeur_saut_par_frame, perso_class) == False:

                if perso_class.perso_y  < 100:
                    perso_class.biais_y += valeur_saut_par_frame
                    BIAIS_NEIGE_Y = valeur_saut_par_frame
                else:
                    perso_class.perso_y -= valeur_saut_par_frame
                #perso_class.perso_y -= valeur_saut_par_frame

                jump -= 1
                speed = 11
            else:
                jump = 0
                etat_jump = False
        else:
            etat_jump = False
            speed = 11

        # quand le perso tombe
        if etat_jump == False:
            if collision_bas(map, perso_class.perso_x, perso_class.perso_y, perso_class) == False:
                if perso_class.perso_y > 300:
                    perso_class.biais_y -= 8
                    BIAIS_NEIGE_Y -= 8
                else:
                    perso_class.perso_y += 8
                #perso_class.perso_y += 8



        ecrire('perso.txt', str(perso_class.perso_x - perso_class.biais_x) + " " + str(perso_class.perso_y - perso_class.biais_y))


        fenetre.blit(fond, (0, 0))

        # affiche les animations des nuages :
        fenetre.blit(nuage2, (1050 + perso_class.biais_x /(2.5), 30 + perso_class.biais_y), nuage2_class.get_mask(dt))
        fenetre.blit(image_nuage, (800 + perso_class.biais_x / 2, 50  + perso_class.biais_y), test_nuage.get_mask(dt))

        # affiche les animations de la neige
        Snow.tour(fenetre, BIAIS_NEIGE, BIAIS_NEIGE_Y)

        # dessine la map :
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == 'x':
                    fenetre.blit(bloc, (x * taille_bloc + perso_class.biais_x, y * taille_bloc + perso_class.biais_y))
                elif map[y][x] == "h":
                    fenetre.blit(bloc_haut, (x * taille_bloc + perso_class.biais_x, y * taille_bloc + perso_class.biais_y))
                elif map[y][x] == "m":
                    fenetre.blit(bloc_milieu, (x * taille_bloc + perso_class.biais_x, y * taille_bloc + perso_class.biais_y))
                elif map[y][x] == "b":
                    fenetre.blit(bloc_bas, (x * taille_bloc + perso_class.biais_x, y * taille_bloc + perso_class.biais_y))


        fenetre.blit(perso, (perso_class.perso_x, perso_class.perso_y), perso_anime.get_mask_for_multiple_states(gauche_boolean))


        Xtest, Ytest = lire("enemi.txt")
        if Xtest!= -1 and Ytest != -1:
            X, Y = Xtest, Ytest
        fenetre.blit(perso, (X + perso_class.biais_x, Y), pygame.Rect(1 * 32, 0, 32, 32))


        perso_class.avancement_balles()

        I = []
        for i in range(len(perso_class.balles)):
            balle_x = perso_class.balles[i][0] + perso_class.biais_x
            balle_y = perso_class.balles[i][1] + perso_class.biais_y

            if collision(map, balle_x, balle_y, perso_class, taille_bloc, perso_class.taille_balle):
                print("suppresision")
                I.append(perso_class.balles[i])

        perso_class.remove_balle(I)




        for balle in perso_class.balles:
            pygame.draw.rect(fenetre, rouge, (balle[0] + perso_class.biais_x, balle[1] + + perso_class.biais_y, perso_class.taille_balle, perso_class.taille_balle))

        fps = str(int(clock.get_fps()))
        menu.texte( fps, (255, 255, 0), 20, 20, 30)

        if bool_marche:
            perso_anime.set_time(dt)



        if perso_class.dead:
            #musique_mort.play()
            perso_class.reset()

        print("perso_class.biais_x", perso_class.biais_x)
        print("perso_class.perso_x", perso_class.perso_x)

        pygame.display.update()
    write_map(map)

    




################### MENU ############################

map = level_1()
map2 = level_2()
map3 = level_3()
map4 = level_4()

bleu_clair = (0, 189, 255)
orange = (255, 153, 33)
rose = (244, 146, 181)

menu = home_menu('image/police/Dico.ttf', fenetre, 50)

continuer = True
while continuer:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN  :
            ################## CLAVIER ##################
            if event.key == K_ESCAPE:
                fenetre = pygame.display.set_mode(taille)

            ################## SOURIS ##################
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if 288 <= pos[0] <= 720 and 133 <= pos[1] <= 197:
                #ecrire('perso.txt', "108" + " " + "224")
                jeu(deepcopy(level_1()), fenetre)
            if 288 <= pos[0] <= 720 and 217 <= pos[1] <= 280:
                jeu(deepcopy(level_2()), fenetre)
            if 288 <= pos[0] <= 720 and 296 <= pos[1] <= 357:
                jeu(deepcopy(level_3()), fenetre)
            if 288 <= pos[0] <= 720 and 372 <= pos[1] <= 434:
                #ecrire('perso.txt', "203" + " " + "160")
                jeu(deepcopy(level_4()), fenetre)


    fenetre.blit(home, (0, 0))

    pos = pygame.mouse.get_pos()

    menu.texte_qui_varie((288, 720), (133, 197), rose, bleu_clair, 446, 143, 40, "Map 1", pos)
    menu.texte_qui_varie((288, 720), (217, 280), rose, bleu_clair, 446, 224, 40, "Map 2", pos)
    menu.texte_qui_varie((288, 720), (296, 357), rose, bleu_clair, 446, 302, 40, "Map 3", pos)
    menu.texte_qui_varie((288, 720), (372, 434), rose, bleu_clair, 446, 378, 40, "Map 4", pos)

    Snow.tour(fenetre, 0, 0)

    pygame.display.update()


pygame.quit()
