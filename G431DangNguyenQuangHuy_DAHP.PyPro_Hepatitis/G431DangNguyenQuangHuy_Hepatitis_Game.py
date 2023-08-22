import pygame, random
from pygame.locals import *
from tkinter import messagebox as huy31mess
LANEWIDTH = 60
X_MARGIN = 80
class Game:
    def __init__(self):
        pygame.init()
        self.WINDOWWIDTH = 400
        self.WINDOWHEIGHT = 600
        self.DISTANCE = 200
        self.OBSTACLESSPEED = 2
        self.CHANGESPEED = 0.001
        self.OBSTACLESIMG = pygame.image.load('./G431DangNguyenQuangHuy_Hepatitis/obstacles.png')
        self.CARWIDTH = 40
        self.CARHEIGHT = 60
        self.CARSPEED = 3
        self.CARIMG = pygame.image.load('./G431DangNguyenQuangHuy_Hepatitis/car.png')
        self.FPS=60
        self.fpsClock = pygame.time.Clock() 
        self.BGSPEED = 1.5 # tốc độ cuộn nền
        self.FPS = 60 # Famres Per Second
        self.fpsClock = pygame.time.Clock() #Lặp theo nhịp clock (tham số FPS)
        self.BGIMG = pygame.image.load('./G431DangNguyenQuangHuy_Hepatitis/background.png') # hình nền
        self.DISPLAYSURF = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption('31 Đặng Nguyễn Quang Huy = Ex7.5: Game = Game ĐUA XE')
# LỚP HÌNH NỀN = CUỘN NỀN
class Background(Game):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.speed = self.BGSPEED
        self.img = self.BGIMG
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def draw(self):
        self.DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
        self.DISPLAYSURF.blit(self.img, (int(self.x), int(self.y-self.height)))
    def update(self):
        self.y += self.speed
        if self.y > self.height:
            self.y -= self.height
#LỚP XE TRONG GAME
class Car(Game):
    def __init__(self):
        super().__init__()
        self.width = self.CARWIDTH
        self.height = self.CARHEIGHT
        self.x = (self.WINDOWWIDTH-self.width)/2
        self.y = (self.WINDOWHEIGHT-self.height)/2
        self.speed = self.CARSPEED
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill((255, 255, 255))
    def draw(self):
        self.DISPLAYSURF.blit(self.CARIMG, (int(self.x), int(self.y)))
    def update(self, moveLeft, moveRight, moveUp, moveDown):
        if moveLeft == True:
            self.x -= self.speed
        if moveRight == True:
            self.x += self.speed
        if moveUp == True:
            self.y -= self.speed
        if moveDown == True:
            self.y += self.speed

        if self.x < X_MARGIN:
            self.x = X_MARGIN
        if self.x + self.width > self.WINDOWWIDTH - X_MARGIN:
            self.x = self.WINDOWWIDTH -X_MARGIN - self.width
        if self.y < 0:
            self.y = 0
        if self.y + self.height >self. WINDOWHEIGHT :
            self.y = self.WINDOWHEIGHT - self.height
class Obstacles(Game):
    def __init__(self):
        super().__init__()
        self.width = self.CARWIDTH
        self.height = self.CARHEIGHT
        self.distance = self.DISTANCE
        self.speed = self.OBSTACLESSPEED
        self.changeSpeed = self.CHANGESPEED
        self.ls = []
        for i in range(5):
            y = -self.CARHEIGHT-i*self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
    def draw(self):
        for i in range(5):
            x = int(X_MARGIN + self.ls[i][0]*LANEWIDTH + (LANEWIDTH-self.width)/2)
            y = int(self.ls[i][1])
            self.DISPLAYSURF.blit(self.OBSTACLESIMG, (x, y))
    def update(self):
        for i in range(5):
            self.ls[i][1] += self.speed
        self.speed += self.changeSpeed
        if self.ls[0][1] > self.WINDOWHEIGHT:
            self.ls.pop(0)
            y = self.ls[3][1] - self.distance
            lane = random.randint(0, 3)
            self.ls.append([lane, y])
