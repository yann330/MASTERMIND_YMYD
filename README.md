## Auteurs
* **Yanis HOURI**
* **Dihia HADJALI**
* **Marie FU**
* **Youcef OULD KACI**

# Mastermind

#### Ce projet est un jeu Mastermind implémenté en 3 versions. 


### Pré-requis :

Pour pouvoir faire marcher correctement ce progamme, il est requis de :
- Installer python3 : ``sudo apt install python3`` .
- Installer cowsay pour faire marcher la première et la deuxième version : ``sudo apt install cowsay`` .
- Avoir un terminal de couleur foncée (noir par exemple) en exécutant les deuc premières versions, car on affichera des étoiles de couleurs.
- Installer la bibliothèque ``Pygame`` :  ``sudo apt-get install -y python3-pip`` .



### Compilation :

Pour compiler et exécuter le projet, on doit : 

- Pour la première version se mettre dans le dossier ``Mastermind_basique`` puis exécuter la commande ``python3 Mastermind.py``.
- Pour la deuxième version, on se met dans le répertoire ``Mastermind_client_serveur``  soit on ouvre deux terminaux, soit on tilise un multiplexeur de terminaux comme ``tmux ``. Pour cela, on exécute la commande  ``tmux `` sur le terminal puis on duplique ce dernier avec les touches  ``ctrl+% ``. On se déplace entre les fenêtres avec les touches  ``ctrl+b `` puis  la flèche correspondante à la fenêtre qu'on veut. On se met ensuite sur la première fenêtre et on exécute ``python3 Serveur.py`` puis sur la deuxième fenêtre et on exécute la commande ``python3 Client.py``.
- Pour la troisième version, on doit se mettre dans le répertoire ``Mastermind_graphique`` puis exécuter la commande ``python3 game.py``.


### Les règles du jeu : 
 Les règles du jeu sont expliquées dans la première et la deuxième versions sous forme d’une petite histoire. Dans la troisième, elles sont expliquées brièvement mais pour l’instant on les a pas encore mises. 

La machine (ou le joueur dans le mode duo) devra générer  une combinaison de n parmi 7 dans la première et la deuxième version selon le niveau de difficulté choisi. Quant à la troisième version, le joueur doit générer une combinaison de 4 couleurs.
Le joueur devra par la suite essayer  de deviner la combinaison. A chaque tentative, le programme ou l’autre joueur lui donnera des indications : 
    • La couleur blanche signifie qu’une couleur est à la bonne position dans la combinaison. 
    • La couleur rouge signifie qu’une couleur est bien présente dans la combinaison mais n’est pas à la bonne place. 
    • La couleur noire signifie qu’une couleur n’est pas dans la combinaison. 
Le joueur aura un maximum de 10 tentatives pour deviner la combinaison. 


 


