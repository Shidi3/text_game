from time import sleep
import pygame
pygame.init()
class Game():
    def __init__(self):
        self.slide=1
        self.stroka=1
class Button():
    def __init__(self, x, y, w = 200, h = 400, color=(255,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.h))

    def set_text(self, text='Вопрос', color_text=(255, 255, 255)):
        font = pygame.font.Font('font.ttf', 70)
        self.text = font.render(text, True, color_text)
        rect = self.text.get_rect()
        rect.center = (self.x + self.w // 2, self.y + self.h // 2)
        win.blit(self.text, rect)
#def a(x, y, img, x_end, y_end, speed):



def settext(a, b, c, x, y):
    font = pygame.font.Font('font.ttf', a)
    text_go = font.render(b, 1, c)
    text_rect = text_go.get_rect()
    text_rect.center = (x // 2, y)
    win.blit(text_go, text_rect)

def game_begin():
    win.blit(fon1, (0, 0))
    f1 = settext(130, 'Лондонская ночь.', (50, 50, 50), 1500, 150)
    f2 = settext(131, 'Лондонская ночь.', (150, 150, 150), 1500, 150)
    btn1 = Button(196, 326, 1108, 168, (150, 150, 150))
    btn1.draw(win)
    btn2 = Button(200, 330, 1100, 160, (80, 80, 80))
    btn2.draw(win)
    btn2.set_text('Начать (q)', (200, 200, 200))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        game.slide += 1

def slide2():
    win.blit(fon2, (0,0))
    if game.stroka == 1:
        f3 = settext(30, 'Вы очнулись в страшной комнате.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f3 = ''
            game.stroka += 1
            sleep(1)
    elif game.stroka == 2:
        f4 = settext(30, 'Последнее что вы помните, это большая кружка вкусного пива.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f4 = ''
            game.stroka += 1
            sleep(1)
    elif game.stroka == 3:
        f5 = settext(30, 'Зря вы много выпили.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f5 = ''
            game.stroka += 1
            sleep(1)
    elif game.stroka == 4:
        f6 = settext(30, 'Вы поднимаетесь с жесткой кровати.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f6 = ''
            game.stroka += 1
            sleep(1)
    elif game.stroka == 5:
        f7 = settext(30, 'Ваши действия: 1 - подойти к окну, 2 - проверить дверь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            game.slide += 1
        elif keys[pygame.K_2]:
            game.slide += 2
        elif keys[pygame.K_3]:
            game.slide += 3

def slide3():
    win.blit(fon3, (0, 0))
    if game.stroka == 5:
        f7 = settext(30, 'Вы подошли к окну.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f7 = ''
            game.stroka += 1
            game.slide += 1
            sleep(1)
def slide4():
    win.blit(fon4, (0, 0))
    if game.stroka == 6:
        f8 = settext(30, 'На улице шел дождь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f8 = ''
            game.stroka += 1
            sleep(1)
    elif game.stroka == 7:
        f9 = settext(30, 'Вы наблюдаете за жизнью одинокой улицы.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f9 = ''
            game.stroka += 1
            sleep(1)
    elif game.stroka == 8:
        f10 = settext(30, 'Нормальные люди сейчас спят в своей теплой, мягкой кроватке.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f10 = ''
            game.stroka += 1
            sleep(1)
    elif game.stroka == 9:
        f11 = settext(30, 'А вы даже не знаете, где находитесь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            f11 = ''
            game.stroka += 1
            sleep(1)
    #elif game.stroka == 10:


###
game = Game()
run = True
fps = 60
clock = pygame.time.Clock()
win = pygame.display.set_mode((1500, 700))
slaide=1
fon1 = pygame.image.load('l.jpeg')
fon1 = pygame.transform.scale(fon1, (1500, 700))
fon2 = pygame.image.load('po.jpg')
fon2 = pygame.transform.scale(fon2, (1500, 700))
fon3 = pygame.image.load('ch.png')
fon3 = pygame.transform.scale(fon3, (1500, 700))
fon4 = pygame.image.load('okno.jpg')
fon4 = pygame.transform.scale(fon4, (1500, 700))
ten = pygame.image.load('ten.png')
###

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEBUTTONPUSH:
    if game.slide==1:
        game_begin()
    elif game.slide == 2:
        slide2()
    elif game.slide == 3:
        slide3()
    elif game.slide == 4:
        slide4()


    pygame.display.update()
    clock.tick(fps)
