from math import floor



class Player:


    def __init__(self, map, taille_bloc):
        self.taille_bloc = taille_bloc

        # attribut pour les balles :
        self.balles = []
        self.enemi_balles = []
        self.orientation_droite = True # le joueur est tourné vers la droite (utile pour le lancer de balle)
        self.taille_balle = 20
        self.number_dead = -1
        self.number_dead_enemi = -1

        self.give_position_player(map)
        self.reset()

    def give_position_player(self, map):
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == 'p':
                    self.perso_x, self.perso_y = (x * self.taille_bloc), (y * self.taille_bloc)
                    self.perso_x_respawn = self.perso_x
                    self.perso_y_respawn = self.perso_y
                    self.retire_p_de_map(map, y)
                    #self.save_biais_x = -(self.taille_bloc * x) + (self.taille_bloc * 5)
                    self.save_biais_x = 0
                    self.save_biais_y = 0


    def retire_p_de_map(self, map, y):
        l = []
        for caractère in map[y]:
            if caractère != 'p':
                l.append(caractère)
            else:
                l.append(' ')
        l = ''.join(l)
        map[y] = l


    def reset(self): # quand on meurt on apelle cette fonction
        self.perso_y = self.perso_y_respawn
        self.perso_x = self.perso_x_respawn

        self.dead = False

        self.biais_x = self.save_biais_x
        self.biais_y = self.save_biais_y

        self.number_dead += 1


    def player_fall(self, height, map):
        if self.perso_y - self.biais_y > len(map) * 64:
            self.dead = True

    def pos_souris(self, map, pos):
        x = pos[0]
        y = pos[1]
        return floor( (x - self.biais_x) / 64), floor( (y - self.biais_y) / 64)

    def change_map(self, map, x, y, type_block):
        liste = list(map[x])
        liste[y] = type_block
        new_str = ''.join(liste)
        map[x] = new_str
        return map

    def check_is_xy_exist_in_map(self, map, x, y):
        if 0 <= x < len(map):
            if 0 <= y < len(map[x]):
                return True
        return False

    def new_block(self, map, pos, type_block):
        y, x = self.pos_souris(map, pos)
        if self.check_is_xy_exist_in_map(map, x, y):
            return self.change_map(map, x, y, type_block)
        return map

    # gère l'avancements des balles tour par tout
    def avancement_balles(self, y_map):

        balles_dead = []
        balles_dead_enemi = []
        vitesse = 9
        for i in range(len(self.balles)):
            if self.balles[i][2] == "d": # si la balle va à doite
                self.balles[i][0] += vitesse
            else:
                self.balles[i][0] -= vitesse

            if self.balles[i][0] < 0:
                balles_dead.append(self.balles[i])

            if self.balles[i][0] > y_map:
                balles_dead.append(self.balles[i])
                

        for i in range(len(self.enemi_balles)):
            if self.enemi_balles[i][2] == "d": # si la balle va à doite
                self.enemi_balles[i][0] += vitesse
            else:
                self.enemi_balles[i][0] -= vitesse

            
            if self.enemi_balles[i][0] < 0:
                balles_dead_enemi.append(self.enemi_balles[i])

            if self.enemi_balles[i][0] > y_map:
                balles_dead_enemi.append(self.enemi_balles[i])
            


        for elem in balles_dead:
            self.balles.remove(elem)

        for elem in balles_dead_enemi:
            self.enemi_balles.remove(elem)
                    



    # quand on tire une balle
    def create_balle(self):
        if len(self.balles) < 5:
            if self.orientation_droite:
                self.balles.append([self.perso_x - self.biais_x, self.perso_y - self.biais_y, "d"])
            else:
                self.balles.append([self.perso_x - self.biais_x, self.perso_y - self.biais_y, "g"])

    def remove_balle(self, I):
        for elem in I:
            self.balles.remove(elem)

