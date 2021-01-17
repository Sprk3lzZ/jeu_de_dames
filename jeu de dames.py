GameStatut = True  # Statu de jeu à True


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
    damier[0][0] = 1   #Pour ne pas pouvoir se déplacer sur cette case.

    #Creation coordonnées.
    for loop in range(1,11):
        damier[0][loop] = loop
        damier[loop][0] = loop

    colonne = 1
    ligne = 1

    #Placer les pions en fonction du joueurs mis en paramètre.
    for loop3 in range(1, 3):
        for loop in range(1 + (6 * (loop3 - 1)), 4 + (6 * (loop3 - 1)), 2):
            for loop1 in range(1, 11, 2):
                damier[loop][loop1] = 0
                damier[loop][loop1 + 1] = loop3
            for loop2 in range(1, 11, 2):
                damier[loop + 1][loop2] = loop3
                damier[loop + 1][loop2 + 1] = 0


    for plat in range(11):
        print(damier[plat])

    return damier



def game_statut(damier):
    """
    Fonction qui test si je jeu est en cours ou pas.
    :return: bool
    """
    Player1alive = False
    Player2alive = False

    #Cela teste quel joueur a gagné.
    for loop2 in range(1, 3):
        for loop in range(1, 11):
            for loop1 in range(1, 11):
                if damier[loop][loop1] == loop2:
                    if(loop2 == 1):
                        Player1alive = True
                    elif(loop2 == 2):
                        Player2alive = True
                elif loop == 10 and loop1 == 10:
                    if loop2 == 1 and Player1alive == False:
                        Player1alive = False
                        print("Le joueur 2 a gagné !!")
                    elif loop2 == 2 and Player2alive == False:
                        Player2alive = False
                        print("Le joueur 1 a gagné !!")


    #Teste si le jeu est toujours en cours.
    if Player2alive and Player1alive:
        GameStatut = True
    elif not Player1alive or not Player2alive:
        GameStatut = False

    return  GameStatut

def print_plat(damier):
    """
    Fonction qui renvoie le plateau et qui évite le retour des pions à leur place.
    :param damier:list
    :return: list
    """

    #Actualise le damier.
    for i in range(len(damier)):
        print(damier[i])

def deplacement(damier):
    """
    Fonction de déplacement.
    :param damier: list
    :return: list
    """

    pions(damier)
    isFinish = not game_statut(damier)

    while isFinish != True:


        play = False
        move = False




        while not play or not move:
            for i in range(1, 3):
                print("Joueur ",i, 'à vous de jouer !')
                play = False
                move = False
                xJ_d = int(input("Rentrez l'abscisse de la position de votre pion : "))
                yJ_d = int(input("Rentrez l'ordonnée de la position de votre pion : "))
                if xJ_d > 0 and xJ_d <= 10 and yJ_d > 0 and yJ_d <= 10:
                    if damier[yJ_d][xJ_d] == i and (xJ_d != 0 and yJ_d != 0):
                        if damier[yJ_d + (1-((i-1)*2))][xJ_d -1] == 0:
                            print(" ")
                            print("Déplacement possible en : P[", xJ_d -1, ';', yJ_d + (1-((i-1)*2)), ']')       #Proposition de déplacment.
                            play = True
                        if damier[yJ_d + (1-((i-1)*2))][xJ_d + 1] == 0:
                            print("Déplacement possible en : P[", xJ_d + 1, ';', yJ_d + (1-((i-1)*2)), ']')      #Proposition de déplacment.
                            play = True
                        if damier[yJ_d - 1][xJ_d - 1] == i + (1-((i-1)*2)) and damier[yJ_d - 2][xJ_d - 2] == 0:
                            print(" ")
                            print("Peut manger en : P[", xJ_d - 2, ';', yJ_d - 2, ']')                           #Proposition d'attaque.
                            play = True
                        if damier[yJ_d - 1][xJ_d + 1] == i + (1-((i-1)*2)) and damier[yJ_d - 2][xJ_d + 2] == 0:
                            print("Peut manger en : P[", xJ_d + 2, ';', yJ_d - 2, ']')                           #Proposition d'attaque.
                            print(" ")
                            play = True
                        if damier[yJ_d + 1][xJ_d - 1] == i + (1-((i-1)*2)) and damier[yJ_d + 2][xJ_d - 2] == 0:
                            print(" ")
                            print("Peut manger en : P[", xJ_d - 2, ';', yJ_d + 2, ']')                           #Proposition d'attaque.
                            play = True
                        if damier[yJ_d + 1][xJ_d + 1] == i + (1-((i-1)*2)) and damier[yJ_d + 2][xJ_d + 2] == 0:
                            print("Peut manger en : P[", xJ_d + 2, ';', yJ_d + 2, ']')                           #Proposition d'attaque.
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
                        xJ_a = int(input("Rentrez l'abscisse de la case de déplacement : "))
                        yJ_a = int(input("Rentrez l'ordonnée de la case de déplacement : "))
                        if xJ_a > 0 and xJ_a <= 10 and yJ_a > 0 and yJ_a <= 10:
                            if damier[yJ_a][xJ_a] == 0 and (yJ_a == yJ_d + (1-((i-1)*2)) and xJ_a == xJ_d + 1) or (
                                    yJ_a == yJ_d + (1-((i-1)*2)) and xJ_a == xJ_d - 1):
                                damier[yJ_d][xJ_d] = 0
                                damier[yJ_a][xJ_a] = i
                                move = True
                            elif (damier[yJ_a + 1][xJ_a - 1] == i + (1-((i-1)*2)) or damier[yJ_a + 1][xJ_a + 1] == i + (1-((i-1)*2)) or
                                  damier[yJ_a - 1][xJ_a - 1] == i + (1-((i-1)*2)) or damier[yJ_a - 1][xJ_a + 1] == i + (1-((i-1)*2))) and \
                                    damier[yJ_a][xJ_a] == 0:
                                damier[yJ_d][xJ_d] = 0
                                if xJ_a == xJ_d + 2 and yJ_d > yJ_a:
                                    damier[yJ_d - 1][xJ_d + 1] = 0
                                if xJ_a == xJ_d - 2 and yJ_d > yJ_a:
                                    damier[yJ_d - 1][xJ_d - 1] = 0
                                if xJ_a == xJ_d + 2 and yJ_d < yJ_a:
                                    damier[yJ_d + 1][xJ_d + 1] = 0
                                if xJ_a == xJ_d - 2 and yJ_d < yJ_a:
                                    damier[yJ_d + 1][xJ_d - 1] = 0
                                damier[yJ_a][xJ_a] = i
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