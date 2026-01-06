from blackjack import Card,suits,ranks,values,Chips,take_bet,deck,Hand,player_busts,player_wins,dealer_busts,dealer_wins,push,hit,hit_or_stand,show_all,show_some
playing=True
while True:
    
    print('Welcome to BlackJack! Play and win !')
    

    mydeck = deck()
    mydeck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(mydeck.deal_one())
    player_hand.add_card(mydeck.deal_one())
    
    dealer_hand = Hand()
    dealer_hand.add_card(mydeck.deal_one())
    dealer_hand.add_card(mydeck.deal_one())
            
    player_chips = Chips()     
    
    
    take_bet(player_chips)
    

    show_some(player_hand,dealer_hand)
    
    while playing:  
        
        
        hit_or_stand(mydeck,player_hand) 
        
    
        show_some(player_hand,dealer_hand)  
        
    
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(mydeck,dealer_hand)    
    
    
        show_all(player_hand,dealer_hand)
        
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

    
    
    