
from random import randint
import pygame

class snow:

    def __init__(self, hauteur, largeur):

        self.hauteur = hauteur
        self.largeur = largeur

        self.liste = []

        for tour in range(40):
            x = randint(0, self.largeur)
            y = randint(0, self.hauteur)
            couleur = (randint(230, 255), randint(230, 255), randint(230, 255))
            self.liste.append([x, y, couleur])



        # second nuage de point

        self.liste2 = []
        for tour in range(80):
            x = randint(0, self.largeur)
            y = randint(0, self.hauteur)
            couleur = (randint(230, 255), randint(230, 255), randint(230, 255))
            size = 4
            self.liste2.append([x, y, couleur, size])

        # troisième nuage de point

        self.liste3 = []
        for tour in range(150):
            x = randint(0, self.largeur)
            y = randint(0, self.hauteur)
            couleur = (randint(230, 255), randint(230, 255), randint(230, 255))
            size = 2
            self.liste3.append([x, y, couleur, size])


    def tour(self, fenetre, biais, biais_y):
        self.deplacement = [2, 2]

        for i in range(len(self.liste)):
            self.liste[i][0] += self.deplacement[0] + biais
            self.liste[i][1] += self.deplacement[1] + biais_y

            size = 6

            x, y  = self.liste[i][0] , self.liste[i][1]

            if x > self.largeur + size:
                self.liste[i][0] = - size - (x - (self.largeur + size))
            elif x < 0 - size: # quand la neige va à gauche
                self.liste[i][0] = self.largeur + x


            if y > self.hauteur + size: # quand la neige va en bas de l'écran
                self.liste[i][1] = (y - (self.hauteur + size)) - size
            elif y < 0 - size: # quand la neigne va en haut de l'écran
                self.liste[i][1] = self.hauteur + (self.hauteur - y)

            pygame.draw.circle(fenetre, self.liste[i][2], (self.liste[i][0], self.liste[i][1]), size, 0)


        # second nugage de points

        for i in range(len(self.liste2)):
            self.liste2[i][0] += self.deplacement[0] + biais
            self.liste2[i][1] += self.deplacement[1] + biais_y

            size = self.liste2[i][3]

            x, y  = self.liste2[i][0] , self.liste2[i][1]

            if x > self.largeur + size:
                self.liste2[i][0] = - size - (x - (self.largeur + size))
            elif x < 0 - size:
                self.liste2[i][0] = self.largeur + x


            if y > self.hauteur + size:
                self.liste2[i][1] = (y - (self.hauteur + size)) - size
            elif y < 0 - size:
                self.liste2[i][1] =  self.hauteur + (self.hauteur - y)

            pygame.draw.circle(fenetre, self.liste2[i][2], (self.liste2[i][0], self.liste2[i][1]), size, 0)


        # troisième nugage de points

        for i in range(len(self.liste3)):
            self.liste3[i][0] += int(self.deplacement[0] / 2) + int( 3/4 * biais)
            self.liste3[i][1] += int(self.deplacement[1] / 2) + int( 3/4 * biais_y)

            size = self.liste3[i][3]

            x, y  = self.liste3[i][0]  , self.liste3[i][1]

            if x > self.largeur + size:
                self.liste3[i][0] = - size - (x - (self.largeur + size))
            elif x < 0 - size:
                self.liste3[i][0] = self.largeur + x


            if y > self.hauteur + size:
                self.liste3[i][1] = (y - (self.hauteur + size)) - size
            elif y < 0 - size:
                self.liste3[i][1] =  self.hauteur + (self.hauteur - y)

            pygame.draw.circle(fenetre, self.liste3[i][2], (self.liste3[i][0], self.liste3[i][1]), size, 0)
