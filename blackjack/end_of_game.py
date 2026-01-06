
def player_busts(player,dealer,chips):
    print("player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player win!")
    chips.win_bet()

def dealer_busts(plyaer,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
    
    