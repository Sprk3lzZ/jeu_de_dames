GameStatu = True  # Statu de jeu à True


def plateau():
    """
    Fonction qui créer un plateau vierge.
    :return: list
    """

    # Création du damier vierge
    damier = [[0 for i in range(11)] for i in range(11)]

    return damier


def pions(damier):
    """
        Fonction qui place des pions joueur1 et joueur2 sur le damier.
        ;entrée: list
        :return: list
        """
    damier[0][0] = 1

    #Creation coordonnées.
    for loop in range(1,11):
        damier[0][loop] = loop
        damier[loop][0] = loop

    colonne = 1
    ligne = 1

    # Placement des pions joueur 1
    for loop in range(1, 4, 2):
        for loop1 in range(1, 11, 2):
            damier[loop][loop1] = 0
            damier[loop][loop1 + 1] = 1
        for loop2 in range(1, 11, 2):
            damier[loop + 1][loop2] = 1
            damier[loop + 1][loop2 + 1] = 0

    # Placement des pions joueur 2
    for loop in range(7, 11, 2):
        for loop1 in range(1, 11, 2):
            damier[loop][loop1] = 0
            damier[loop][loop1 + 1] = 2
        for loop2 in range(1, 10, 2):
            damier[loop + 1][loop2] = 2
            damier[loop + 1][loop2 + 1] = 0

    for plat in range(11):
        print(damier[plat])

    return damier



def game_statu(damier):
    """
    Fonction qui test si je jeu est en cours ou pas.
    :return: bool
    """
    Player1alive = False
    Player2alive = False
    #damier[0][0] = 1

    # Détéction fin de jeu
    for loop in range(1, 11):
        for loop1 in range(1, 11):
            if damier[loop][loop1] == 1:

                Player1alive = True
            elif loop == 10 and loop1 == 10 and Player1alive == False:
                print("Le joueur 2 a gagné !!")
                Player1alive = False

    for loop in range(1, 11):
        for loop1 in range(1, 11):
            if damier[loop][loop1] == 2:
                Player2alive = True
            elif loop == 10 and loop1 == 10 and Player2alive == False:
                print("Le joueur 1 a gagné !!")
                Player2alive = False
    if Player2alive and Player1alive:
        GameStatu = True
    elif not Player1alive or not Player2alive:
        GameStatu = False

    return  GameStatu

def print_plat(damier):
    """
    Fonction qui renvoie le plateau et qui évite le retour des pions à leur place.
    :param damier:list
    :return: list
    """

    for i in range(len(damier)):
        print(damier[i])

