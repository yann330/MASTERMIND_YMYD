import pygame
from ecran import Ecran

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '200,300'

colorEmpty = pygame.image.load(os.path.join('image', 'vide.png'))
rules1 = pygame.image.load(os.path.join('image', 'regle_p1.png'))
background_menu = pygame.image.load(os.path.join('image', 'fond_menu.png'))

surface = pygame.display.set_mode((650, 1000))  # taille de l'ecran
pygame.display.set_caption('Mastermind')  # nom de l'entête

ecran = Ecran()
running = True
player = "codeur"
combi = 1
color_c = 1
color_d = 5
essai = 0
choix = []
combi_essai = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if (pos[0] // 50 == 1) & (pos[1] // 50 == 1):
                    running = False
                if player == "decodeur":
                    if ((pos[0] // 50 >= 3) & (pos[0] // 50 <= 6) & (pos[1] // 50 == essai)) \
                                or ((pos[0] // 50 == 1) & (pos[1] // 50 == 8)):
                        ecran.get_mouse(pos[0] // 50, pos[1] // 50, color_d)
                elif player == "codeur":
                    if (((pos[0] // 50 >= 8) & (pos[0] // 50 <= 11) & (pos[1] // 50 == essai))
                            or ((pos[0] // 50 == 1) & (pos[1] // 50 == 8))) & (combi == 0):
                        ecran.get_mouse(pos[0] // 50, pos[1] // 50, color_c)
                    elif (((pos[0] // 50 >= 8) & (pos[0] // 50 <= 11) & (pos[1] // 50 == 0)
                          or (pos[0] // 50 == 1) & (pos[1] // 50 == 8))) & (combi == 1):
                        ecran.get_mouse(pos[0] // 50, pos[1] // 50, color_d)
                if ecran.switch_player:
                    if player == "codeur":
                        if combi == 1:
                            if (color_d < 10) & (color_d >= 5):
                                color_d = color_d + 1
                            else:
                                color_d = 5
                            if (pos[0] // 50 == 1) & (pos[1] // 50 == 8):
                                player = "decodeur"
                                combi = 0
                                choix = ecran.cacher_et_creer_combi(8, 0)
                        if combi == 0:
                            if (color_c < 3) & (color_c >= 1):
                                color_c = color_c + 1
                            else:
                                color_c = 1
                            if (pos[0] // 50 == 1) & (pos[1] // 50 == 8):
                                player = "decodeur"
                                essai = essai + 1
                    elif player == "decodeur":
                        if (color_d < 10) & (color_d >= 5):
                            color_d = color_d + 1
                        else:
                            color_d = 5
                        if (pos[0] // 50 == 1) & (pos[1] // 50 == 8):
                            player = "codeur"
                            combi_essai = ecran.combinaison_essai(3, essai)
                            if ecran.compare_combi(choix, combi_essai):
                                ecran.affiche_gagnant(2)
                            elif essai >= 10:
                                ecran.affiche_gagnant(1)

    surface.fill((250, 250, 250))
    ecran.draw(surface)
    pygame.display.flip()
