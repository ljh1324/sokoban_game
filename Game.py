import pygame                   # pygame 모듈을 import
from pygame.locals import *
import os 
import sys
from time import sleep

import utils
#import easy_draw
import file_handle

from defines import *
from Button import *
from Sokoban import *
from InteractiveButton import *
from BoardPainter import *
from Label import *

def game_main():  # 게임 메인화면 입니다.
  screen = pygame.display.set_mode(SCREEN_SHAPE) # 그림을 그릴 수 있는 Surface를 생성 후 반환 합니다. 인자로 Surface크기를 주었습니다.
                                                                    # 그림을 나타낼 수 있는 Surface를 screen에 저장합니다.
  pygame.display.set_caption('Color Sokoban')                       # Window의 타이틀바의 텍스트를 설정합니다.

  start_button = InteractiveButton((104, 300, 120, 40), GREEN, GREEN_ON, RED, 24, 'Start')
  make_map_button = InteractiveButton((296, 300, 120, 40), GREEN, GREEN_ON, RED, 24, 'Make Map')
  title_label = Label((260, 100), RED, 32, 'ColorSokoban')

  while True:
    for event in pygame.event.get(): # Window에서 발생한 이벤트를 버튼 객체에 전달해주고. QUIT, KEYDOWN 이벤트를 처리합니다. 해당 이벤트외에도 다양한 이벤트가 존재합니다.
      if start_button.is_clicked(event):
        game_start()  # 시작 버튼을 클릭하면 게임을 시작합니다.
      elif make_map_button.is_clicked(event):
        game_make()   # 만들기 버튼을 클릭하면 맵을 만듭니다.

      if event.type == pygame.QUIT:  # 닫기 버튼을 눌렀을 경우
        pygame.quit()
        sys.exit()

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE: # ESC 키에 대한 처리
          pygame.quit()
          sys.exit()

    mouse = pygame.mouse.get_pos()       # 마우스의 위치를 받아옵니다.
    start_button.hover_check(mouse)      # 마우스의 위치에 따른 button의 상태를 설정합니다.
    make_map_button.hover_check(mouse)

    screen.fill(WHITE)                   # 화면을 흰색으로 채웁니다.
    title_label.draw(screen)             # 라벨을 screen에 그려줍니다.
    start_button.draw(screen)            # 버튼을 screen에 그려줍니다.
    make_map_button.draw(screen)
    pygame.display.flip()                # 화면을 그리고 나서 화면 전체를 업데이트 합니다. pygame.display.update()를 이용하면 부분적으로 화면을 업데이트 할 수 있습니다.


