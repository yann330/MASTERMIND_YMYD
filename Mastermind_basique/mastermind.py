#   mmmmm    mm    mmmm  mmmmm    mmm         m    m mmmmmm mmmmm   mmmm  mmmmm  mmmm  mm   m 
#   #    #   ##   #"   "   #    m"   "        "m  m" #      #   "# #"   "   #   m"  "m #"m  #   
#   #mmmm"  #  #  "#mmm    #    #              #  #  #mmmmm #mmmm" "#mmm    #   #    # # #m # 
#   #    #  #mm#      "#   #    #              "mm"  #      #   "m     "#   #   #    # #  # #   
#   #mmmm" #    # "mmm#" mm#mm   "mmm"          ##   #mmmmm #    " "mmm#" mm#mm  #mm#  #   ## 
                                                                             
                                                                     
from os import system, name
import random
import time


#Pour afficher en couleurs 
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'

#Fontion qui prend en paramètre un entier et renvoie une liste de n couleurs aléatoires 
#Le joueur aura 10 essais pour trouver cette combinaison 
def generer_combi(n): 
    colors = ['R','G','Y','B','C','W','M']
    choix=[]
    for i in range(n): 
        choix.append(random.choice(colors))
    return choix


#Fonction qui demande au joueur A de donner des indications au joueur B par rapport à la combinaison qu'il a saisi
def combi_joueur_A(n, pseudo_A):
    system("clear")
    print(pseudo_A,':\n')
    choix = input("Choisis la combinaison que tu feras deviner à ton advesaire. Elle doit comprendre "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n ")
    while(len(choix)!=n or not(autre_couleur(choix))): 
        print(pseudo_A,':\n')
        choix = input ("Choisis la combinaison que tu feras deviner à ton advesaire. Elle doit comprendre "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n ")
    return choix



#Fonction qui vérifie si le joueur a rentré une couleur autre que celles permises 
#Renvoie False si le joueur rentre une combinaison de couleurs non présentes dans la liste couleurs ( 0 sert à quitter la partie )
#Renvoie True sinon 
def autre_couleur(choix): 
    couleurs = ['R','G','Y','B','C','W','M','0']
    for i in choix:
        if not(i in couleurs):
            return False 
    return True 


#Fonction qui demande au joueur de saisir une combinaison de (n) couleurs 
#Le choix n'est pas pris en compte si l'utilisateur rentre une combinaison de plus de n caractères 
#Elle renvoie la saisie du joueur à la fin 
def combi_joueur(n): 
    choix=input ("Choisis une combinaison de " +str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ") 
    if(choix=='0'):
        exit(0)
    while(len(choix)!=n or not(autre_couleur(choix))): 
        choix = input ("Choisis une combinaison de "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ")
        if(choix=='0'):
            exit(0)
    return choix     



#Fonction qui demande au joueur de saisir une combinaison de (n) couleurs 
#Le choix n'est pas pris en compte si l'utilisateur rentre une combinaison de plus de n caractères 
#Elle renvoie la saisie du joueur à la fin 
def combi_joueur_duo(n): 
    choix=input ("Choisis une combinaison de "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ") 
    if(choix=='0'):
        exit(0)
    while(len(choix)!=n or not(autre_couleur(choix))): 
        choix = input ("Choisis une combinaison de "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ")
        if(choix=='0'):
            exit(0)
    return choix  


#Fonction qui vérifie si le joueur 1 (celui qui fait deviner la combinaison de couleurs) ne triche pas 
#Renvoie True s'il triche 
#Renvoie False sinon 
def anti_triche_joueur(combi1, combi2):
    if (combi1 != combi2): 
        return True 
    else: 
        return False  

#Fonction qui affiche la combinaison saisie en couleurs sur terminal 
def afficher_couleurs(combi): 
    for n in combi:
        if n == 'R':
            print(RED+'*'+RESET+'   ', end='') 
        elif n == 'Y':
            print(YELLOW+'*'+RESET+'   ', end='') 
        elif n == 'B':
            print(BLUE+'*'+RESET+'   ', end='') 
        elif n == 'W':
            print(WHITE+'*'+RESET+'   ', end='') 
        elif n == 'M':
            print(MAGENTA+'*'+RESET+'   ', end='')
        elif n == 'C':
            print(CYAN+'*'+RESET+'   ', end='')
        elif n == 'G':
            print(GREEN+'*'+RESET+'   ', end='')
    print('')


#Fonction qui affiche en couleurs les indications du joueur 1 (celui qui fait deviner la combinaison de couleurs) au joueur 2
def afficher_couleurs_compare(combi): 
    for n in combi:
        if n == 'R':
            print(RED+'*'+RESET+'   ', end='') 
        elif n == 'B':
            print(BLACK+'*'+RESET+'   ', end='') 
        elif n == 'W':
            print(WHITE+'*'+RESET+'   ', end='') 
    print('')


#Fonction qui compare deux combinaisons passées en argument 
#Affiche: Étoile blanche -> La couleur est au bon endroit 
#         Étoile Rouge   -> La couleur est présente dans la combinaison mais n'est pas au bon endroit 
#         Étoile Noire   -> La couleur n'est pas présente dans la combinaison qu'on veut trouver 
#Elle renvoie une liste des couleurs qui sont affichées, qui nous servivra à déterminer si oui ou non le joueur a gagné 
#De plus, la liste tmp nous servira à déterminer si les joueurs ne trichent pas 
def compare_combi(combi1, combi2):
    tmp = [] 
    for i in range(len(combi1)):
        if combi1[i] == combi2[i]: 
            print(WHITE+'*'+RESET+'   ', end='')
            tmp.append('W')
        elif (combi1[i] in combi2): 
            print(RED+'*'+RESET+'   ', end='') 
            tmp.append('R')
        else: 
            print(BLACK+'*'+RESET+'   ', end='') 
            tmp.append('B')
    return tmp 


#Fonction qui fait la même chose que la fonction ci-dessus mais sans l'affichage 
def compare_combi_2(combi1, combi2):
    tmp = [] 
    for i in range(len(combi1)):
        if combi1[i] == combi2[i]: 
            tmp.append('W')
        elif (combi1[i] in combi2): 
            tmp.append('R')
        else:  
            tmp.append('B')
    return tmp 


#Fonction qui demande au joueur 1 de donner des indications au joueur 2 par rapport à la combinaison qu'il a saisi
def compare_combi_joueur(n, pseudo_A):
    tmp=[]
    print(pseudo_A, ':\n')
    choix=input ("Compare ta combinaison avec celle de ton adversaire : \n(0)Pour quitter:\n  ")
    if(choix=='0'):
        exit(0)
    while(len(choix)!=n):
        print(pseudo_A, ':\n')
        choix=input ("Compare ta combinaison avec celle de ton adversaire : \n(0)Pour quitter:\n  ")
    for i in choix:
        tmp.append(i)
    return tmp  

#Premier menu
def menu(): 
    print(BLUE+"===================MASTERMIND===================\n"+RESET+"|                                              |\n|                                              |\n|                                              |\n|        1)Jouer                               |\n|        2)Règles du jeu                       | \n|        0)QUITTER                             |\n|                                              |\n|                                              |\n|                                              |\n"+BLUE+"================================================"+RESET) 
    choix_possible = ['1','2','0']
    choix = input ("Ton choix: ")
    while( not(choix in choix_possible) ):
        choix = input ("Ton choix: ")
    return choix 

#Deuxième menu
def menu_jouer():
    print(BLUE+"===================JOUER========================\n"+RESET+"|                                              |\n|                                              |\n|                                              |\n|        1)SOLO                                |\n|        2)DUO                                 | \n|        0)QUITTER                             |\n|                                              |\n|                                              |\n|                                              |\n"+BLUE+"================================================"+RESET)
    choix_possible = ['1','2','0']
    choix = input ("Ton choix: ")
    while( not(choix in choix_possible) ):
        choix = input ("Ton choix: ")
    return choix 

#Troisième menu
def menu_jouer_2():
    print(BLUE+"===================DIFFICULTÉS========================\n"+RESET+"|                                              |\n|                                              |\n|                                              |\n|        1)FACILE                              |\n|        2)MOYEN                               | \n|        2)DIFFICILE                           | \n|        0)QUITTER                             |\n|                                              |\n|                                              |\n|                                              |\n"+BLUE+"================================================"+RESET)
    choix_possible = ['1','2','3','0']
    choix = input ("Ton choix: ")
    while( not(choix in choix_possible) ):
        choix = input ("Ton choix: ")
    return choix 

#règles du jeux : 
def regles():
    system('clear') 
    system("cowsay -f turtle \" Te voilà enfin arrivé, fils de Hyoga.\nJe m'appelle Tort et je suis le plus vieil animal sur la planète.\n Suis-moi, je vais te raconter ce qui s’est passé il y a de cela des milliers d’années.\n\"")
    time.sleep(4)
    time.sleep(4)
    system("cowsay -f turtle \" Il y a longtemps, la planète Terre était la meilleure de toute la galaxie.\n Elle était bien peuplée et bien plus belle.\n Hélas, les humains ne la respectaient pas, ce qui a provoqué la colère des éléments de la nature.    \"")
    time.sleep(4)
    system("cowsay -f turtle \" Ainsi, quelques jours après le départ de ton père, avec son équipe d’astronautes dans l’espace, une force surnaturelle a provoqué la pétrification de toute la planète.\n À leur retour, malgré que la science eût été très avancée, ils n’ont pas pu fabriquer de remède à cause du manque des substances.\n Ils ont alors décidé de repeupler la planète.  \"")
    time.sleep(4)
    system("cowsay -f turtle \" Cependant, ton père qui croyait profondément en toi et en ton intelligence,  était sûr qu’un jour tu seras dépétrifié et tu pourras récupérer la science qu’il t’a laissée.\n La science qui permettra de fabriquer un remède pour la pétrification.\"")
    time.sleep(4)
    system("cowsay -f turtle \" Cette science est un guide qui se trouve dans ce vaisseau, il disait que tu es le seul à pouvoir l’ouvrir et à pouvoir t’en servir correctement pour sauver l’humanité.\nIl répétait que si ça tombait entre de mauvaises mains, la planète serait détruite.\"")
    time.sleep(4)
    system("cowsay -f turtle \" Fox va t'indiquer ce qu'il faut faire pour ouvrir le vaisseau.\"")
    time.sleep(4)
    system("cowsay -f fox \"Bonjour petit ! \n Votre père a codé un jeu qu'il a appelé Mastermind.\n Tu dois trouver la combinaison gagnante pour pouvoir ouvrir le vaisseau\n\"")
    time.sleep(4)
    system("cowsay -f fox \" Si tu choisis le mode \"solo\", le jeu va générer automatiquement une combinaison de couleurs, que tu devras deviner\n \"")
    time.sleep(4)
    system("cowsay -f fox \" Si tu choisis le mode \"duo\", un de tes amis choisira une combinaison\n que tu devras trouver.\n Attention, si vous essayez de tricher, le vaisseau explosera.\"")
    time.sleep(4)
    system("cowsay -f fox \" La combinaison sera composée de 4, 6 ou 8 couleurs parmi 6, selon le niveau de difficulté que tu choisiras.\n Les couleurs disponibles sont : Red(R), Yellow(Y), Blue(B), Cyan(C), White(W), Magenta(M), Green(G).\n Vous avez 10 tentatives pour trouver la bonne combinaison.\"")
    time.sleep(4)
    system("cowsay -f fox \" Bonne chance ! L'avenir de l'humanité est entre tes mains !\"")
  

#Fonction qui initialise une liste avec (n) occurrences de 'W' 
def initialiser_gagner(n):
    tmp=[] 
    for i in range(n):
        tmp.append('W')
    return tmp  


#Version SOLO du mastermind 
#Le joueur affrontera la machine 
def mastermind_solo(n): 
    score=100
    gagner = 0 
    recommencer = 1 
    tentative = 10 
    while((recommencer)):
        pseudo = input ("Pour commencer, saisis ton pseudo : \n")
        combi_secrete = generer_combi(n)
        gagner_liste = initialiser_gagner(n)
        system('clear')
        while(not(gagner) and tentative): 
            print(pseudo, ", Il te reste ", tentative, "tentative(s)" )
            choix=combi_joueur(n)
            afficher_couleurs(choix)
            print("Si on compare ta combinaison avec la bonne combinaison, on trouve :\n")
            compare = compare_combi(choix, combi_secrete)
            if( compare == gagner_liste ): 
                gagner = 1 
            elif(not(gagner)):
                score = score - 10
                tentative = tentative - 1
            print ("")
            print ("")
        if(not(gagner)): 
            system("cowsay -f fox \"Le nombre de tentatives est nul, Tu as perdu...\"")
            system("cowsay -f fox \"Veux-tu recommencer?\n1) Oui   0) Non : \"")
            choix=input ("")
            while(not (choix in ['1','0'])):
                system("cowsay -f fox \"Veux-tu recommencer?\n1) Oui   0) Non : \"")
                choix=input ("")
            if choix == '0': 
                recommencer = 0 
                exit(0)
            else:
                tentative = 10 
        else: 
            print("Score: " + str(score)) 
            system("cowsay -f turtle \"Tu as gagné!\n\"")
            system("cowsay -f turtle \"Veux-tu recommencer?\n1) Oui   0) Non : \"")
            choix=input ("")
            if choix == '0': 
                recommencer = 0
                exit(0)
            elif choix == '1':
                gagner = 0
                tentative = 10


#Version DUO du mastermind 
#Le joueur affrontera un autre joueur  
def mastermind_duo(n): 
    score=100
    gagner = 0 
    recommencer = 1 
    tentative = 10 
    while((recommencer)):
        print("Pour commencer, veuillez saisir vos pseudo:\nLe joueur A choisira une combinaison et la fera deviner au joueur B\n")
        pseudo_A = input("Joueur A : \n")
        pseudo_B = input("Joueur B : \n")
        combi_secrete = combi_joueur_A(n, pseudo_A)
        system('clear')
        gagner_liste = initialiser_gagner(n)
        while(not(gagner) and tentative): 
            print(pseudo_B,':\nIl te reste ', tentative, 'tentative(s)' )
            choix=combi_joueur_duo(n)
            afficher_couleurs(choix)
            compare = compare_combi_joueur(n, pseudo_A)
            tmp = compare_combi_2(combi_secrete,choix) 

            while(anti_triche_joueur(compare, tmp)):
                print(pseudo_A, ':\nArrête de tricher et sois honnête...\n')
                compare = compare_combi_joueur(n, pseudo_A)
            afficher_couleurs_compare(compare)
            if( compare == gagner_liste ): 
                gagner = 1 
            elif(not(gagner)):
                score = score - 10
                tentative = tentative - 1
            print ("")
            print ("")
        if(not(gagner)): 
            system("cowsay -f fox \"Le nombre de tentatives est nul, Tu as perdu...\"")
            system("cowsay -f fox \"Veux-tu recommencer?\n1) Oui   0) Non : \"")
            choix=input ("")
            while(not (choix in ['1','0'])):
                system("cowsay -f fox \"Veux-tu recommencer?\n1) Oui   0) Non : \"")
                choix=input ("")
            if choix == '0': 
                recommencer = 0 
                exit(0)
            else:
                tentative = 10 
        else: 
            print("Score: "+ str(score))
            system("cowsay -f turtle \"Tu as gagné!\n\"")
            system("cowsay -f turtle \"Veux-tu recommencer?\n1) Oui   0) Non : \"")
            choix=input ("")
            while(not (choix in ['1','0'])):
                system("cowsay -f turtle \"Veux-tu recommencer?\n1) Oui   0) Non : \"")
                choix=input ("")
            if choix == '0': 
                recommencer = 0
                exit(0)
            else:
                gagner=0
                tentative = 10

#Fonction principale 
def main():
    system('clear')
    choix = menu()
    system('clear')
    while(not(choix in ['1','2','0'])):
        choix = menu()
        system('clear')
    while(choix=='2'):
        regles()
        choix = menu()
    if(choix=='1'):
        choix=menu_jouer()
        if(choix=='1'): 
            choix=menu_jouer_2()
            while(not(choix in ['1','2','3','0'])):
                choix = menu()
                system('clear')
            if(choix=='1'):
                mastermind_solo(4)
            elif(choix=='2'): 
                mastermind_solo(6)
            elif(choix=='3'):
                mastermind_solo(8)
        elif(choix=='2'):
            choix=menu_jouer_2()
            if(choix=='1'):
                mastermind_duo(4)
            elif(choix=='2'): 
                mastermind_duo(6)
            elif(choix=='3'):
                mastermind_duo(8)
        elif(choix == '0'):
            exit(0)

#Appel de la fonction principale
main()
