#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
#     <li><a href="Lokale%20variabler.ipynb">Lokale variabler</a></li>
#     <li><a href="Globale%20variabler.ipynb">Globale variabler</a></li>
#     <li><a href="Euklids%20algoritme.ipynb">Euklids algoritme</a></li>
#     <li><a href="Primtall.ipynb">Primtall</a></li>
#     <li><a href="Multiplikasjon.ipynb">Multiplikasjon</a></li>
#         <li><a href="Den%20store%20sporreundersokelsen.ipynb">Den store spørreundersøkelsen</a></li>
#     <li><a href="Arbeidsdager.ipynb">Arbeidsdager</a></li>
#     <li><a href="Sekantmetoden.ipynb">Sekantmetoden</a></li>
#     <li class="active"><a href="Not%20quite%20Blackjack.ipynb">Not quite Blackjack</a></li>
#         <li><a href="Funksjoner%20og%20Jupyter%20widgets.ipynb">Funksjoner og Jupyter widgets</a></li>
#     </ul>
#   </div>
# </nav>
# 
# 
# # Not quite Blackjack
# 
# **Læringsmål:**
# - Funksjoner
# - Betingelser
# - Løkker
# 
# **Starting Out with Python:**
# - Kap. 3: Decision Structures and Boolean Logic 
# - Kap. 4.2: The while Loop
# - Kap. 5: Functions
# 
# I denne oppgaven skal du lage spillet Blackjack med en vri. Vanlige Blackjack reglene som skal implementeres er som følger:
# 
# - Et ess teller enten 1 eller 11
# - Alle bildekort (J, Q, K) har verdi 10
# - Du får alltid utdelt to kort til å begynne med
# - Hvis den samlede verdien på kortene er over 21 er du ute
# - Et ess med 10 eller et bildekort er en «ekte» blackjack
# - Du vinner på én av tre måter:
#   - Du får ekte blackjack uten at dealer gjør det samme,
#   - Du oppnår en høyere hånd enn dealer uten å overstige 21, eller
#   - Din hånd har verdi mindre enn 21, mens dealerens hånd overstiger 21
# 
# Det som er annerledes med vår Blackjack, er at dealer bare får to kort, og at spilleren ikke får velge verdien ess vil ha. Spillet vil automatisk ta den verdien som er nærmest 21, men som ikke overstiger 21, og så fort en verdi for ess er satt, vil ikke denne endres senere. Dvs. at om man først får 1 (ess) og 8, vil verdien bli satt til 11+8=19. Om man deretter velger å trekke enda et kort og får 4, vil verdien bli 19+4=23, og man vil tape. Det blir altså ikke tatt hensyn til at 1+8+4<21. Om man derimot først fikk 4 og 8, og deretter fikk 1 (ess), så ville verdien blitt 4+8+1=13. 
# 
# **Eksempel på kjøring:**
# ```
# Dealers cards are 9 and ?
# Your score is: 16
# Do you want another card? (J/N) J
# Your score is: 19
# Do you want another card? (J/N) N
# Dealers score is: 18
# You won!
#   
# Dealers cards are 10 and ?
# Your score is: 20
# Do you want another card? (J/N) N
# Dealers score is: 21
# You lost
#   
#   
# Dealers cards are 10 and ?
# Your score is: 15
# Do you want another card? (J/N) J
# You got: 25
# You lost
# ```
# 
# ***Skriv koden din i kodeblokken under***

# In[ ]:


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

