import pygame
import os

colorWhite = pygame.image.load(os.path.join('image', 'blanc.png'))
colorBlack = pygame.image.load(os.path.join('image', 'noir.png'))
colorRed = pygame.image.load(os.path.join('image', 'rouge.png'))
colorYellow = pygame.image.load(os.path.join('image', 'jaune.png'))
colorGreen = pygame.image.load(os.path.join('image', 'vert.png'))
colorPurple = pygame.image.load(os.path.join('image', 'violet.png'))
colorGrey = pygame.image.load(os.path.join('image', 'gris.png'))
colorSky = pygame.image.load(os.path.join('image', 'ciel.png'))
colorBlue = pygame.image.load(os.path.join('image', 'bleu.png'))
colorEmpty = pygame.image.load(os.path.join('image', 'vide.png'))
c_gagne = pygame.image.load(os.path.join('image', 'codeur_gagne.png'))
d_gagne = pygame.image.load(os.path.join('image', 'decodeur_gagne.png'))
next_p = pygame.image.load(os.path.join('image', 'next.png'))
prec_p = pygame.image.load(os.path.join('image', 'prec.png'))
cs_c = pygame.image.load(os.path.join('image', 'consigne_codeur.png'))
cs_d = pygame.image.load(os.path.join('image', 'consigne_decodeur.png'))
cs_d_c = pygame.image.load(os.path.join('image', 'consigne_donner_combi.png'))
background_menu = pygame.image.load(os.path.join('image', 'fond_menu.png'))


class Ecran:
    def __init__(self):
        # tracer de l'ecran
        self.ecran_lines = [((50, 50), (100, 50)), ((150, 50), (350, 50)), ((400, 50), (600, 50)),
                            ((50, 100), (100, 100)), ((150, 100), (350, 100)), ((400, 100), (600, 100)),
                            ((50, 150), (100, 150)), ((150, 150), (350, 150)), ((400, 150), (600, 150)),
                            ((150, 200), (350, 200)), ((400, 200), (600, 200)),
                            ((150, 250), (350, 250)), ((400, 250), (600, 250)),
                            ((150, 300), (350, 300)), ((400, 300), (600, 300)),
                            ((150, 350), (350, 350)), ((400, 350), (600, 350)),
                            ((150, 400), (350, 400)), ((400, 400), (600, 400)),
                            ((150, 450), (350, 450)), ((400, 450), (600, 450)),
                            ((150, 500), (350, 500)), ((400, 500), (600, 500)),
                            ((150, 550), (350, 550)), ((400, 550), (600, 550)),
                            ((50, 50), (50, 150)),
                            ((100, 50), (100, 150)),
                            ((150, 50), (150, 550)),
                            ((200, 50), (200, 550)),
                            ((250, 50), (250, 550)),
                            ((300, 50), (300, 550)),
                            ((350, 50), (350, 550)),
                            ((400, 50), (400, 550)),
                            ((450, 50), (450, 550)),
                            ((500, 50), (500, 550)),
                            ((550, 50), (550, 550)),
                            ((600, 50), (600, 550)),
                            ((50, 400), (50, 450)), ((100, 400), (100., 450)),
                            ((50, 400), (100, 400)), ((50, 450), (100, 450))]
        self.ecran = [[0 for x in range(15)] for y in range(15)]
        self.switch_player = True

    def draw(self, surface):
        for line in self.ecran_lines:
            pygame.draw.line(surface, (0, 0, 0), line[0], line[1], 2)
        for y in range(len(self.ecran)):
            for x in range(len(self.ecran[y])):
                if self.get_cell_value(x, y) == 1:
                    surface.blit(colorWhite, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 2:
                    surface.blit(colorBlack, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 3:
                    surface.blit(colorRed, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 4:
                    surface.blit(colorEmpty, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 5:
                    surface.blit(colorYellow, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 6:
                    surface.blit(colorBlue, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 7:
                    surface.blit(colorSky, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 8:
                    surface.blit(colorGreen, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 9:
                    surface.blit(colorPurple, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 10:
                    surface.blit(colorGrey, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 12:
                    surface.blit(c_gagne, (x*50+1, y*50+1))
                elif self.get_cell_value(x, y) == 13:
                    surface.blit(d_gagne, (x*50+1, y*50+1))

    def print_ecran(self):
        for row in self.ecran:
            print(row)

    def get_cell_value(self, x, y):
        return self.ecran[y][x]

    def set_cell_value(self, x, y, value):
        self.ecran[y][x] = value

    def get_mouse(self, x, y, color):
        if color == 1:
            self.set_cell_value(x, y, 1)
        elif color == 2:
            self.set_cell_value(x, y, 2)
        elif color == 3:
            self.set_cell_value(x, y, 3)
        elif color == 5:
            self.set_cell_value(x, y, 5)
        elif color == 6:
            self.set_cell_value(x, y, 6)
        elif color == 7:
            self.set_cell_value(x, y, 7)
        elif color == 8:
            self.set_cell_value(x, y, 8)
        elif color == 9:
            self.set_cell_value(x, y, 9)
        elif color == 10:
            self.set_cell_value(x, y, 10)

    def cacher_et_creer_combi(self, x, y):
        choix = []
        for i in range(4):
            choix.append(self.get_cell_value(x+i, y))
            self.set_cell_value(x+i, y, 1)
        print(choix)
        return choix

    def combinaison_essai(self, x, y):
        combi_essai = []
        for i in range(4):
            combi_essai.append(self.get_cell_value(x+i, y))
        print(combi_essai)
        return combi_essai

    def compare_combi(self, choix, combi_essai):
        for i in range(4):
            if choix[i] != combi_essai[i]:
                return 0
        return 1

    def affiche_gagnant(self, int):
        if int == 1:
            self.set_cell_value(1, 12, 12)
        elif int == 2:
            self.set_cell_value(1, 12, 13)
