import pygame as pg
import sys
import time
import random
pg.init()

width=600
height=600

win=pg.display.set_mode((width,height))
bg_img = pg.image.load('bg.jpg')
bg_img = pg.transform.scale(bg_img,(width,height))
i=0


clock=pg.time.Clock()
box=pg.rect.Rect((width/2-50,height-20,100,10))
ball=pg.Vector2((box.x+50,height-30))
ball_speed=pg.Vector2((10,10))

font=pg.font.Font("arial.ttf",24)
label_text=font.render("Score: 0",(0,0,0),(255,0,0))
label_rect=label_text.get_rect()
label_rect.center=(80,10)


font2=pg.font.Font("arial.ttf",65)
over_text=font2.render("Game Over",(0,0,0),(0,0,0))
over_rect=over_text.get_rect()
over_rect.center=(300,300)

speed=12
target_fps=60
last_time=time.time()
dt=0
game_started=False
game_lost=False
game_score=0

def gameOver():
    win.blit(over_text,over_rect)
    pg.display.update()
    

def checkBallCollision(ball):
    global game_lost,game_score,label_text
    if ball.y<=0:
        ball_speed.y=-ball_speed.y
    if ball.x<=0 or ball.x>=width:
        ball_speed.x=-ball_speed.x
    if (ball.x>=box.x and ball.x<=box.x+100) and (ball.y>box.y-10):
       ball_speed.y=-ball_speed.y
       if game_started==True:
           game_score+=1
           label_text=font.render(f"Score: {game_score}",(255,255,255),(255,255,255))
    if ball.y+10>=height:
        game_lost=True
        gameOver()



while True:
    if game_lost==True:
      pg.time.delay(5000)
    new_time=time.time()
    dt=new_time-last_time
    last_time=new_time

    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE and game_started==False:
                game_started=True
                ball_speed.y=ball_speed.y
                flag=random.randint(0,1)
                randd_speed=random.randint(5,10)
                if flag==0:
                    ball_speed.x=-ball_speed.x
                

    keys=pg.key.get_pressed()

    
    if keys[pg.K_RIGHT]:
        if box.x+100<width:
            box.x+=speed*dt*target_fps
      
    if keys[pg.K_LEFT]:
        if box.x>0:
            box.x-=speed*dt*target_fps
    if game_started==False:
        ball.x=box.x+50
    else:
        ball.y-=ball_speed.y *dt*target_fps
        ball.x+=ball_speed.x*dt*target_fps
    
    
        
    
    win.fill((0,0,0)) 
    
    win.blit(bg_img,(i,0))
    win.blit(bg_img,(width+i,0))
    if (i==-width):
        win.blit(bg_img,(width+i,0))
        i=0
    i-=1
    pg.draw.circle(win,(0,0,0),ball,10)
    pg.draw.rect(win,(255,255,255),box)
    win.blit(label_text,label_rect)
    checkBallCollision(ball)
    
    pg.display.update()
    clock.tick(60)

