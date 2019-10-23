#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li ><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li ><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
#     <li ><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li ><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#         <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li class="active"><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Tre på rad
# 
# **Læringsmål:**
# 
# * Lister
# * Funksjoner 
# * Betingelser
# * Strenger
#  
# I denne oppgaven skal du implementere det populære spillet 3 på rad. Spillet er for to spillere; x og o, som plasserer brikker . En spiller vinner om den klarer å få 3 på rad, enten horisontalt, vertikalt eller diagonalt.
# 
# 
# **a)** Lag en funksjon som skriver ut brettet, det kan f.eks. se slikt ut om du vil:
# 
# ```python
#     1   2   3
#   -------------
# 1 |   |   |   |
#   -------------
# 2 |   |   |   |
#   -------------
# 3 |   |   |   |
#   -------------
#     ```

# In[1]:


def disp_board( board ):
    string = f'''    0   1   2
  *-----------*
0 | {board[0][0]:1} | {board[0][1]:1} | {board[0][2]:1} |
  |-----------|
1 | {board[1][0]:1} | {board[1][1]:1} | {board[1][2]:1} |
  |-----------|
2 | {board[2][0]:1} | {board[2][1]:1} | {board[2][2]:1} |
  *-----------*'''
    print(string)


board = [['', '', ''], ['', '', ''], ['', '', '']]
disp_board( board )


# **b)** Lag en funksjon som sjekker om en spiller har vunnet

# In[4]:


def disp_board( board ):
    string = f'''    0   1   2
  *-----------*
0 | {board[0][0]:1} | {board[0][1]:1} | {board[0][2]:1} |
  |-----------|
1 | {board[1][0]:1} | {board[1][1]:1} | {board[1][2]:1} |
  |-----------|
2 | {board[2][0]:1} | {board[2][1]:1} | {board[2][2]:1} |
  *-----------*'''
    print(string)


def rows( player, board ):
    won = None
    for y in board:
        won = True
        for p in y:
            if p != player:
                won = False
                break
        if won:
            break
    return won


def collums( player, board ):
    won = None
    for x  in enumerate( board[0] ):
        won = True
        for y in enumerate( board ):
            if board[y[0]][x[0]] != player:
                won=False
                break
        if won:
            break
    return won


def diagonals( player, board ):
    won = True
    for i in range( len( board ) ):
        if board[i][i] != player:
            won = False
            break
    if not won:
        won = True
        for i in range( len( board ) ):
            if board[i][-1-i] != player:
                won = False
                break
    return won


def has_won( player, board ):
    return rows( player, board ) or collums( player, board ) or diagonals( player, board )


board = [['x', '', ''], ['', 'x', 'o'], ['', 'o', 'x']]
disp_board( board )
print( has_won( 'x', board ) )


# **c)** Lag en funksjon som tar inn navnene til de to brukerne.

# In[5]:


def get_player_info():
    x = ( 'X', input('Navn til spiller X: ') )
    o = ( 'O', input('Navn til spiller O: ') )
    return x, o


print(get_player_info())


# **d)** Lag en funksjon som sjekker om et trekk er lovlig, altså at det ikke finnes andre brikker der.

# In[6]:


def legal_move( board, x, y ):
    return board[y][x] == ''


# **e)** Lag en funksjon som sjekker at input fra brukeren er riktig, altså at man ikke skriver inn rare tegn, eller skriver inn koordinater utenfor spillebrettet.

# In[9]:


def valid_input( imp ):
    imp = imp.strip()
    if len(imp) != 4:
        return False
    elif ', ' not in imp:
        return False
    else:
        moves = imp.split(', ')
        if moves[0] not in '012' or moves[1] not in '012':
            return False
        else:
            return True


print( valid_input( input( 'x, y: ' ) ) )


# **f)** Sett dette sammen til et fullverdig 3 på rad spill!

# In[11]:


from os import system


def disp_board( board ):
    string = f'''    0   1   2
  *-----------*
0 | {board[0][0]:1} | {board[0][1]:1} | {board[0][2]:1} |
  |-----------|
1 | {board[1][0]:1} | {board[1][1]:1} | {board[1][2]:1} |
  |-----------|
2 | {board[2][0]:1} | {board[2][1]:1} | {board[2][2]:1} |
  *-----------*
  '''
    print(string)


def rows( player, board ):
    won = None
    for y in board:
        won = True
        for p in y:
            if p != player:
                won = False
                break
        if won:
            break
    return won


def collums( player, board ):
    won = None
    for x  in enumerate( board[0] ):
        won = True
        for y in enumerate( board ):
            if board[y[0]][x[0]] != player:
                won=False
                break
        if won:
            break
    return won


def diagonals( player, board ):
    won = True
    for i in range( len( board ) ):
        if board[i][i] != player:
            won = False
            break
    if not won:
        won = True
        for i in range( len( board ) ):
            if board[i][-1-i] != player:
                won = False
                break
    return won


def has_won( player, board ):
    return rows( player, board ) or collums( player, board ) or diagonals( player, board )


def get_player_info():
    x = ( 'X', input('Navn til spiller X: ') )
    o = ( 'O', input('Navn til spiller O: ') )
    return x, o


def legal_move( board, x, y ):
    return board[y][x] == ''


def valid_input( imp ):
    imp = imp.strip()
    if len(imp) != 4:
        return False
    elif ', ' not in imp:
        return False
    else:
        move = imp.split(', ')
        if move[0] not in '012' or move[1] not in '012':
            return False
        else:
            return True, move


def main():
    system( 'clear' )
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    X, O = get_player_info()
    turn = 0
    player = X
    while True:
        x , y = None, None
        system( 'clear' )
        disp_board( board )
        if turn % 2 == 0:
            player = X
        else:
            player = O
        tmp = None
        while True:
            move = input( f'{player[1]}, hvor vil du legge en brikke. x, y: ' )
            tmp = valid_input(move)
            if not tmp is False:
                x, y = tuple( tmp[1] )
                x, y = int(x), int(y)
                if legal_move( board, x, y ):
                    break
        board[y][x] = player[0]
        if has_won( player[0], board ):
            system( 'clear' )
            disp_board( board )
            print( f'{player[1]} vant!' )
            break
        else:
            turn += 1



main()

