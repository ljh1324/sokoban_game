def load_board(filename):
    f = open(filename, 'r')
    shape = f.readline()

    items = shape.split()
    width  = int(items[0])
    height = int(items[1])

    board = [[0 for x in range(width)] for y in range(height)]

    for i in range(height):
        line = f.readline()
        items = line.split()
        for j in range(width):
            board[i][j] = int(items[j])
    
    f.close()
    return board

def save_board(filename, board):
    f = open(filename, 'w')
    
    width = len(board[0])
    height = len(board)
    f.write('{0} {1}\n'.format(width, height))
    for i in range(height):
        for j in range(width):
            f.write('{0} '.format(board[i][j]))
        f.write('\n')

    f.close()
