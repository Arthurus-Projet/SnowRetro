import pygame
import pygame.freetype



class home_menu:


    def __init__(self, police, fenetre, size):
        self.police = police
        self.fenetre = fenetre
        self.size = size
        pygame.init()
        pygame.font.init()
        self.update_font(police, size)


    def update_font(self, police, size):
        self.font = pygame.freetype.Font(police , size)

    def afficher_texte(self, texte, x, y):
        self.fenetre.blit(texte, (x, y))

    def texte(self, texte, couleur, x, y, taille_texte):
        self.update_font(self.police, self.size)
        txt, r = self.font.render(texte, couleur)
        self.afficher_texte(txt, x, y)

    def texte_qui_varie(self, borne_x, borne_y, couleur1, couleur2, x, y, taille, texte, pos):
        inf_x = borne_x[0]
        sup_x = borne_x[1]
        inf_y, sup_y = borne_y[0], borne_y[1]

        if inf_x <= pos[0] <= sup_x and inf_y <= pos[1] <= sup_y:

            self.texte(texte, couleur1, x, y, taille)
        else:
            self.texte(texte, couleur2, x, y, taille)
