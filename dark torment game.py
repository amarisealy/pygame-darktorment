
#ISSA
#Ryan Wong, Aakar Panth, Amari Sealy
#Dark Torment
#


from gamelib import*

game = Game(1422,800,"Dark Torment")
bk = Image("image\\bk.png",game)
game.setBackground(bk)
ammobox = Image("image\\ammo box.png",game)
ammobox.moveTo(550,730)
ammobox.resizeBy(-30)
bandage = Image("image\\bandage.png",game)
bandage.resbandage.moveTo(70,730)
shield = Image("image\\shield.png",game)
shield.resizeBy(-60)
shield.moveTo(100,650)
man = Image("image\\man.png",game)
man.moveTo(200,670)
man.resizeBy(-40)
title = Image("image\\start.png",game) 
title.moveTo(750,600)
title.resizeBy(-20)
bk2= Image("image\\jungle.png",game)
zombies = Image("image\\zombies.png",game)
howtoplay = Image("image\\howtoplay.png",game)
howtoplay.moveTo(200,700)
boss1 = Image("image\\boss1.png",game)
boss2 = Image("image\\boss2.png",game)
gun = Sound("image\\gun.wav",1)

zombies = []
for index in range(10):
    zombies.append(Animation("image\\zombies.png",1,game,1000,1407))
for index in range(10):
    x = randint(1000,1900)
    y = randint(670,670)
    zombies[index].moveTo(x,y)
    zombies[index].setSpeed(-1,-90)
    zombies[index].resizeBy(-80)
ammo = []
for index in range(1):
    ammo.append(Animation("image\\ammo.png",game))
for index in range(1):
    x = randint(100,730)
    y = randint(600,700)
    ammo[index].moveTo(x,y)
    if (K_SPACE).collidedWith(mouse):
        ammo[index].setSpeed(3,90)
    ammo[index].resizeBy(-20)
                
    
    

while not game.over:
    game.processInput()
    bk.draw()
    title.draw()
    howtoplay.draw()
    if howtoplay.collidedWith(mouse) and mouse.LeftClick:
        game.drawText("Your objective of the game is for the man to save his son. Control the man with the left and right arrow keys on the keyboard. You'll have to fight throught and survive two waves of enemies in order to win the game and save the man's son. Failing to survive both waves will result in the man's death and the game will be over. 
    if title.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

        
    game.update(60)

game.over = False

#Level 1
while not game.over:
    game.processInput()
    game.scrollBackground("left",2)
    bk2.draw()
    man.draw()
    shield.draw()
    ammobox.draw()
                      bandage.draw()
    game.drawText("Ammo: " + str(ammo),bk2.x-300,bk2.y-390)
    game.drawText("Health: " + str(man.health),bk2.x-700,bk2.y-390)
    for index in range(10):
        zombies[index].move()
        if zombies[index].collidedWith(man):
            man.health -= 5
        if man.health <1:
            game.over = True
        if man.collidedWith(ammobox):
            ammo += 30
        if man.collidedWith(bandage):
            man.health += 15
        if man.collidedWith(bandage) and man.health >99:
            man.health += 0


    if keys.Pressed[K_RIGHT]:
        man.x += 4
    if keys.Pressed[K_LEFT]:
        man.x -= 4
    gun.play(K_SPACE)
    

    game.update(60)
game.quit()
