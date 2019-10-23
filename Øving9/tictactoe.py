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