def game_start():
  filename = game_input()         # game_input()을 통해 filename을 입력받습니다.
  filename = 'maps/' + filename
  
  try:
    board = file_handle.load_board(filename)  # file_handle 모듈의 load_board를 통해 게임판을 불러옵니다.
    sokoban = Sokoban(board)                  # 불러온 게임판으로 Sokoban을 생성합니다.
  except:
    return

  screen = pygame.display.set_mode(SCREEN_SHAPE)

  # 사운드를 위한 파일을 불러옵니다.
  push_effect = pygame.mixer.Sound('resource/Metal_Shuffling.wav')
  walk_effect = pygame.mixer.Sound('resource/Jog_on_concrete.wav')
  win_effect = pygame.mixer.Sound('resource/Battle_Crowd_Celebrate_Stutter.wav')

  board_rect = pygame.Rect(60, 60, 400, 400)
  board_painter = BoardPainter(board_rect, TABLE_SHAPE) # 게임판을 그리기 위한 BoardPainter를 생성합니다.

  move_label = Label((120, 40), BLACK, 24, '')  # 움직임 수를 나타낼 Label을 생성합니다.
  
  move_cnt = 0
  move_kind = NOT_MOVE

  while True:
    for event in pygame.event.get():
      # 이벤트를 처리하는 부분 -> 키보드, 마우스 등의 이벤트 처리 코드가 들어감
      if event.type ==  pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type ==  pygame.KEYDOWN:
        if event.key ==  pygame.K_ESCAPE:
          return
        elif event.key == pygame.K_r:
          move_cnt = 0
          sokoban = Sokoban(board)     # 'r' 키를 눌렀을 경우 게임을 초기화 합니다.
        elif event.key == pygame.K_UP:
          move_kind = sokoban.move(UP)     # 누른 방향키에 따라 Sokoban의 player를 이동시킨 후 이동 종류를 반환합니다.
        elif event.key == pygame.K_DOWN:
          move_kind = sokoban.move(DOWN)
        elif event.key == pygame.K_LEFT:
          move_kind = sokoban.move(LEFT)
        elif event.key == pygame.K_RIGHT:
          move_kind = sokoban.move(RIGHT)

    if move_kind != NOT_MOVE:
      if move_kind == MOVE_WITH_STONE:   # 돌을 움직이면서 이동했을 경우 push_effect음악을 0.5초간 들려줍니다.
        push_effect.play(maxtime=500)
      elif move_kind == MOVE:            # 일반 움직임일 경우 walk_effect음악을 0.5초간 들려줍니다.
        walk_effect.play(maxtime=500)
      move_kind = NOT_MOVE
      move_cnt += 1  # 움직임 횟수를 1증가 시킵니다.

    game_map = sokoban.get_game_map()         # 이벤트를 처리 후 업데이트된 게임맵을 받아옵니다.
    portal_list = sokoban.get_portal_list()   # sokoban의 포탈 위치를 받아옵니다.

    
    #easy_draw.draw_map_and_portal(screen, boardRect, game_map, portal_list)

    screen.fill(WHITE)

    board_painter.draw_board(screen, game_map)           # 게임맵을 그립니다.
    board_painter.draw_portal(screen, portal_list)       # 포탈을 그립니다.

    move_label.set_text('Move: {0}'.format(move_cnt))    # Label에 기록된 움직임 횟수를 수정합니다.
    move_label.draw(screen)                              # Label을 screen에 그려줍니다.
    pygame.display.flip()                                # 화면 전체를 업데이트 합니다.

    if sokoban.is_win():  # 모든 돌이 적절한 포탈에 위치했을 경우 "Win" Label을 보여준 후 메인 화면으로 돌아갑니다.
      win_label = Label((260, 260), BLACK, 32, 'Win!')
      win_label.draw(screen)
      win_effect.play(maxtime=2500)
      #easy_draw.draw_text(screen, 'Win!!', (260, 260), BLACK, 32)
      pygame.display.flip()
      sleep(1)
      return
  