def deplacement(damier):
    """
    Fonction de déplacement.
    :param damier: list
    :return: list
    """

    pions(damier)
    isFinish = not game_statu(damier)

    while isFinish != True:

        print("Joueur 1 à vous de jouer")
        play = False
        move = False

        while not play or not move:
            play = False
            move = False
            xJ1_d = int(input("Rentrez l'abscisse de la position de votre pion : "))
            yJ1_d = int(input("Rentrez l'ordonnée de la position de votre pion : "))
            if xJ1_d > 0 and xJ1_d <= 10 and yJ1_d > 0 and yJ1_d <= 10:
                if damier[yJ1_d][xJ1_d] == 1 and (xJ1_d != 0 and yJ1_d != 0):
                    if damier[yJ1_d + 1][xJ1_d - 1] == 0:
                        print(" ")
                        print("Déplacement possible en : P[", xJ1_d - 1, ';', yJ1_d + 1, ']')
                        play = True
                    if damier[yJ1_d + 1][xJ1_d + 1] == 0:
                        print("Déplacement possible en : P[", xJ1_d + 1, ';', yJ1_d + 1, ']')
                        print(" ")
                        play = True
                    if damier[yJ1_d + 1][xJ1_d - 1] == 2 and damier[yJ1_d + 2][xJ1_d - 2] == 0:
                        print(" ")
                        print("Peut manger en : P[", xJ1_d - 2, ';', yJ1_d + 2, ']')
                        play = True
                    if damier[yJ1_d + 1][xJ1_d + 1] == 2 and damier[yJ1_d + 2][xJ1_d + 2] == 0:
                        print("Peut manger en : P[", xJ1_d + 2, ';', yJ1_d + 2, ']')
                        print(" ")
                        play = True
                    if damier[yJ1_d - 1][xJ1_d - 1] == 2 and damier[yJ1_d - 2][xJ1_d - 2] == 0:
                        print(" ")
                        print("Peut manger en : P[", xJ1_d - 2, ';', yJ1_d - 2, ']')
                        play = True
                    if damier[yJ1_d - 1][xJ1_d + 1] == 2 and damier[yJ1_d - 2][xJ1_d + 2] == 0:


                        print(" ")
                        play = True
                    elif not play:
                        print_plat(damier)
                        print(" ")
                        print("Veuillez reesayer : Le déplacement est impossible.")
                        print(" ")

                else:
                    print_plat(damier)
                    print(" ")
                    print("Veuillez reesayer : Il n'y a pas de pion ou ce n'est pas le votre.")
                    print(" ")
                if play:
                    xJ1_a = int(input("Rentrez l'abscisse de la case de déplacement : "))
                    yJ1_a = int(input("Rentrez l'ordonnée de la case de déplacement : "))
                    if xJ1_a > 0 and xJ1_a <= 10 and yJ1_a > 0 and yJ1_a <= 10:
                        if damier[yJ1_a][xJ1_a] == 0 and (yJ1_a == yJ1_d + 1 and xJ1_a == xJ1_d + 1) or (
                                yJ1_a == yJ1_d + 1 and xJ1_a == xJ1_d - 1):
                            damier[yJ1_d][xJ1_d] = 0
                            damier[yJ1_a][xJ1_a] = 1
                            move = True
                        elif (damier[yJ1_a - 1][xJ1_a - 1] == 2 or damier[yJ1_a - 1][xJ1_a + 1] == 2 or damier[yJ1_a + 1][xJ1_a - 1] == 2 or damier[yJ1_a + 1][xJ1_a + 1] == 2) and damier[yJ1_a][xJ1_a] == 0:
                            damier[yJ1_d][xJ1_d] = 0
                            if xJ1_a == xJ1_d + 2 and yJ1_d > yJ1_a:
                                damier[yJ1_d - 1][xJ1_d + 1] = 0
                            if xJ1_a == xJ1_d - 2 and yJ1_d > yJ1_a:
                                damier[yJ1_d - 1][xJ1_d - 1] = 0
                            if xJ1_a == xJ1_d + 2 and yJ1_d < yJ1_a:
                                damier[yJ1_d + 1][xJ1_d + 1] = 0
                            if xJ1_a == xJ1_d - 2 and yJ1_d < yJ1_a:
                                damier[yJ1_d + 1][xJ1_d - 1] = 0
                            damier[yJ1_a][xJ1_a] = 1
                            move = True
                        else:
                            print_plat(damier)
                            print(" ")
                            print("Veuillez reesayer : déplacement impossible.")
                            print(" ")
                    else:
                        print_plat(damier)
                        print("")
                        print("Veuillez reesayer : déplacement impossible.")
                        print(" ")
            else:
                print_plat(damier)
                print(" ")
                print("Veuillez reesayer : déplacement impossible.")
                print(" ")

        print_plat(damier)
        play = False
        move = False
        print("Joueur 2 à vous de jouer !")

        while not play or not move:
            play = False
            move = False
            xJ2_d = int(input("Rentrez l'abscisse de la position de votre pion : "))
            yJ2_d = int(input("Rentrez l'ordonnée de la position de votre pion : "))
            if xJ2_d > 0 and xJ2_d <= 10 and yJ2_d > 0 and yJ2_d <= 10:
                if damier[yJ2_d][xJ2_d] == 2 and (xJ2_d != 0 and yJ2_d != 0):
                    if damier[yJ2_d - 1][xJ2_d - 1] == 0:
                        print(" ")
                        print("Déplacement possible en : P[", xJ2_d - 1, ';', yJ2_d - 1, ']')
                        play = True
                    if damier[yJ2_d - 1][xJ2_d + 1] == 0:
                        print("Déplacement possible en : P[", xJ2_d + 1, ';', yJ2_d - 1, ']')
                        play = True
                    if damier[yJ2_d - 1][xJ2_d - 1] == 1 and damier[yJ2_d - 2][xJ2_d - 2] == 0:
                        print(" ")
                        print("Peut manger en : P[", xJ2_d - 2, ';', yJ2_d - 2, ']')
                        play = True
                    if damier[yJ2_d - 1][xJ2_d + 1] == 1 and damier[yJ2_d - 2][xJ2_d + 2] == 0:
                        print("Peut manger en : P[", xJ2_d + 2, ';', yJ2_d - 2, ']')
                        print(" ")
                        play = True
                    if damier[yJ2_d + 1][xJ2_d - 1] == 1 and damier[yJ2_d + 2][xJ2_d - 2] == 0:
                        print(" ")
                        print("Peut manger en : P[", xJ2_d - 2, ';', yJ2_d + 2, ']')
                        play = True
                    if damier[yJ2_d + 1][xJ2_d + 1] == 1 and damier[yJ2_d + 2][xJ2_d + 2] == 0:
                        print("Peut manger en : P[", xJ2_d + 2, ';', yJ2_d + 2, ']')
                        print(" ")
                        play = True
                    elif not play:
                        print_plat(damier)
                        print(" ")
                        print("Veuillez reesayer : déplacement impossible.")
                        print(" ")

                else:
                    print_plat(damier)
                    print(" ")
                    print("Veuillez reesayer : aucun pions.")
                    print(" ")
                if play:
                    xJ2_a = int(input("Rentrez l'abscisse de la case de déplacement : "))
                    yJ2_a = int(input("Rentrez l'ordonnée de la case de déplacement : "))
                    if xJ2_a > 0 and xJ2_a <= 10 and yJ2_a > 0 and yJ2_a <= 10:
                        if damier[yJ2_a][xJ2_a] == 0 and (yJ2_a == yJ2_d - 1 and xJ2_a == xJ2_d + 1) or (yJ2_a == yJ2_d - 1 and xJ2_a == xJ2_d - 1):
                            damier[yJ2_d][xJ2_d] = 0
                            damier[yJ2_a][xJ2_a] = 2
                            move = True
                        elif (damier[yJ2_a + 1][xJ2_a - 1] == 1 or damier[yJ2_a + 1][xJ2_a + 1] == 1 or damier[yJ2_a - 1][xJ2_a - 1] == 1 or damier[yJ2_a - 1][xJ2_a + 1] == 1) and damier[yJ2_a ][xJ2_a ] == 0:
                            damier[yJ2_d][xJ2_d] = 0
                            if xJ2_a == xJ2_d + 2 and yJ2_d > yJ2_a:
                                damier[yJ2_d - 1][xJ2_d + 1] = 0
                            if xJ2_a == xJ2_d - 2 and yJ2_d > yJ2_a:
                                damier[yJ2_d - 1][xJ2_d - 1] = 0
                            if xJ2_a == xJ2_d + 2 and yJ2_d < yJ2_a:
                                damier[yJ2_d + 1][xJ2_d + 1] = 0
                            if xJ2_a == xJ2_d - 2 and yJ2_d < yJ2_a:
                                damier[yJ2_d + 1][xJ2_d - 1] = 0
                            damier[yJ2_a][xJ2_a] = 2
                            move = True
                        else:
                            print_plat(damier)
                            print(" ")
                            print("Veuillez reesayer : déplacement impossible.")
                            print(" ")
                    else:
                        print_plat(damier)
                        print(" ")
                        print("Veuillez reesayer : déplacement impossible.")
                        print(" ")
            else:
                print_plat(damier)
                print(" ")
                print("Veuillez reesayer : déplacement impossible.")
                print(" ")

        print_plat(damier)

def game_manager(damier):
    """
    Fonction du fonctionnement du jeu de dames.
    :entrée: list
    :return: list
    """

    deplacement(damier)


game_manager(plateau())