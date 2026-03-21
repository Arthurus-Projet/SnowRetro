from random import randint
import pygame

class rain:


    def __init__(self, hauteur, largeur):

        self.hauteur = hauteur
        self.largeur = largeur


        self.deplacements = [0, 5]
        self.liste = []

        for x in range(50):
            couleur = (0, randint(147, 167), 255) #157
            x, y = randint(0, largeur), randint(0, hauteur)
            longueur_pluie = randint(80, 120)
            self.liste.append([x, y, couleur, longueur_pluie])





    def tour(self, fenetre):


        for i in range(len(self.liste)):
            self.liste[i][0] += self.deplacements[0]
            self.liste[i][1] += self.deplacements[1]

            x = self.liste[i][0]
            y = self.liste[i][1]

            longueur_pluie = self.liste[i][3]

            if x > self.largeur + longueur_pluie:
                self.liste[i][0] = - longueur_pluie
            elif x < 0 - longueur_pluie:
                self.liste[i][0] = self.largeur + longueur_pluie


            if y > self.hauteur + longueur_pluie:
                self.liste[i][1] = - longueur_pluie
            elif y < 0 - longueur_pluie:
                self.liste[i][1] = self.hauteur + longueur_pluie


            couleur = self.liste[i][2]

            pygame.draw.rect(fenetre, couleur, (self.liste[i][0], self.liste[i][1], 5, longueur_pluie), 3)
