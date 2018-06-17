from defines import TABLE_SHAPE
import utils

def load_board(filename):
  f = open(filename, 'r')

  width, height = TABLE_SHAPE

  line = f.readline()
  items = line.split()

  board = utils.make_2D_array((width, height))
    
  idx = 0
  for i in range(height):
    for j in range(width):
      board[i][j] = int(items[idx])
      idx += 1
    
  f.close()
  return board

def save_board(filename, board):
  f = open(filename, 'w')
    
  width, height = TABLE_SHAPE
    
  for i in range(height):
    for j in range(width):
      f.write('{0} '.format(board[i][j]))

  f.write('\n')
  f.close()
