import pygame

class Button:
  def __init__(self, rect, back_color, font_color, font_size, text):
    self.__rect = pygame.Rect(rect)  # (left, top, width, hegiht)를 통해 pygame에서 제공하는 Rect객체를 생성합니다. Rect객체를 이용하여 마우스와의 충돌을 감지할 수 있습니다.
    #self.__font_color = font_color
    self.__back_color = back_color
    #self.__font = pygame.font.Font(None, font_size)
    self.__text = text

    font = pygame.font.Font(None, font_size)
    #self.__txt_surface = self.font.render(text, True, self.__font_color)
    self.__txt_surface = font.render(text, True, font_color)

  def is_clicked(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:   # 마우스가 버튼을 클릭할 경우 True를 반환합니다.
      if self.__rect.collidepoint(event.pos):  # event가 발생한 위치(여기서는 마우스 위치)가 rect안에 있는지 확인합니다.
        return True
      else:
        return False

  def draw(self, screen):
    # Blit the text.
    pygame.draw.rect(screen, self.__back_color, self.__rect)
    text_rect = self.__txt_surface.get_rect()                            # 텍스트 객체의 출력 위치를 가져온다
    center_x, center_y = self.__rect.center
    text_rect.center = (center_x, center_y)                              # 텍스트 객체의 출력 중심 좌표를 설정한다
    
    screen.blit(self.__txt_surface, text_rect)                           # screen(Surface객체)에 text_rect위치에 txt_surface를 그려줍니다.