class Score(Game):
    def __init__(self):
        super().__init__()
        self.score = 0
    def draw(self):
        font = pygame.font.SysFont('consolas', 30)
        scoreSuface = font.render('Score: '+str(int(self.score)), True, (0, 0, 0))
        self.DISPLAYSURF.blit(scoreSuface, (10, 10))
    def update(self):
        self.score += 0.02
def rectCollision(rect1, rect2):
    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
        return True
    return False
def isGameover(car, obstacles):
    carRect = [car.x, car.y, car.width, car.height]
    for i in range(5):
        x = int(X_MARGIN + obstacles.ls[i][0]*LANEWIDTH + (LANEWIDTH-obstacles.width)/2)
        y = int(obstacles.ls[i][1])
        obstaclesRect = [x, y, obstacles.width, obstacles.height]
        if rectCollision(carRect, obstaclesRect) == True:
            return True
    return False
class Run(Game):
    def __init__(self):
        super().__init__()
    def gameOver(self,bg, car, obstacles, score):
            font = pygame.font.SysFont('consolas', 60)
            headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
            headingSize = headingSuface.get_size()
            font = pygame.font.SysFont('consolas', 20)
            commentSuface = font.render('Press "space" to replay', True, (0, 0, 0))
            commentSize = commentSuface.get_size()
            while True:
                try:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.display.quit()
                        if event.type == pygame.KEYUP:
                            if event.key == K_SPACE:
                                return
                except:
                    huy31mess.showerror("Thông Báo!","Có Lỗi Xảy Ra")
                    return
                bg.draw()
                car.draw()
                obstacles.draw()
                score.draw()
                self.DISPLAYSURF.blit(headingSuface, (int((self.WINDOWWIDTH - headingSize[0])/2), 100))
                self.DISPLAYSURF.blit(commentSuface, (int((self.WINDOWWIDTH - commentSize[0])/2), 400))
                pygame.display.update()
                self.fpsClock.tick(self.FPS)

    def gameStart(self,bg):
            bg.__init__()
            font = pygame.font.SysFont('consolas', 60)
            headingSuface = font.render('RACING', True, (255, 0, 0))
            headingSize = headingSuface.get_size()
            font = pygame.font.SysFont('consolas', 20)
            commentSuface = font.render('Press "space" to play', True, (0, 0, 0))
            commentSize = commentSuface.get_size()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        return
                    if event.type == pygame.KEYUP:
                        if event.key == K_SPACE:
                            return
                bg.draw()
                self.DISPLAYSURF.blit(headingSuface, (int((self.WINDOWWIDTH - headingSize[0])/2), 100))
                self.DISPLAYSURF.blit(commentSuface, (int((self.WINDOWWIDTH - commentSize[0])/2), 400))
                pygame.display.update()
                self.fpsClock.tick(self.FPS)

    def gamePlay(self,bg, car, obstacles, score):
            car.__init__()
            obstacles.__init__()
            bg.__init__()
            score.__init__()
            moveLeft = False
            moveRight = False
            moveUp = False
            moveDown = False
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            moveLeft = True
                        if event.key == K_RIGHT:
                            moveRight = True
                        if event.key == K_UP:
                            moveUp = True
                        if event.key == K_DOWN:
                            moveDown = True
                    if event.type == KEYUP:
                        if event.key == K_LEFT:
                            moveLeft = False
                        if event.key == K_RIGHT:
                            moveRight = False
                        if event.key == K_UP:
                            moveUp = False
                        if event.key == K_DOWN:
                            moveDown = False

                if isGameover(car, obstacles):
                    return
                bg.draw()
                bg.update()
                car.draw()
                car.update(moveLeft, moveRight, moveUp, moveDown)
                obstacles.draw()
                obstacles.update()
                score.draw()
                score.update()
                pygame.display.update()
                self.fpsClock.tick(self.FPS)
