# Rapport du Projet Commun L2 Informatique
				
#Le jeu du  Mastermind

#Rapport de Groupe

## Auteurs : 
* **Yanis HOURI**
* **Dihia HADJALI**
* **Maire Fu**
* **Youcef Ould Kaci**



## Présentation du projet :
Le projet est un jeu « Mastermind ». C’est un jeu de stratégie combinatoire abstrait qui nécessite réflexion et déduction. Ses règles sont assez simples, on les décrira plus bas dans le rapport. 


## Description brève du projet :
On a implémenté trois versions du jeu « Mastermind » : 
    • La première est un jeu simple où le joueur peut choisir de jouer en solo, c’est-à-dire contre l’ordinateur, on a pour ça implémenté une petite IA qui génère une combinaison aléatoire et qui compare la combinaison du joueur à la combinaison générée. Il peut aussi choisir le mode duo, où il jouera contre un autre joueur. Ce dernier générera une combinaison et donnera des indications à son adversaire. Le programme lui interdit de tricher. Ce jeu a aussi un menu où le joueur pourra choisir le niveau de difficulté qui lui convient. 
    • La deuxième   est une version client-serveur de la première mais sans le mode duo, c’est-à-dire, le joueur jouera contre la machine. 
    • La troisième est un jeu avec une vraie interface graphique où deux joueurs s’affronteront. Le premier génère une combinaison, le deuxième essaiera de la deviner grâce aux indications du premier. Malheureusement, on a pas pu finir cette version. 


### Répertoires du projet :

Dans le répertoire Mastermind, on trouve en plus de ce rapport : 
- Un répertoire « Mastermind_basique » qui contient la première version.
- Un répertoire « Mastermind_client_serveur » qui contient la deuxième version.
- Un répertoire « Mastermind_graphiqiue » qui contient la troisième. 
- Un fichier **README.md** qui décrit en détail la démarche à suivre pour faire fonctionner le jeu. 


###Les différentes versions : 

- Le mastermind basique :
Cette version a été la plus simple à programmer. Son implémentation nous a permis de nous familiariser avec le langage python. Ce qui est bien dans cette version est que l’on peut jouer seul, comme jouer à deux. 

- Le mastermind version TCP :
est la deuxième étape de notre projet. On a donc implémenté un serveur local qui peut prendre au maximum 1000 clients, et les faire jouer simultanément. On aurait aimé que cette version fasse affronter les clients deux à deux mais on a fait le choix de faire jouer les clients contre le serveur.

Pour utiliser les fonctionnalités d'envoie et de réception de paquets, on a importé le module socket, qui contient les fonctions send() et recv(). Ces dernières permettent respectivement d'envoyer et de recevoir des paquets de la part du client ou du serveur. 

Notre serveur n'a malheureusement pas de graceful shutdown mais les clients en ont un. En effet, ils quittent la partie en fermant la socket de connexion et envoient un message 'FIN' au serveur pour qu'il ferme la connexion de son côté aussi. Mais étant donné qu'on n'a pas de connaissance sur les signaux en python, on ignore comment interpréter un SIGINT en une autre action qui fermerait la socket du serveur.

- Mastermind avec interface graphique :
Après avoir fait le jeu sur terminal, et un essai sur tcp. On a travaillé sur la partie graphique. Malheureusement, l'implémentation des différents programmes nous a pris plus de temps que prévu et l'assemblage des trois version n'a pas pu être fait convenablement.

La version graphique n'a donc pas beauoup de fonctions et ne peut être joué s'il n'y a pas deux joueurs, et il est seulement possible  d'y jouer en local.
Le code n'est donc pas très compliqué et il contient beaucoup de test conditionnel puisque les tests comme "case" en C n'existe pas.
Nous avons remarqué par ailleurs qu'il n'est pas aussi simple qu'on le pensait de programmer en python, mais qu'il n'est pas impossible de créer quelque chose à partir de rien.
L'utilisation de la bibliothèque pygame est une partie importante du programme et nous avons appris qu'il est très difficile de faire une interface graphique.



