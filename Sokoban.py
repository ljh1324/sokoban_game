import utils
from defines import *

class Sokoban:
  def __init__(self, board):
    self.__shape = (len(board[0]), len(board))
    self.__player_x = -1
    self.__player_y = -1
    self.__game_map = utils.make_2D_array(self.__shape)
    self.__portal_list = []
    self.__dx = [0, 0, -1, 1]
    self.__dy = [-1, 1, 0, 0]

    for y in range(self.__shape[1]):
      for x in range(self.__shape[0]):
        if board[y][x] == PLAYER:
          self.__player_x = x
          self.__player_y = y
          self.__game_map[y][x] = board[y][x]
        elif utils.is_portal(board[y][x]):
          self.__portal_list.append((x, y, board[y][x]))
        else:
          self.__game_map[y][x] = board[y][x]
  
  def in_range(self, x, y):
    return 0 <= x < self.__shape[0] and 0 <= y < self.__shape[1]

  def can_move(self, dir):
    next_x = self.__player_x + self.__dx[dir]
    next_y = self.__player_y + self.__dy[dir]

    if not self.in_range(next_x, next_y):
      return False
    
    if self.__game_map[next_y][next_x] == BRICK:
      return False

    elif self.__game_map[next_y][next_x] == EMPTY:
      return True
    
    if utils.is_stone(self.__game_map[next_y][next_x]):
      next_x = next_x + self.__dx[dir]
      next_y = next_y + self.__dy[dir]
      if not self.in_range(next_x, next_y):
        return False
      if self.__game_map[next_y][next_x] == 0:
        return True
      else:
        return False

  def move(self, dir):
    if self.can_move(dir) == False:
      return NOT_MOVE
    #print("뀨")
    next_x = self.__player_x + self.__dx[dir]
    next_y = self.__player_y + self.__dy[dir]
    self.__game_map[self.__player_y][self.__player_x] = 0

    move = MOVE
    if utils.is_stone(self.__game_map[next_y][next_x]):
      rockX = next_x + self.__dx[dir]
      rockY = next_y + self.__dy[dir]
      self.__game_map[rockY][rockX] = self.__game_map[next_y][next_x]
      move = MOVE_WITH_STONE

    self.__game_map[next_y][next_x] = PLAYER
    self.__player_x += self.__dx[dir]
    self.__player_y += self.__dy[dir]
    return move

  def is_win(self):
    for portal in self.__portal_list:
      x = portal[0]
      y = portal[1]
      want = utils.portal_to_stone(portal[2])
      
      if self.__game_map[y][x] != want:
        return False
    return True

  def get_game_map(self):
    return self.__game_map
 
  def get_portal_list(self):
    return self.__portal_list


    
    
      
      

    
        
  