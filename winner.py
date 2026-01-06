def winner(board,player):
  condition=((board[6] == board[7] == board[8]==player) or # across the top
    (board[3] == board[4] == board[5]==player) or # across the middle
    (board[0] == board[1] == board[2]==player) or # across the bottom
    (board[6] == board[3] == board[0]==player) or # down the middle
    (board[7] == board[4] == board[1]==player) or # down the middle
    (board[8] == board[5] == board[2]==player) or # down the right side
    (board[6] == board[4] == board[2]==player) or # diagonal
    (board[8] == board[4] == board[0]==player)) # diagonal
  if condition and player!=" ":
    print(f"{player} wins")
    return (f"{player} wins")
  