### Les règles du jeu :
Les règles du jeu sont expliquées dans la première et la deuxième versions sous forme d’une petite histoire. Dans la troisième, elles sont expliquées brièvement mais pour l’instant on les a pas encore mises. 

La machine (ou le joueur dans le mode duo) devra générer  une combinaison de n parmi 7 dans la première et la deuxième version selon le niveau de difficulté choisi. Quant à la troisième version, le joueur doit générer une combinaison de 4 couleurs.
Le joueur devra par la suite essayer  de deviner la combinaison. A chaque tentative, le programme ou l’autre joueur lui donnera des indications : 
    • La couleur blanche signifie qu’une couleur est à la bonne position dans la combinaison. 
    • La couleur rouge signifie qu’une couleur est bien présente dans la combinaison mais n’est pas à la bonne place. 
    • La couleur noire signifie qu’une couleur n’est pas dans la combinaison. 
Le joueur aura un maximum de 10 tentatives pour deviner la combinaison. 


## Répartition des tâches : 
Concernant la répartition des tâches, on a pas fait ça de manière claire. Les 4 membres du groupe ont touché aux 3 versions du projets. Mais certains ont travaillé plus sur l’affichage, d’autres sur le client/serveur ou sur la version graphique qui s’est avérée plus compliquée que ce qu’on aurait pu imaginer. On a cependant préféré travailler sur Jitsi, Discord et Whatsapp au lieu de créer un dépôt Git car on est habitué à ces logiciels et aussi on est pas encore très familiers avec l’utilisation de Git. Pour envoyer le lien aux prof, on a décidé de mettre le dépôt sur le compte Git de Yanis puisque c’est le seul qui en possède un pour l’instant. 


## Problèmes rencontrées :
    • Le python n’étant pas un langage enseigné systématiquement à l’Institut Galilée, on a d’abord commencé à l’apprendre avant de faire tout autre chose. C’est un langage facile à prendre en main pour les fonctions de base mais ayant fait la plupart de nos cours en C, comme la partie réseau et la multiprogrammation, on a mis un peu de temps à assimiler cette partie en python. 
    • On a pas eu de problème à implémenter la première approche car c’est la plus simple. On a appris le python dessus. 
    • La deuxième approche fût un peu compliquée, car comme dit en haut, la multiprogrammation et la conception client/serveur on les a faites en C. Du coup, on a eu un problème avec l’envoie des paquets, la programmation multitâche. Des problèmes avec les fonctions send() et recv()  qui sont bloquantes. On a également eu à découvrir des nouvelles fonctions qu’on n’a jamais vues en C telles que decode() et encode(). 
    • La troisième approche fût la plus compliquée car on a jamais conçu d’interface graphique auparavant, ni eu des cours dessus. Ça nous a pris beaucoup plus de temps que prévu et on a pas pu la finir.  



## Solutions trouvées 
    • L’entraide entre les membres du groupes nous a permis de rapidement prendre en main le langage python. Yanis et Youcef qui ont eu une initiation à la robotique ont aidé Dihia et Marie à l’apprendre rapidement. 
    • On a réglé le problème de la synchronisation en utilisant la fonction time.sleep().
    • On a utilisé le module multiprocessing et la fonction process pour pouvoir concevoir un programme multitâche. 
    • Pour l’interface graphique, on a tous cherché sur internet des tutos et regardé des vidéos youtube pour apprendre à créer des interfaces graphiques, mais on ne les maîtrise pas encore. 

#Rapports individuels 

##Yanis HOURI

1-Expérience de cor-coordination: 
Ce projet nous a demandé une très forte coordination avec mes camarades. Notre projet contient plusieurs variantes de mastermind, une version basique sur console, une version client/serveur TCP et une version graphique. On s'est entraidé sur toutes les parties de notre projet, que ce soit sur l'apprentissage des bases de python, les sockets et les bases de pygame. On a d'abord implémenté le jeu sur terminale puis après le cours de TCP/UDP qu'on a eu en 'Système et réseau' on a décidé de faire une version client/serveur. L'idée de la version graphique nous est venu à la fin c'est pour ça qu'elle beaucoup moins complète comparée aux autres. 


