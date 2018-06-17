from defines import *

def mapping(click_pos, start_pos, board_shape, table_shape):
  delta_x, delta_y = calculate_delta(board_shape, table_shape)

  x = int((click_pos[0] - start_pos[0]) / delta_x)
  y = int((click_pos[1] - start_pos[1]) / delta_y)

  return x, y

def calculate_delta(board_shape, table_shape):
  delta_x = int(board_shape[0] / table_shape[0])
  delta_y = int(board_shape[1] / table_shape[1])
  return (delta_x, delta_y)

def is_stone(item):
  return item == RED_STONE or item == BLUE_STONE or item == YELLOW_STONE
  
def is_portal(item):
  return item == RED_PORTAL or item == BLUE_PORTAL or item == YELLOW_PORTAL

def make_2D_array(shape):
  return [[0 for x in range(shape[0])] for y in range(shape[1])]

def portal_to_stone(portal):
  return portal - 1

def stone_to_portal(stone):
  return stone + 1