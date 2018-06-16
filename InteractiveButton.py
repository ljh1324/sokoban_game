import pygame
import utils

class InteractiveButton:
  def __init__(self, rect, normal_color, hover_color, font_color, font_size, text):
    self.__rect = pygame.Rect(rect)  # (left, top, width, hegiht)를 통해 pygame에서 제공하는 Rect객체를 생성합니다. Rect객체를 이용하여 마우스와의 충돌을 감지할 수 있습니다.
    self.__normal_color = normal_color
    self.__hover_color = hover_color
    self.__text = text
    self.__flag = False
    
    font = pygame.font.Font(None, font_size)  # 새로운 폰트 객체를 만듭니다. None에 폰트 파일을 지정할 수 있습니다.
    self.__txt_surface = font.render(text, True, font_color)  # 정해진 폰트를 가지는 글자를 새로운 Surface에 그립니다. Surface는 이미지를 나타내는 클래스입니다.
    # self.__txt_surface = self.font.render(text, True, self.fontColor)

  def is_clicked(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:   # 마우스가 버튼을 클릭할 경우 True를 반환합니다.
      if self.__rect.collidepoint(event.pos):  # event가 발생한 위치(여기서는 마우스 위치)가 rect안에 있는지 확인합니다.
        return True
      else:
        return False

  def hover_check(self, mouse):  # 마우스가 Button안에 들어와있으면 flag를 True로, 버튼 밖으로 나갈 경우 flag를 False로 바꾸는 메소드를 만들었습니다.
    if self.__rect.collidepoint(mouse):
      self.__flag = True
    else:
      self.__flag = False

  def draw(self, screen):
    # Blit the text.
    if self.__flag == True:   # flag에 따라 색깔을 다르게 하여 screen에 그립니다.
      pygame.draw.rect(screen, self.__hover_color, self.__rect)
    else:
      pygame.draw.rect(screen, self.__normal_color, self.__rect)

    text_rect = self.__txt_surface.get_rect()                             # 텍스트 객체의 출력 위치를 가져온다
    center_x, center_y = utils.middle_of_rect(self.__rect)                # 사각형의 중심 좌표를 계산합니다.
    text_rect.center = (center_x, center_y)                               # 텍스트 객체의 출력 중심 좌표를 설정한다

    screen.blit(self.__txt_surface, text_rect)                            # screen(Surface객체)에 text_rect위치에 txt_surface를 그려줍니다.