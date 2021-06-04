#mmmmmmm   mmm  mmmmm           mmm  m      mmmmm  mmmmmm mm   mmmmmmmm
#   #    m"   " #   "#        m"   " #        #    #      #"m  #   #   
#   #    #      #mmm#"        #      #        #    #mmmmm # #m #   #   
#   #    #      #             #      #        #    #      #  # #   #   
#   #     "mmm" #              "mmm" #mmmmm mm#mm  #mmmmm #   ##   #   
                                                                      
                         
                              
import socket, sys
from os import system, name
import random
import socket, sys
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


#Fonction qui vérifie si le joueur a rentré une couleur autre que celles permises 
#Renvoie False si le joueur rentre une combinaison de couleurs non présentes dans la liste couleurs ( 0 sert à quitter la partie )
#Renvoie True sinon 
def autre_couleur(choix): 
    couleurs = ['R','G','Y','B','C','W','M','0']
    for i in choix:
        if not(i in couleurs):
            return False 
    return True 

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
    print(BLUE+"===================DIFFICULTÉS==================\n"+RESET+"|                                              |\n|                                              |\n|                                              |\n|        1)FACILE                              |\n|        2)MOYEN                               | \n|        3)DIFFICILE                           | \n|        0)QUITTER                             |\n|                                              |\n|                                              |\n|                                              |\n"+BLUE+"================================================"+RESET)
    choix_possible = ['1','2','3','0']
    choix = input ("Ton choix: ")
    while( not(choix in choix_possible) ):
        choix = input ("Ton choix: ")
    return choix 


#Connexion du client au serveur 
HOST = '127.0.0.1'
PORT = 8877
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print ("La connexion a échoué.")
    sys.exit()    
print ("Connexion établie avec le serveur.")

#Le jeu 
def mastermind_solo_client(n): 
    score=100
    gagner = 0 
    recommencer = 1 
    tentative = 10 
    while((recommencer)):
        pseudo = input("Pour commencer, saisis ton pseudo : \n")
        mySocket.send(pseudo.encode())
        combi_secrete=mySocket.recv(1024)
        gagner_liste=mySocket.recv(1024)
        system('clear')
        while(not(gagner) and tentative):
            print (pseudo, "Il te reste "+ str(tentative)+ " tentative(s)")
            choix=input ("Choisis une combinaison de "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ") 
            if(choix=='0'):
                mySocket.send('FIN'.encode())
                time.sleep(1)
                mySocket.close()
                exit(0)

            while(len(choix)!=n or not(autre_couleur(choix))):
                choix=input ("Choisis une combinaison de "+str(n)+" couleurs parmi ['R','G','Y','B','C','W','M']\n(0) Pour quitter:  ") 
                if(choix=='0'):
                    mySocket.send('FIN'.encode())
                    time.sleep(1)
                    mySocket.close()
                    exit(0)
            mySocket.send(choix.encode())
            afficher_couleurs(choix)
            print("Si on compare ta combinaison avec celle à trouver on trouve:")
            compare= mySocket.recv(1024)
            afficher_couleurs_compare(compare.decode('utf8'))
            if( compare.decode('utf8') == gagner_liste.decode('utf8') ): 
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
            mySocket.send(choix.encode())
            if choix == '0': 
                recommencer = 0 
                mySocket.close()
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
            mySocket.send(choix.encode())
            if choix == '0': 
                recommencer = 0
                mySocket.close()
            elif choix == '1':
                gagner = 0
                tentative = 10


#règles du jeux : 
def regles():
    system('clear')
    system("cowsay -f turtle \" Te voilà enfin arrivé, fils de Hyoga.\nJe m'appelle Tort et je suis le plus vieil animal sur la planète.\n Suis-moi, je vais te raconter ce qui s’est passé il y a de cela des milliers d’années.\n\"")
    time.sleep(2)
    time.sleep(2)
    system("cowsay -f turtle \" Il y a longtemps, la planète Terre était la meilleure de toute la galaxie.\n Elle était bien peuplée et bien plus belle.\n Hélas, les humains ne la respectaient pas, ce qui a provoqué la colère des éléments de la nature.    \"")
    time.sleep(2)
    system("cowsay -f turtle \" Ainsi, quelques jours après le départ de ton père, avec son équipe d’astronautes dans l’espace, une force surnaturelle a provoqué la pétrification de toute la planète.\n À leur retour, malgré que la science eût été très avancée, ils n’ont pas pu fabriquer de remède à cause du manque des substances.\n Ils ont alors décidé de repeupler la planète.  \"")
    time.sleep(2)
    system("cowsay -f turtle \" Cependant, ton père qui croyait profondément en toi et en ton intelligence,  était sûr qu’un jour tu seras dépétrifié et tu pourras récupérer la science qu’il t’a laissée.\n La science qui permettra de fabriquer un remède pour la pétrification.\"")
    time.sleep(2)
    system("cowsay -f turtle \" Cette science est un guide qui se trouve dans ce vaisseau, il disait que tu es le seul à pouvoir l’ouvrir et à pouvoir t’en servir correctement pour sauver l’humanité.\nIl répétait que si ça tombait entre de mauvaises mains, la planète serait détruite.\"")
    time.sleep(2)
    system("cowsay -f turtle \" Fox va t'indiquer ce qu'il faut faire pour ouvrir le vaisseau.\"")
    time.sleep(2)
    system("cowsay -f fox \"Bonjour petit ! \n Votre père a codé un jeu qu'il a appelé Mastermind.\n Tu dois trouver la combinaison gagnante pour pouvoir ouvrir le vaisseau\n\"")
    time.sleep(2)
    system("cowsay -f fox \" Si tu choisis le mode \"solo\", le jeu va générer automatiquement une combinaison de couleurs, que tu devras deviner\n \"")
    time.sleep(2)
    system("coxsay -f fox \" Si tu choisis le mode \"duo\", un de tes amis choisira une combinaison\n que tu devras trouver.\n Attention, si vous essayez de tricher, le vaisseau explosera.\"")
    time.sleep(2)
    system("cowsay -f fox \" La combinaison sera composée de 4, 6 ou 8 couleurs parmi 6, selon le niveau de difficulté que tu choisiras.\n Les couleurs disponibles sont : Red(R), Yellow(Y), Blue(B), Cyan(C), White(W), Magenta(M), Green(G).\n Vous avez 10 tentatives pour trouver la bonne combinaison.\"")
    time.sleep(2)
    system("cowsay -f fox \" Bonne chance ! L'avenir de l'humanité est entre tes mains !\"")
  
#Fonction principale
def main():
    system('clear')
    #Le programme en entier             
    choix = menu()
    system('clear')
    while(not(choix in ['1','2','0'])):
        choix = menu()
        system('clear')
    while choix == '2':
        regles()
        choix = menu()
    if(choix=='1'):
        choix=menu_jouer_2()
        while(not(choix in ['1','2','3','0'])):
            choix = menu()
            system('clear')
        time.sleep(1)
        mySocket.send(choix.encode())
        if(choix=='1'):
            mastermind_solo_client(4)
        elif(choix=='2'): 
            mastermind_solo_client(6)
        elif(choix=='3'):
            mastermind_solo_client(8)
    elif( choix=='0'):
        mySocket.close()
        exit(0)
 
#Appel de la fonction principale
main()



