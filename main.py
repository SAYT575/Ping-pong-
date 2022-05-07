from pygame import *

class GameSprite(sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed, width, height):
    super().__init__()
    self.image = transform.scale(image.load(player_image))
    self.speed = player_speed
    sefl.rect = self.image.get_rect()
    self.rect.x = player_x 
    self.rect.y = player_y
  def reset(self):
    window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def update_r(self):
      keys = key.get_pressed()
      if keys[K_UP] and self.rect.y > 5:
        self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect < 420:
        self.rect.y += self.speed
      def update_l(self):
        pass
      
     win_width = 600
     win_height = 500

      
back = (200,255,255)
win_width, win_height = 600, 500
window = display.set_mode((win_width, win_height))
window.fill(back)
raket1 = Player("racket.png", 30, 200, 4, 50)
raket2 = Player("racket.png", 30, 200, 4, 50)

ball = GameSprite("ball.png", 200,200,4,50,50)
font.init()
font = font.Font(None,35)
lose1 = font.render("Player 1 lose!", True, (180,0,0))
lose2 = font.render("Player 2 lose!", True, (180,0,0))
speed_x = 3
speed_y = 3

while game:
  for e in event.get():
    if e.type == QUIT:
  if finish != True:
      window.fill(back)
      racket1.update_l()
      recket2.update_r()
      ball.rect.x += speed_x
      ball.rect.y += speed_y
      if sprite.collide_rect(racket1, ball) or sprite.collide_rect(raket, ball):
        speed_x *= -1
        speed_y *= -1
      if ball.rect.x > win_height - 50 or ball.rect.y:
        speed_y *= -1 
      if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
        game = False 
      if ball.rect.x > win_width - 50 or ball.rect.x:
        finish = True 
        window.blit(lose2, (200,200))
      racket1.reset()
      raket2.reset()
      ball.reset()
      
    display.update()
    clock.tick(FPS)
      
        
