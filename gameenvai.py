from typing import Tuple, Callable
import pygame #2.5.2 
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
    Player_instances = []
    def __init__(self,id:int,Width:int=16,Height:int=76) -> None:
        super().__init__()
        Player.Player_instances.append(self)
        self.id = id
        self.Width = Width
        self.Height = Height
        self.Y = (self.ScreenHeight-self.Height)//2
        self.X = 15 if self.id%2 else self.ScreenWidth-self.Width-15
        self.speed = 5
        self.score = 0
    @staticmethod
    def access_ball_stuff(index): 
        if 0<=index<len(Ball.ball_instances):
            return (Ball.ball_instances[index].X,Ball.ball_instances[index].Y,Ball.ball_instances[index].size)
        else:
            return None
    @staticmethod
    def access_ball_number():
        return len(Ball.ball_instances) if Ball.ball_instances else None

    def Human(self):
        Base.check(self)
        keys = Base.GetKeys(self) 
        if self.id%2:
            if keys[pygame.K_UP]:
                self.Y-=self.speed
            if keys[pygame.K_DOWN]:
                self.Y+=self.speed
        else:
            if keys[pygame.K_w]:
                self.Y-=self.speed
            if keys[pygame.K_s]:
                self.Y+=self.speed
        
    def Unbeatable(self):
        balls = []
        ballXs = []

        for i in range(self.access_ball_number()):
            balls.append(self.access_ball_stuff(i))

        if balls:
            # Populate ballXs with the first element of each ball tuple
            ballXs = [ball[0] for ball in balls]

            # Find the index of the minimum x value
            if self.id % 2:
                min_x = min(ballXs)
            else:
                min_x = max(ballXs)

            # Find the corresponding x value
            y = balls[ballXs.index(min_x)][1]
            #print (f'y: {y}, x: {min_x}, blls: {balls}')
            # Adjust player position based on the calculated y value

            if y > self.Y+balls[ballXs.index(min_x)][2] + self.speed :
                self.Y += self.speed
            elif y < self.Y+balls[ballXs.index(min_x)][2] - self.speed:
                self.Y -= self.speed

    def Play(self,Strategy:Callable=None):
        match Strategy:
            case None:
                self.Human()
            case 'Human':
                self.Human
            case 'Unbeatable':
                self.Unbeatable()
            

        if self.Y > self.ScreenHeight:
            self.Y=-self.Height
        elif self.Y<-self.Height:
            self.Y=self.ScreenHeight
class Ball(Base):
    ball_instances = []
    def __init__(self, id:int=1) -> None:
        super().__init__()
        Ball.ball_instances.append(self)
        self.id = id
        self.size = 15
        self.X = (self.ScreenWidth-self.size)//2
        self.Y = (self.ScreenHeight-self.size)//2
        self.Xspeed = 0
        self.Yspeed = 0
        self.isGame = False
        self.started = False
    @staticmethod    
    def access_player_stuff(index):
        if 0<=index<len(Player.Player_instances):
            return Player.Player_instances[index].X,Player.Player_instances[index].Y,Player.Player_instances[index].Width,Player.Player_instances[index].Height
        else:
            return None
    @staticmethod
    def access_player_instance_number():
        return len(Player.Player_instances) if Player.Player_instances else None


    def resetPoss(self):
        self.X = (self.ScreenWidth-self.size)//2
        self.Y = (self.ScreenHeight-self.size)//2
        self.Xspeed = 0
        self.Yspeed = 0
        self.started = False
    def start(self):
        Base.check(self)
        keys = Base.GetKeys(self)
        if keys[pygame.K_SPACE] and not self.started:#needs a better algorithm so the ball is not 2slow
            self.Xspeed, self.Yspeed = random.choice([-1,1])*random.randint(2,5),random.choice([-1,1])*random.randint(2,5) 
            self.isGame = True
            self.started = True
        if self.isGame:
            self.X += self.Xspeed
            self.Y += self.Yspeed
            if self.X>self.ScreenWidth or self.X<0:
                self.resetPoss()
            if self.Y<=0 or self.Y>=self.ScreenHeight-self.size:
                self.Yspeed=-self.Yspeed
        
        ballObj = pygame.Rect(self.X,self.Y,self.size,self.size)
        for i in range(self.access_player_instance_number()):
            x,y,w,h = self.access_player_stuff(i)
            Pobj = pygame.Rect(x,y,w,h)
            if ballObj.colliderect(Pobj):
                self.Xspeed=-self.Xspeed
    def for_dibug(self):
        a,b,c,d = Ball.access_player_stuff(0)
        print(a,b,c,d)
class Pong(Base):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        self.screen = pygame.display.set_mode(self.ScreenSize)
        self.clock = pygame.time.Clock()
        self.isRunning = True
    def draw(self,x:int,y:int,w:int,h:int,color:Tuple[int,int,int]=(255,155,155)):
        pygame.draw.rect(self.screen,color,(x,y,w,h))
    def updateScreen(self,ScreenColor:Tuple[int,int,int]=(0,0,0)):
        self.screen.fill(ScreenColor)
    def update(self):
        # for i in 
        pygame.display.flip()
        self.clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
    def end(self):
        pygame.quit()
        sys.exit()

