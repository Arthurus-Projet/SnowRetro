





# "écrire les stats du joueurs : "
def ecrire(name_file, message):
    fic = open(name_file, "w")
    fic.write(message)
    fic.close()

def lire(name_file):
    fic = open(name_file, "r")
    read = fic.read()
    fic.close()

    read = read.split(' ')
    if len(read) > 1:
        return float(read[0]), float(read[1])
    return -1, -1

def lire_str(name_file):
    fic = open(name_file, "r")
    read = fic.read()
    fic.close()

    return bytes(read, "utf-8")
