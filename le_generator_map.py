

from random import randint


def give_map():


    map = []

    for x in range(13):
        liste = []

        for y in range(20):
            n = randint(1, 5)
            if n == 2:
                liste.append('x')
            else:
                liste.append(' ')

            if x == 0:
                try :
                    liste[2] = "p"
                except:pass

        map.append("".join(liste))



    return map

"""t = give_map()
for p in t:
    print(p)"""


def level_1():
    map = [
    "                            h                  hxxxxxxxh                                                                x                                     ",
    "         x                  b                  m       m                                                     xxxxx      x                   xxxxxxxxxx        ",
    "   p                                       h   m   h   m                                              x                 x         x                           ",
    "            x               h         x    m   mx  m   m                                                                x                                     ",
    "xxxxxxx      x        x     m              m   m   m  xm                      x                                         x                                     ",
    "              x             m      x       m   b  xm   m                                       xxxxx                    x      x                              ",
    "               xxxx       xxbxxx           m       mx  b              x              x                                                                        ",
    "                                           m       m          x                                                         x                                     ",
    "                                           bxxxxxxxb   xxxx                                                                                                   "

    ]
    return map


def level_2():
    map = [
    "                      h     hxxxxxxxxhxxxxxxx                                         ",
    "         h            m     m        m                                                ",
    "         m    h       b     m hxxxxx m                                                ",
    "  p      b    m             b m      m                                                ",
    "xxxxxxx       b       h       m xxxxxb                                                ",
    "                      m     h m                                                       ",
    "              x       m     m m xxxxxx                                                ",
    "                      m     m m                                                       ",
    "                      b     bxbxxxxxxxxxxxxxxxxxxxx                                   "

    ]

    return map




def level_3():
    map = [
    "   xxxxxxx                                                                            ",
    "                      h  hxxh   h   h  x   x                                   ",
    "                      m  m  m   mx  m   x x                                    ",
    "                    x m  m  m   m x m    x                                     ",
    "     p               xb  bxxb   b  xb   x                                      ",
    "   xxxxxxx      xhx                                                                  ",
    "                 b                                                                    ",
    "              x                                                                       ",
    "               x                                                                      ",
    "                x                                                                     ",
    "                 x                                                                    ",
    "                  x                                                                   ",
    "                   xxxxxxx                                                            ",
    "                                                                                      ",
    "                                                                                      ",
    "                                                                                      ",
    "                                                                                      ",
    "                                                                                      ",


    ]

    return map


def ajuste_map(map):
    for i in range(len(map)):
        for y in range(len(map[i])):

            if map[i][y] != " ":
                if map[i - 1][y] == ' ' and map[i + 1][y] == ' ':
                    map[i][y] = "x"



def write_map(map):
    fic = open("map.txt", "w")
    for ligne in map:
        fic.write("'" + ligne + "'," + '\n')
    fic.close()



def level_4():
    map = [
    '                                                                                  xxxh',
'                                                     x                               m',
'    p                                               x       x                     m  m',
'  xxxxxxx                                          x       x x                    m  m',
'                         xxx                    xxx       x   x                   m xm',
'          xxxxxxx                 xxx                                             m  m',
'                       h     h                                   xxxxh            m  m',
'                       m  x  m              x                        m            mx m',
'                       b     b                           x      h    m            m  m',
'          hx     xh                                             m    m            m  m',
'          m       m      xxx            xxxxxx    xxxx          m    b            m xm',
'        xxb   x   bxxxxh                      x        x        m                 m  m',
'h                      m                 x xx  xx       h       bxxxx             m  m',
'm  xx                  m    hhhhx   xx           x      m                         mx m',
'm       hxxx  h  hxxx  m    mmmb      x  xx x     xxxx  m     h                   m  m',
'mh      m     m  m     m    mmb        x                b     m                   m  m',
'mm      m     m  m     m    mm  h       xxxxxxx        x      b                   m xm',
'mmh   xxb   xxb  b   xxb    mb  b               xxxxxxx                           m  m',
'mmm                         m         h                                           m  m',
'mmmhh                       m h       b            xxx     x                      mx m',
'mmmmmhhhhhhhhhhhhhhh hhhhhh m m  xxxx          x                                  m  m',
'bbbbbbbbbbbbbbbbbbbb bmbbmb b m                                                   m  m',
'                      m  b    m                                                   m xm',
'                   h  b       m                                                   m  m',
'              xxx  m     h    m                                                      m',
'    xxxxxx         bxxxxxbxxxxb                                                 xxxxxb',





    ]

    return map
