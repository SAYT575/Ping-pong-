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