2-Ma contribution:
En ayant étudié le langage C depuis la première année, la prise en main de python a été instantanée. 

J'ai touché à toutes les versions un peu moins la version graphique. L'implémentation sur console était la partie la plus simple selon moi comparée à la version client/serveur ou à la version graphique.

J'ai eu quelques difficultés dans l'implémentation du client serveur, surtout pour rendre le serveur multitâche. On a vu les fork et les threads en architecture système et en système et réseau, mais ces dernières sont implémentées différemment en python. Pour ce faire, on a inclus le module multiprocessing qui avec la fonction Process on crée des processus enfants qui s'exécutent en parallèle. On n'a pas utilisé de fonctions qui attendent la terminaison des autres processus car chaque joueur est indépendant, chacun peut mettre fin à la partie quand il veut sans impacter la partie en cours d'un autre joueur. De plus, j'ai eu des difficultés dans l'envoie et la réception des paquets, avec les fonctions encode() et decode() qu'on a jamais utilisé en C. 

Concernant la partie graphique, c'est la partie ou à laquelle j’ai le moins contribué. Avant d'avoir l'idée de faire une version du jeu avec pygame on a eu l'idée d'afficher des étoiles symbolisant les pions à placer sur le plateau du jeu et ajouter des personnage avec cowsay pour créer une histoire autour du jeu et ajouter plus d'immersion dans ce dernier. 



3-Ce qu'on aurait pu faire: 
1- La version client/serveur aurait pu être une version multijoueur du jeu. Le serveur connecte deux client et les fait affronter. De plus, si on avait plus de connaissances sur le multithreading, on aurait pu faire une threadpool qui aurait une meilleure optimisation et qui augmenterait le nombre de clients qui pourraient se connecter au serveur. 

2-On aurait pu apporter une meilleure version graphique du jeu (plus complète) avec tous les modes de jeu possibles. 

3-On aurait pu se pencher sur un langage plus adapté aux jeux vidéos comme le C++ pour avoir une version 100% graphique et complète.

4-Faire un graceful shutdown au serveur en sauvegardant le score des joueurs et les afficher à la demande de ces derniers 

4-Retour d’expérience :
Ce projet a été une occasion pour moi d'apprendre davantage de choses sur python et la programmation de jeux vidéos. J'ai aussi constaté que python n'était pas forcément le langage adéquat pour implémenter des jeux graphiquement.
De plus, cette expérience m'a fait comprendre à quel point le travail d'équipe est important dans le domaine du développement et de la programmation.


##Dihia HADJALI

Expérience de co-coordination :

Étant de nature discrète, j’ai d’habitude du mal à m’intégrer dans des groupes. Cependant, ce projet m’a permis de collaborer parfaitement avec mes camarades, qui, j’ai de la chance sont aussi mes amis. En effet, on discutait régulièrement sur le projet que ce soit virtuellement ou à la fac quand on a la chance de nous y retrouver. On faisait régulièrement des vision-conférences notamment sur Jitsi.  Le fait qu’on ne se soit pas clairement réparti les tâches a amélioré notre coordination. On a tous touché à toutes les versions du projet, on a travaillé ensemble sur toutes les parties et à chaque fois que l’un de nous rencontrait un problème, il y avait quelqu’un pour l’aider. 


Ma contribution :

Comme je l’ai mentionné plus haut, tout le monde a contribué à toutes les versions du projet. J’ai par exemple participé à l’implémentation des programmes, l’invention de l’histoire, la rédaction du rapport et à la création d’un menu pour l’interface graphique qu’on a malheureusement pas pu afficher finalement. 

