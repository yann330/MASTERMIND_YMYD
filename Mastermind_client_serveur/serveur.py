#mmmmmmm   mmm  mmmmm          mmmm  mmmmmm mmmmm  m    m mmmmmm mmmmm 
#   #    m"   " #   "#        #"   " #      #   "# "m  m" #      #   "#
#   #    #      #mmm#"        "#mmm  #mmmmm #mmmm"  #  #  #mmmmm #mmmm"
#   #    #      #                 "# #      #   "m  "mm"  #      #   "m
#   #     "mmm" #             "mmm#" #mmmmm #    "   ##   #mmmmm #     m
                                                                      
                               

from os import system, name
import random
import socket, sys
import time 
import multiprocessing

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

#Client serveur 
HOST = '127.0.0.1'
PORT = 8877

#Création de la socket serveur 
system('clear')
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print ("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()
print ("Serveur prêt, en attente de requêtes ...")


#Fontion qui prend en paramètre un entier et renvoie une liste de n couleurs aléatoires 
#Le joueur aura 10 essais pour trouver cette combinaison 
def generer_combi(n): 
    colors = ['R','G','Y','B','C','W','M']
    choix=[]
    for i in range(n): 
        choix.append(random.choice(colors))
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
    choix=input ("Choisis une combinaison de "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ") 
    if(choix=='0'):
        exit(0)
    while(len(choix)!=n or not(autre_couleur(choix))): 
        choix = input ("Choisis une combinaison de "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ")
    return choix     

#Fonction qui demande au joueur A de choisir une combinaison qu'il va faire deviner à son adversaire 
def combi_joueur_A(n, pseudo_A):
    system("clear")
    print(pseudo_A,':\n')
    choix = input("Choisis la combinaison que tu feras deviner à ton advesaire. Elle doit comprendre "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n ")
    while(len(choix)!=n or not(autre_couleur(choix))): 
        print(pseudo_A,':\n')
        choix = input ("Choisis la combinaison que tu feras deviner à ton advesaire. Elle doit comprendre "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n ")
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
def compare_combi_joueur(n):
    tmp=[]
    choix=input ("Compare ton choix avec le choix du joueur B: \n(0)Pour quitter:  ")
    if(choix=='0'):
        exit(0)
    while(len(choix)!=n):
        choix=input ("Compare ton choix avec le choix du joueur B: \n(0)Pour quitter:  ")
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

#Fonction qui initialise une liste avec (n) occurrences de 'W' 
def initialiser_gagner(n):
    tmp=[] 
    for i in range(n):
        tmp.append('W')
    return tmp  

#Le jeu 
def mastermind_solo_serveur(connexion, n): 
    time.sleep(4)
    score=100
    gagner = 0 
    recommencer = 1 
    tentative = 10 
    while((recommencer)):
        pseudo = connexion.recv(1024)
        time.sleep(2)
        combi_secrete = generer_combi(n)
        connexion.send(str(combi_secrete).encode())
        gagner_liste = initialiser_gagner(n)
        time.sleep(2)
        connexion.send(str(gagner_liste).encode())
        while(not(gagner) and tentative):
            choix = connexion.recv(1024)
            if( choix.decode().upper() == 'FIN' ):
                exit(0)
            compare = compare_combi_2(choix.decode('utf8'), combi_secrete)
            connexion.send(str(compare).encode())
            if( compare == gagner_liste ): 
                gagner = 1 
            elif(not(gagner)):
                score = score - 10
                tentative = tentative - 1
        if(not(gagner)): 
            choix=connexion.recv(1024)
            if choix.decode() == '0': 
                recommencer = 0 
                connexion.close()
            else:
                tentative = 10 
        else: 
            choix=connexion.recv(1024)
            if choix.decode('utf8') == '0': 
                recommencer = 0
                exit(0)
            elif choix.decode('utf8') == '1':
                gagner = 0
                tentative = 10
#Fonction principale qui prend la connexion des clients
def main():
    #Nombre de clients limité à 1000
    mySocket.listen(1000)
    proc=[]
    # 4) Etablissement de la connexion :
    for i in range(1000):
        connexion, adresse = mySocket.accept()
        print ("Client connecté(e), adresse IP : %s, port : %s" % (adresse[0], adresse[1]))
        n=connexion.recv(1024)
        if(n.decode('utf8')=='1'):
            tmp = 4
            t= multiprocessing.Process(target=mastermind_solo_serveur, args=(connexion, tmp, ))
            proc.append(t)
            t.start()
        elif(n.decode('utf8')=='2'):
            tmp = 6
            t= multiprocessing.Process(target=mastermind_solo_serveur, args=(connexion, tmp, ))
            proc.append(t)
            t.start()
        elif(n.decode('utf8')=='3'):
            tmp = 8
            t= multiprocessing.Process(target=mastermind_solo_serveur, args=(connexion, tmp, ))
            proc.append(t)
            t.start()
        
        
    
#Appel de la fonction principale 
main()