def game_make():
  screen = pygame.display.set_mode(SCREEN_SHAPE)
  pygame.display.set_caption('Color Sokoban')  # 타이틀바의 텍스트를 설정
  tool = 0

  # 게임판을 저장, 불러오기할 수 있는 버튼과 게임판을 만드는데 필요한 도구를 선택할 수 있는 버튼을 생성합니다.
  save_button = Button((10, 10, 40, 30), WHITE, BLACK, 16, 'Save')
  load_button = Button((50, 10, 40, 30), WHITE, BLACK, 16, 'Load')
  red_button = Button((100, 10, 60, 30), WHITE, RED, 16, 'RedStone')
  blue_button = Button((170, 10, 60, 30), WHITE, BLUE, 16, 'BlueStone')
  yellow_button = Button((240, 10, 60, 30), WHITE, YELLOW, 16, 'YellowStone')
  brick_button = Button((310, 10, 60, 30), WHITE, BROWN, 16, 'Brick')
  player_button = Button((380, 10, 60, 30), WHITE, PINK, 16, 'Player')
  erase_button = Button((450, 10, 40, 30), WHITE, GRAY, 16, 'Erase')

  button_list = [red_button, blue_button, yellow_button, brick_button, player_button, erase_button]
  tools = [RED_STONE, BLUE_STONE, YELLOW_STONE, BRICK, PLAYER, EMPTY]  # 각 버튼에 맞는 도구를 지정합니다.
  
  screen.fill(WHITE)
  for button in button_list:
    button.draw(screen)
  save_button.draw(screen)
  load_button.draw(screen)

  board = utils.make_2D_array(TABLE_SHAPE)

  board_rect = pygame.Rect(60, 60, 400, 400)             # 게임판의 위치를 설정합니다.
  board_painter = BoardPainter(board_rect, TABLE_SHAPE)  # 게임판을 그리기 위한 BoardPainter를 생성합니다.

  done = False
  while not done:
    for event in pygame.event.get():

      for i in range(len(button_list)):
        if button_list[i].is_clicked(event):
          tool = tools[i]  # i번째 버튼이 눌렀을 경우 도구를 i번째 도구로 설정합니다.

      if save_button.is_clicked(event):  # save button을 눌렀을 경우
        filename = game_input()  # filename을 입력받습니다.
        filename = 'maps/' + filename
        try:
          file_handle.save_board(filename, board)  # 게임판을 filename에 저장합니다.
          return
        except:
          pass

      elif load_button.is_clicked(event):  # load button을 눌렀을 경우
        filename = game_input()  # filename을 입력받습니다.
        filename = 'maps/' + filename
        try:
          board = file_handle.load_board(filename)  # file_handle 모듈의 load_board를 통해 게임판을 불러옵니다.
          screen.fill(WHITE)          # 화면을 초기화 해줍니다.
          for button in button_list:
            button.draw(screen)
          save_button.draw(screen)
          load_button.draw(screen)
        except:
          board = utils.make_2D_array(TABLE_SHAPE)  # 불러오기를 실패했을 경우 TABLE_SHAPE형태로 비어있는 2차원 배열을 만들어줍니다.

      if event.type ==  pygame.QUIT:
        pygame.quit()
        sys.exit()

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          done = True

      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if board_rect.collidepoint(mouse):  # mouse가 게임판을 클릭했을 경우
          x, y = utils.mapping(mouse, (board_rect[0], board_rect[1]), (board_rect[2], board_rect[3]), TABLE_SHAPE)  # 클릭한 부분을 TABLE_SHAPE크기에 맞도록 변환한다. 
          board[y][x] = tool  # board[y][x]에 tool값을 넣어준다.

          if utils.is_stone(tool):  # tool이 stone일 경우 portal로 변환시킨다.
            tool += 1
          elif utils.is_portal(tool): # tool이 portal일 경우 stone으로 변환시킨다.
            tool -= 1
    
    board_painter.draw_board(screen, board)

    pygame.display.flip()
  
  return


def game_input():
  screen = pygame.display.set_mode(SCREEN_SHAPE)
  font = pygame.font.Font(None, 32)

  text = ''

  info_label = Label((260, 220), YELLOW, 32, 'File Name')
  filename_label = Label((260, 240), YELLOW, 32, ': ')

  done = False
  while not done:
    for event in pygame.event.get():
      if event.type ==  pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RETURN:
          done = True  # 엔터키를 눌렀을 경우 done을 True로 바꿔 while문을 종료시킵니다.
        elif event.key == pygame.K_BACKSPACE:
          text = text[:-1]  # 백스페이스키를 눌렀을 경우 text를 한 칸 줄입니다.
          filename_label.set_text(': ' + text)  # Label을 업데이트 합니다.
        elif event.key == pygame.K_ESCAPE:
          text = ''
          done = True
        else:
          text += event.unicode  # 엔터키, 백스페이스키, ESC키가 아닌 경우 text에 입력받은 값을 추가합니다.
          filename_label.set_text(': ' + text)  # Label을 업데이트 합니다.
    screen.fill((30, 30, 30))
    info_label.draw(screen)
    filename_label.draw(screen)
    pygame.display.flip()

  return text


if __name__ == '__main__':
  pygame.init() # now use display and fonts
  game_main()