Les difficultés sur les parties auxquelles j’ai contribué et les solutions utilisées : 
    • L’interface graphique a particulièrement  été difficile à programmer. En effet, je n’ai pas réussi à afficher le menu. Bien que j’aie regardé des vidéos traitant le sujet, je n’ai pas pu faire grand-chose sur cette partie. 
    • Le python m’étant un langage complètement inconnu, j’ai du commencer par son apprentissage. 
      

Une réflexion sur ce que j’aurais fait différemment : 
    • J’aurais commencé bien plus tôt. 
    • J’aurais sollicité l’aide des profs. 
    • J’aurais aimé apprendre davantage sur les interfaces graphiques afin de pouvoir implémenter un jeu graphique digne de ce nom. 
    • J’aurai pris de tester la version client/serveur sur plusieurs machines.
    • J’aurais implémenté un client/serveur en duo. Deux clients qui essaient de trouver une combinaison que le programme génère, le premier à ce faire gagne. Ou un client qui génère une combinaison qu’il fera deviner à un autre client


Retour d’expérience : 

Ce projet m’a permis de prendre en main un langage que je ne connaissais absolument pas, d’apprendre comment on programme des jeux et avoir une idée de comment on programme des interfaces graphiques. Je compte bien en apprendre davantage sur ce domaine d’ailleurs.
Cela m’a permis également de collaborer avec des camarades alors que ce n’est pas de mes habitudes. De m’intégrer harmonieusement dans une équipe. Cette dernière capacité est en effet indispensable si à l’avenir je veux travailler dans une entreprise. 
Le fait que nous ayons réussi à programmer ce jeu me donne confiance et me motive à en créer d’autres. 
Cela m’a permis aussi de mettre en  pratique mes connaissances théoriques. 


##Marie FU

Lors d'une discussion en groupe, on s'est répati les tâches à faire et je me suis occupé de la partie graphique du jeu, pendant que le reste du groupe travaillait sur une version du jeu sur 
terminal et une possible version avec le jeu en tcp.

Pendant l'écriture du programme, j'en ai appris beaucoup sur  python, notamment l'importance de l'indentation puisqu'il n'y a pas de séparateurs comme ";". Pour prrogrammer le jeu, j'ai utilisé le
logiciel PyCharm et la bibliothèque pygame.
Ce qui m'a pris plus de temps que prévu était la conception du support graphique avec des images à dessiner et redimensionner. Il fallait que j'optimise l'espace de ma fenêtre pour ne pas avoir 
quelque chose de désordonné.
Les problèmes que j'ai rencontré ont souvent été liés à ma méconnaissance du langage et à des problèmes sur les conditions, il y en a beaucoup qui sont emboitées les uns dans les autres et rend 
le code assez illisible par moment. J'ai aussi eu quelque problème  d'affichage d'image et ne sachant pas supprimer une image déjà affichée, j'ai mis des images vides.

Je trouve cette expérience satisfaisante, surtout quand je  réussit à résoudre un problème et que le code fonctionne. Bien que  je trouve l'interface assez fade, puisque je ne suis pas arrivée à 
faire en sorte qu'un fond ne soit pas impacté par les affichages que je fait pas dessus.


##Youcef Ould Kaci

Après le choix du jeu, on s'est réparti les tâches à faire un groupe (dont je fais partie) pour la partie développement, on  a travaillé ensemble sur les fonctions du jeu, et les 2 diffèrent 
mode, et à la fin sur une éventuelle version TCP du jeu. Lors de l'écriture du code , j'ai dû faire des recherches et regarder des vidéos pour en apprendre plus sur Python , et Pygame plus précisément qui est une bibliothèque pour coder des jeux. 

Les problèmes que j’ai rencontrés mis à part le peu de savoir que j'ai sur Python, c'est de d'envoyer des paquets (messages) entre clients TCP , du coup on a pas réussi à implémenter le mode duo sur 
la version TCP du jeu.

Ce que j'aurais fait différemment si je m'y prend maintenant, c'est de consacrer plus de temps pour la partie TCP , pour faire jouer deux clients ensemble, mais je trouve qu'on a déjà fait un bon travail
avec une bonne ambiance.
