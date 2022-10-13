
board = list(range(1, 10))
def dashboard(board):
   a = "-" * 13
   for i in range(3):
      a+= "\n| "
      a+= str(board[0+i*3])
      a+= " | "
      a+= str(board[1+i*3])
      a+= " | "
      a+= str(board[2+i*3])
      a+= " |\n"
      a+="-" * 13
   return a
print(dashboard(board))
