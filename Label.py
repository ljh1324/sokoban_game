import pygame
import utils

class Label:
  def __init__(self, center_pos, font_color, font_size, text):
    self.__center_x = center_pos[0]
    self.__center_y = center_pos[1]

    self.__text = text
    self.__font_color = font_color
    self.__font = pygame.font.Font(None, font_size)  # 새로운 폰트 객체를 만듭니다. 인자로 폰트 파일, 폰트 크기를 줄 수 있습니다. None을 줄 경우 폰트를 설정하지 않습니다.


  def draw(self, screen):
    # Blit the text.
    txt_surface = self.__font.render(self.__text, True, self.__font_color)  # 정해진 폰트를 가지는 글자를 새로운 Surface에 그립니다. Surface는 이미지를 나타내는 클래스입니다.
    text_rect = txt_surface.get_rect()                                      # 텍스트 객체의 출력 위치를 가져온다
    text_rect.center = (self.__center_x, self.__center_y)                   # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(txt_surface, text_rect)                                     # screen(Surface객체)에 text_rect위치에 txt_surface를 그려줍니다.

  def set_text(self, text):
    self.__text = text                  # text를 설정합니다.

