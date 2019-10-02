from random import randint


def deal_card( deck ):
    card_int = randint(0, len( deck ) -1 )
    card = deck.pop(card_int)
    return card


def add_card_to_total( current, card ):
    ans = 0
    if card =='A':
        ans = current + 11
        if ans > 21:
            ans -= 10
    elif card in [ 'J', 'Q', 'K' ]:
        ans = current + 10
    else:
        ans = current + int( card )
    return ans


def has_won( player, dealer ):
    if player > 21:
        return False
    elif player > dealer or dealer > 21:
        return True
    else:
        return False


def deal_first_hand( deck ):
    player = []
    dealer = []
    for i in range(4):
        if i%2 == 0:
            player.append( deal_card( deck ) )
        else:
            dealer.append( deal_card( deck ) )
    return player, dealer


def sum_hand( hand ):
    init = 0
    for i in range( len( hand ) ):
        init = add_card_to_total( init, hand[i] )
    return init


cards = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]
stack = cards.copy()*4


#main
hands = deal_first_hand( stack )
player_hand = hands[0]
dealer_hand = hands[1]
print( f'Dealers cards are {dealer_hand[0]} and ?' )
while True:
    print( f'Your score is: {sum_hand(player_hand)}' )
    if sum_hand(player_hand) > 21:
        break
    promt = input( 'Do you want another card? (J/N) ' )
    if promt is 'J':
        player_hand.append( deal_card( stack ) )
    else:
        break
player_sum = sum_hand( player_hand )
dealer_sum = sum_hand( dealer_hand )
print( f'Dealers score is: {dealer_sum}' )
if has_won( player_sum, dealer_sum ):
    print( 'You won!' )
else:
    print( 'You lost' )
