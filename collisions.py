


# TESTE si le jouer peut sauter
def collision_haut(map, position_X, position_Y):
    for y in range(len(map)):
        for x in range(len(map[y])):

            if map[y][x] == "x" or map[y][x] == "t":
                Y = y * taille_bloc + biais_y
                X = x * taille_bloc + biais_x

                if Y <= position_Y  <=  Y + taille_bloc  and X <= position_X <=  X + taille_bloc:
                    if  X <= position_X + 1 <=  X + taille_bloc:
                        return True

                if Y <= position_Y <=  Y + taille_bloc  and X <= position_X + taille_joueur_x <=  X + taille_bloc:
                    if   X <= position_X + taille_joueur_x -1 <=  X + taille_bloc:
                        return True
    return False

# SERT à tester si le jouer doit tomber ou si il est sur le sol :
def collision_bas(map, position_X, position_Y):
    for y in range(len(map)):
        for x in range(len(map[y])):

            if map[y][x] == "x":
                Y = y * taille_bloc + biais_y
                X = x * taille_bloc + biais_x

                if Y <= position_Y + taille_joueur_y <=  Y + taille_bloc  and X <= position_X <=  X + taille_bloc:
                    if  X <= position_X + 1 <=  X + taille_bloc: # bloc sur bloc
                        return True

                if Y <= position_Y + taille_joueur_y <=  Y + taille_bloc  and X <= position_X + taille_joueur_x <=  X + taille_bloc:
                    if   X <= position_X + taille_joueur_x -1 <=  X + taille_bloc:
                        return True
    return False


############ 3 FONCTIONS POUR TESTER SI LE JOUEUR PEUT SE DEPLACER AU NOUVEL ENDROIT ############


# REGARDE si la nouvelle position touche quelque chose :

def not_collision2(map, position_X, position_Y, X, Y):
    value_Y = [0, taille_joueur_y, 0, taille_joueur_y]
    value_X = [0, 0, taille_joueur_y, taille_joueur_y]

    for i in range(4):
        if Y <= position_Y + value_Y[i] <=  Y + taille_bloc  and X <= position_X  + value_X[i] <=  X + taille_bloc:
            return False

    return True

# REGARDE autour pour etre sur que le joueur peut
# faire un mouvement autorisé, et non pas à l'intétieur d'un mur

def around(map, position_X, position_Y, X, Y):
    pos = [[-1, -1], [1, -1], [1, 1], [-1, 1]]

    for p in pos:
        x = p[0]
        y = p[1]

        if not_collision2(map, position_X + x, position_Y + y, X, Y) == True:
            return False

    return True

# FONCTION qui test si il y a une collision, c'est à dire
# si le joueur touche un mur :

def not_collision(map, position_X, position_Y):
    value_Y = [0, taille_joueur_y, 0, taille_joueur_y]
    value_X = [0, 0, taille_joueur_y, taille_joueur_y]

    for y in range(len(map)):
        for x in range(len(map[y])):

            if map[y][x] == "x"  or map[y][x] == "t":
                Y = (y * taille_bloc) + biais_y
                X = (x * taille_bloc) + biais_x

                for i in range(4):
                    if Y <= position_Y + value_X[i] <=  Y + taille_bloc  and X <= position_X + value_Y[i] <=  X + taille_bloc:
                        if around(map, position_X, position_Y, X, Y):
                            return False
    return True
