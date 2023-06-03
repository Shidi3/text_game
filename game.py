from time import sleep
import pygame
pygame.init()

###

class Game():
    def __init__(self):
        self.slide = 1
        self.stroka = 1

def img(x, y, img, w, h, win):
    img = pygame.image.load(img)
    img = pygame.transform.scale(img, (w, h))
    rect = img.get_rect()
    rect.x = x
    rect.y = y
    win.blit(img, rect)

def scremer(x, y, img, w, h, win):
    img = pygame.image.load(img)
    img = pygame.transform.scale(img, (w, h))
    rect = img.get_rect()
    rect.x = x
    rect.y = y
    a = 0
    while a != 5:
        win.blit(fon4, (0, 0))
        win.blit(img, rect)
        rect.x += 5
        rect.y += 5
        w += 5
        h += 5

def settext(a, b, c, x, y):
    font = pygame.font.Font('font.ttf', a)
    text_go = font.render(b, 1, c)
    text_rect = text_go.get_rect()
    text_rect.center = (x // 2, y)
    win.blit(text_go, text_rect)

def game_begin(): #начальная  страница
    win.blit(fon1, (0, 0))
    f1 = settext(80, 'Не пейте много пива на ночь.', (150, 150, 150), 1500, 150)
    f1_1 = settext(70, 'Начать - пробел', (150, 150, 150), 1500, 400)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game.slide += 1
        sleep(0.5)
        del f1
        del f1_1

def slide2(): #первая развилка
    win.blit(fon2, (0,0))
    if game.stroka == 1:
        f2 = settext(30, 'Вы очнулись в страшной комнате.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f2
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 2:
        f3 = settext(30, 'Последнее что вы помните, это большая кружка вкусного пива.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f3
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 3:
        f4 = settext(30, 'Зря вы много выпили.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f4
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 4:
        f5 = settext(30, 'Вы поднимаетесь с жесткой кровати.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f5
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 5:
        f6 = settext(30, 'Ваши действия: 1 - подойти к окну, 2 - проверить дверь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            game.slide += 1
        elif keys[pygame.K_2]:
            game.slide += 2
        elif keys[pygame.K_3]:
            game.slide += 3
        del f6

def slide3_1(): #развилка 1; вариант развития 1
    win.blit(fon3, (0, 0))
    if game.stroka == 5:
        f7 = settext(30, 'Вы подошли к окну.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f7
            game.stroka += 1
            game.slide += 1
            sleep(0.5)

def slide3_2(): #развилка 1; вариант 1; продолжение
    win.blit(fon4, (0, 0))
    if game.stroka == 6:
        f8 = settext(30, 'На улице шел дождь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f8
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 7:
        f9 = settext(30, 'Вы наблюдаете за жизнью одинокой улицы.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f9
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 8:
        f10 = settext(30, 'Нормальные люди сейчас спят в своей теплой, мягкой кроватке.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f10
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 9:
        f11 = settext(30, 'А вы даже не знаете, где находитесь.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f11
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 10:
        img(567, 478, 'ten.png', 150, 150, win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            sleep(0.5)
            win.blit(fon4, (0,0))
    elif game.stroka == 11:
        f12 = settext(30, 'Что это было?', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f12
            game.stroka += 1
            sleep(0.5)
            game.slide +=1

def slide3_3(): #развилка 1; вариант 1; начало новой развилки
    if game.stroka == 12:
        f13 = settext(30, 'Может птичка пролетела...', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f13
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 13:
        img(567, 478, 'ruk.png', 150, 150, win)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.stroka += 1
            sleep(0.5)
    elif game.stroka == 14:
        f14 = settext(30, 'Ваши действия: 1 - продолжать смотреть в окно, 2 - побежать к двери.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        del f14
        if keys[pygame.K_1]:
            game.slide += 1
        elif keys[pygame.K_2]:
            game.slide += 2
        elif keys[pygame.K_3]:
            game.slide += 3



def slide4_1(): #развилка 1_1; вариант 1
    if game.stroka == 14:
        f15 = settext(30, 'Вы продолжаете дальше смотреть в окно.', (150, 150, 150), 1500, 70)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            del f15
            game.stroka += 1
            sleep(0.5)

###

game = Game()
run = True
fps = 30
clock = pygame.time.Clock()
win = pygame.display.set_mode((1500, 700))
slaide = 1
fon1 = pygame.image.load('b.jpeg')
fon1 = pygame.transform.scale(fon1, (1500, 700))
fon2 = pygame.image.load('po.jpg')
fon2 = pygame.transform.scale(fon2, (1500, 700))
fon3 = pygame.image.load('ch.png')
fon3 = pygame.transform.scale(fon3, (1500, 700))
fon4 = pygame.image.load('okno.jpg')
fon4 = pygame.transform.scale(fon4, (1500, 700))

###

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if game.slide ==  1:
        game_begin()
    elif game.slide == 2:
        slide2()
    elif game.slide == 3:
        slide3_1()
    elif game.slide == 4:
        slide3_2()
    elif game.slide == 5:
        slide3_3()
    elif game.slide == 6:
        slide4_1()

    pygame.display.update()
    clock.tick(fps)
