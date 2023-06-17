from pygame import *

class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      sprite.Sprite.__init__(self)
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y

  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed 
    def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed      
    
platform_left = Player("racket.png",30,250,40,100,15)
platform_right = Player("racket.png",520,250,40,100,15)
tennis_ball = GameSprite("tenis_ball.png",200,200,50,50,20)

font.init()
font1 = font.Font(None,36)
player1win = font1.render("PLAYER 1 WIN!",True,(190,0,0))
player2win = font1.render("PLAYER 2 WIN!",True,(190,0,0))

win_width = 600
win_height = 500

window = display.set_mode((win_width,win_height))
back = (200,250,250)

game = True
finish = False


clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:
        window.fill(back)
        platform_left.reset()
        platform_right.reset()
        tennis_ball.reset() 
        platform_left.update_l()
        platform_right.update_r()
        tennis_ball.rect.x += speed_x
        tennis_ball.rect.y += speed_y
    if tennis_ball.rect.y > win_height-50 or tennis_ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(platform_left,tennis_ball) or sprite.collide_rect(platform_right,tennis_ball):
        speed_x *= -1
        speed_y *= 1
    if tennis_ball.rect.x > win_width:
        finish = True
        window.blit(player1win,(200,200))
    if tennis_ball.rect.x < 0:
        finish = True
        window.blit(player2win,(200,200))










    display.update()
    clock.tick(FPS)
        