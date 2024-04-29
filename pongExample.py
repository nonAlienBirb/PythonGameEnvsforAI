import gameenvai


myGame = gameenvai.Pong()
p1 = gameenvai.Player(1)
p2 = gameenvai.Player(2)
ball = gameenvai.Ball(1)
ball2 = gameenvai.Ball(2)
while myGame.isRunning:
    myGame.updateScreen() 
    myGame.check()
    p1.Play('Human')
    p2.Play('Unbeatable')
    ball.start()
    ball2.start()
    myGame.draw(ball2.X,ball2.Y,ball2.size,ball2.size)
    myGame.draw(ball.X,ball.Y,ball.size,ball.size)
    myGame.draw(p1.X,p1.Y,p1.Width,p1.Height)
    myGame.draw(p2.X,p2.Y,p2.Width,p2.Height)
    myGame.update()
myGame.end()
