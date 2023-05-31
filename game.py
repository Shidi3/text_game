import pygame
pygame.init()

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
        font = pygame.font.Font('shrift.ttf', 70)
        self.text = font.render(text, True, color_text)
        rect = self.text.get_rect()
        rect.center = (self.x + self.w // 2, self.y + self.h // 2)
        win.blit(self.text, rect)

def settext(a, b, c, x, y):
    font = pygame.font.Font('shrift.ttf', a)
    text_go = font.render(b, 1, c)
    text_rect = text_go.get_rect()
    text_rect.center = (x // 2, y)
    win.blit(text_go, text_rect)

def game():
    win.blit(fon1, (0, 0))
    f1 = settext(70, 'Лонданская ночь.', (50, 50, 50), 1000, 50)
    f2 = settext(71, 'Лонданская ночь.', (150, 150, 150), 1000, 50)
    btn1 = Button(196, 146, 608, 108, (150, 150, 150))
    btn1.draw(win)
    btn2 = Button(200, 150, 600, 100, (80, 80, 80))
    btn2.draw(win)
    btn2.set_text('Начать', (200, 200, 200))
    btn3 = Button(196, 306, 608, 108, (150, 150, 150))
    btn3.draw(win)
    btn4 = Button(200, 310, 600, 100, (80, 80, 80))
    btn4.draw(win)
    btn4.set_text('Выйти', (200, 200, 200))


###

run = True
fps = 60
clock = pygame.time.Clock()
win = pygame.display.set_mode((1000, 500))
slaide=1
fon1 = pygame.image.load('sity.jpeg')
fon1 = pygame.transform.scale(fon1, (1000, 500))

###

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #if event.type == pygame.MOUSEBUTTONPUSH:


    game()
    pygame.display.update()
    clock.tick(fps)
