import gameenvai

myGame = gameenvai.Pong()

p1 = gameenvai.Player(1)
p3 = gameenvai.Player(3)
p2 = gameenvai.Player(2)

ball = gameenvai.Ball(1)
ball2 = gameenvai.Ball(2)
ball3 = gameenvai.Ball(3)

while myGame.isRunning:
    myGame.updateScreen()
    myGame.check()
    p1.Play()
    p2.Play('Unbeatable')
    p3.Play('Unbeatable')
    ball.start()
    ball2.start()
    ball3.start()
    
    myGame.update()
myGame.end()
