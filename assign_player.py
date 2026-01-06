board=[" "," "," "," "," "," "," "," "," "]
choice=["X","O"]
def get_user():
  player1=input("Player 1 choose X or O: ")
  if player1 in choice:
    player2=[i for i in choice if i!=player1][0]
    return (player1,player2)
  else:
    print("invalid input")
    return get_user()
