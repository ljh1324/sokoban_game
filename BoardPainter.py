import pygame
import utils
from defines import *

class BoardPainter:
  def __init__(self, board_rect, table_shape):
    self.__canvas_x = board_rect[0]
    self.__canvas_y = board_rect[1]
    self.__canvas_width = board_rect[2]
    self.__canvas_height = board_rect[3]
    self.__table_width = table_shape[0]
    self.__table_height = table_shape[1]
    self.__delta_x = int(self.__canvas_width / self.__table_width)
    self.__delta_y = int(self.__canvas_height / self.__table_height)
    self.__TOOL_COLOR = {}
    self.__TOOL_COLOR[RED_PORTAL] = RED
    self.__TOOL_COLOR[BLUE_PORTAL] = BLUE
    self.__TOOL_COLOR[YELLOW_PORTAL] = YELLOW
    self.__TOOL_COLOR[RED_STONE] = RED
    self.__TOOL_COLOR[BLUE_STONE] = BLUE
    self.__TOOL_COLOR[YELLOW_STONE] = YELLOW
    self.load_image_file()

  def load_image_file(self):  # 게임판을 그리는데 필요한 이미지 파일을 모두 불러옵니다.
    TILE_IMAGE = pygame.image.load('resource/tile.png')
    self.__TILE_IMAGE = pygame.transform.scale(TILE_IMAGE, (self.__delta_x, self.__delta_y))

    BRICK_IMAGE = pygame.image.load('resource/brick.png')
    self.__BRICK_IMAGE = pygame.transform.scale(BRICK_IMAGE, (self.__delta_x, self.__delta_y))

    PLAYER_IMAGE = pygame.image.load('resource/player.png')
    self.__PLAYER_IMAGE = pygame.transform.scale(PLAYER_IMAGE, (self.__delta_x, self.__delta_y))

    RED_STONE_IMAGE = pygame.image.load('resource/red.png')
    self.__RED_STONE_IMAGE = pygame.transform.scale(RED_STONE_IMAGE, (self.__delta_x, self.__delta_y))

    BLUE_STONE_IMAGE = pygame.image.load('resource/blue.png')
    self.__BLUE_STONE_IMAGE = pygame.transform.scale(BLUE_STONE_IMAGE, (self.__delta_x, self.__delta_y))

    YELLOW_STONE_IMAGE = pygame.image.load('resource/yellow.png')
    self.__YELLOW_STONE_IMAGE = pygame.transform.scale(YELLOW_STONE_IMAGE, (self.__delta_x, self.__delta_y))

  def draw_board(self, screen, board):  # 게임판을 그려줍니다.
    for i in range(self.__table_height):   # screen의 canvas가 나타내는 부분을 TILE_IMAGE로 덮어줍니다.
      for j in range(self.__table_width): 
        # screen(Surface 객체)위에 x좌표 canvas_x + delta_x * j, y좌표 canvas_y + delta * i 위치에 이미지를 delta_x * delta_y 크기만큼 그려줍니다.
        screen.blit(self.__TILE_IMAGE, (self.__canvas_x + self.__delta_x * j, self.__canvas_y + self.__delta_y * i, self.__delta_x, self.__delta_y))

    for i in range(self.__table_height):
      for j in range(self.__table_width):  # board[i][j]의 값에 따라 screen에 이미지를 그려줍니다.
        if board[i][j] == BRICK:
          screen.blit(self.__BRICK_IMAGE, (self.__canvas_x + self.__delta_x * j, self.__canvas_y + self.__delta_y * i, self.__delta_x, self.__delta_y))
        elif board[i][j] == RED_STONE:
          screen.blit(self.__RED_STONE_IMAGE, (self.__canvas_x + self.__delta_x * j, self.__canvas_y + self.__delta_y * i, self.__delta_x, self.__delta_y))
        elif board[i][j] == BLUE_STONE:
          screen.blit(self.__BLUE_STONE_IMAGE, (self.__canvas_x + self.__delta_x * j, self.__canvas_y + self.__delta_y * i, self.__delta_x, self.__delta_y))
        elif board[i][j] == YELLOW_STONE:
          screen.blit(self.__YELLOW_STONE_IMAGE, (self.__canvas_x + self.__delta_x * j, self.__canvas_y + self.__delta_y * i, self.__delta_x, self.__delta_y))
        elif board[i][j] == PLAYER:
          screen.blit(self.__PLAYER_IMAGE, (self.__canvas_x + self.__delta_x * j, self.__canvas_y + self.__delta_y * i, self.__delta_x, self.__delta_y))
        elif utils.is_portal(board[i][j]):  # portal일 경우 portal 위치에 원을 그려줍니다. 
          color = self.__TOOL_COLOR[board[i][j]]
          pygame.draw.ellipse(screen, color, (self.__canvas_x + self.__delta_x * j, self.__canvas_y + self.__delta_y * i, self.__delta_x, self.__delta_y), 3)
    

  def draw_portal(self, screen, portal_list):  # 포탈을 그려줍니다.
    for portal in portal_list:
      x = portal[0] # portal_list의 portal의 x, y좌표를 변수에 저장합니다.
      y = portal[1]
      want = portal[2]
      color = self.__TOOL_COLOR[want]
      pygame.draw.ellipse(screen, color, (self.__canvas_x + self.__delta_x * x, self.__canvas_y + self.__delta_y * y, self.__delta_x, self.__delta_y), 3)


  


