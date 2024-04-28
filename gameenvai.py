from typing import Tuple, Callable
import pygame
import sys
import random

class Base:
    ScreenSize:Tuple[int,int] = (1000,600)
    def __init__(self) -> None:
        self.ScreenSize = Base.ScreenSize
        self.ScreenWidth, self.ScreenHeight = self.ScreenSize
        self.keys = []
    def check(self):
        self.keys = pygame.key.get_pressed()
    @classmethod
    def GetKeys(cls, instance):
        return instance.keys
class Player(Base):
    def __init__(self,id:int,Width:int=16,Height:int=76) -> None:
        super().__init__()
        self.id = id
        self.Width = Width
        self.Height = Height
        self.Y = (self.ScreenHeight-self.Height)//2
        self.X = 15 if self.id%2 else self.ScreenWidth-self.Width-15
        self.speed = 5
        self.score = 0
    def Human(self):
        Base.check(self)
        keys = Base.GetKeys(self) 
        if keys[pygame.K_UP]:
            self.Y-=self.speed
        if keys[pygame.K_DOWN]:
            self.Y+=self.speed
        if self.Y > self.ScreenHeight:
            self.Y=-self.Height
        elif self.Y<-self.Height:
            self.Y=self.ScreenHeight
    def Unbeatable(self):
        pass
    def Play(self,Strategy:Callable=None):
        match Strategy:
            case None:
                self.Human()
            case 'Human':
                self.Human
            case 'Unbeatable':
                self.Unbeatable()
class Ball(Base):
    def __init__(self, id:int) -> None:
        super().__init__()
        self.id = id
        self.size = 15
        self.X = (self.ScreenWidth-self.size)//2
        self.Y = (self.ScreenHeight-self.size)//2
        self.Xspeed = 0
        self.Yspeed = 0
class Pong(Base):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode(self.ScreenSize)
        self.clock = pygame.time.Clock()
        self.isRunning = True
    def draw(self,x:int,y:int,w:int,h:int):
        pygame.draw.rect(self.screen,(255,155,155),(x,y,w,h))
    def updateScreen(self,ScreenColor:Tuple[int,int,int]=(0,0,0)):
        self.screen.fill(ScreenColor)
    def update(self):
        pygame.display.flip()
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
    def end(self):
        pygame.quit()
        sys.exit()
