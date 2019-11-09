from os import system
from string import ascii_uppercase
from copy import deepcopy


def make_board( board_string, size ):
    matrix = []
    for i in range( size ):
        row =[]
        for j in range( size ):
            str_pos = i*size + j
            if board_string[ str_pos ] is '.': row.append( None )
            else: row.append( board_string[ str_pos ] )
        matrix.append(row)
    return matrix


def disp_board( board ):
    piece_dict ={'r':'♖', 'R':'♜', 'b':'♗', 'B':'♝', 'n':'♘', 'N':'♞', 'q':'♕', 'Q':'♛', 'k':'♔', 'K':'♚', 'p':'♙', 'P':'♟', None:' '}
    linebreak = '  *' + '-'*(len(board)*4-1) + '*'
    print( linebreak )
    for y, r in enumerate(board):
        line = f"{len(r)-y} |"
        for p in r: line += ' ' + piece_dict[ p ] + ' |'
        print( line )
        if y == len(board)-1: break
        linebreak = "  " + '|---'*len(r) + '|'
        print(linebreak)
    linebreak = '  *' + '-'*(len(board)*4-1) + '*'
    print( linebreak )
    linebreak = '  '
    for i, c in enumerate( ascii_uppercase ):
        if i == len(board): break
        else: linebreak += f'  {c} '
    print( linebreak )


def get_piece( board, x, y ): return board[ y ][ x ]


def move_pice( field, origin, to ):
    field[to[1]][to[0]] = get_piece( field, origin[0], origin[1] )
    field[origin[1]][origin[0]] = None


def get_color( board, x, y ):
    white = True
    piece = get_piece( board, x, y )
    if piece is None: white = None
    elif piece == piece.lower(): white = False
    return white


def oob( board, x, y ):
    if x >= len( board ) or x<0 or y >= len( board ) or y<0: return True
    else: return False


def pawn_on_start( white, y, board_size ):
    if white and y == board_size-2: return True
    elif white is False and y ==1: return True
    else: return False


def pawn_moves( board, x, y, white ):
    direction = 1
    if white: direction *= -1
    moves = []
    if get_piece( board, x, y + direction ) is None:
        moves.append(( x, y + direction ))
    if get_piece( board, x, y + 2 * direction ) is None and pawn_on_start( white, y, len(board) ):
        moves.append( ( x, y + 2 * direction ) )
    if not oob(board, x+1, y+ direction) and not white == get_color(board, x-1 , y + direction) and get_color(board, x-1 , y + direction) != None:
        moves.append( ( x - 1, y + direction ) )
    if not oob(board, x+1, y+ direction) and not white == get_color(board, x+1 , y + direction) and get_color(board, x+1 , y + direction) != None:
        moves.append( ( x + 1, y + direction ) )
    return moves


def knight_moves( board, x, y, white ):
    from copy import deepcopy
    dirs = [-2, -1, 1, 2]
    moves = []
    for X in dirs:
        for Y in dirs:
            if abs(Y) != abs(X):
                if not oob( board, x+X, y+Y ) and get_color( board, x+X, y+Y ) != white:
                    moves.append( ( x+X, y+Y ) )
    return moves


def king_moves( board, x, y, white ):
    dirs = [-1, 0 , 1]
    moves = []
    for X in dirs:
        for Y in dirs:
            if not oob( board, x+X, y+Y ) and get_color( board, x+X, y+Y ) != white:
                moves.append( ( x+X, y+Y ) )
    return moves


def bishop_moves( board, x, y, white ):
    dirs = [-1, 1]
    moves = []
    for X in dirs:
        for Y in dirs:
            i  = 1
            while True:
                if oob( board, x+X*i, y+Y*i ): break
                elif get_piece( board, x+X*i, y+Y*i ) is None:
                    moves.append( ( x+X*i, y+Y*i ) )
                elif get_color( board, x+X*i, y+Y*i ) != white:
                    moves.append( ( x+X*i, y+Y*i ) )
                    break
                else: break
                i += 1
    return moves


def rook_moves( board, x, y, white ):
    dirs = [-1, 1]
    moves = []
    for X in dirs:
        i = 1
        while True:
            if oob( board, x+X*i, y ): break
            elif get_piece( board, x+X*i, y ) is None:
                moves.append( ( x+X*i, y ) )
            elif get_color( board, x+X*i, y ) != white:
                moves.append( ( x+X*i, y ) )
                break
            else: break
            i += 1
    for Y in dirs:
        i = 1
        while True:
            if oob( board, x, y+Y*i ): break
            elif get_piece( board, x, y+Y*i ) is None:
                moves.append( ( x, y+Y*i ) )
            elif get_color( board, x, y+Y*i ) != white:
                moves.append( ( x, y+Y*i ) )
                break
            else: break
            i += 1
    return moves


def queen_moves( board, x, y, white ):
    moves = bishop_moves( board, x, y, white )
    moves[len(moves):len(moves)] = rook_moves( board, x, y, white )
    return moves


def get_legal_moves( board, x, y ): #where you stil can put the king in check
    moves = []
    piece = get_piece( board, x, y )
    white = get_color( board, x, y )
    if get_piece( board, x, y ) is None: return moves
    elif get_piece( board, x, y ).lower() == 'p':
        moves =  pawn_moves( board, x, y, white )
    elif get_piece( board, x, y ).lower() == 'n':
        moves =  knight_moves(board, x,y, white)
    elif get_piece( board, x, y ).lower() == 'k':
        moves =  king_moves(board, x,y, white)
    elif get_piece( board, x, y ).lower() == 'b':
        moves =  bishop_moves(board, x,y, white)
    elif get_piece( board, x, y ).lower() == 'r':
        moves =  rook_moves(board, x,y, white)
    elif get_piece( board, x, y ).lower() == 'q':
        moves =  queen_moves(board, x,y, white)
    return moves



def get_all_moves( board, white ):
    moves = []
    for y, r in enumerate(board):
        for x in range(len( r )):
            if get_color( board, x, y ) == white and get_piece( board, x, y ) != None:
                moves[len(moves):len(moves)] = get_legal_moves( board, x, y )
    return moves


def find_king( board, white ):
    king = None
    for y, r in enumerate( board ):
        for x in range( len( r ) ):
            if get_piece( board, x, y ) != None and get_piece( board, x, y ).lower() == 'k' and get_color( board, x, y ) is white:
                king = ( x, y )
                break
        if king != None:
            break
    return king


def check( board, white ):
    king = find_king( board, white )
    if king in get_all_moves( board, not white ):
        return True
    else:
        return False


def rm_check_moves( board, piece, moves, white ):
    res = []
    for move in moves:
        tmp_boad = deepcopy(board)
        move_pice( tmp_boad, piece, move )
        if not check( tmp_boad, white ):
            res.append( move )
    return res


def get_all_moves_wo_check( board, white ):
    moves = []
    for y, r in enumerate(board):
        for x in range(len( r )):
            if get_color( board, x, y ) == white and get_piece( board, x, y ) != None:
                legal_moves = rm_check_moves( board, (x, y), get_legal_moves( board, x, y ), white )
                moves[len(moves):len(moves)] = legal_moves
    return moves


def get_move( board, white_turn, checked ):
    piece = None
    move = None
    while True:
        system('clear')
        disp_board( board )
        if checked: print( 'Check!' )
        greeting = ', how do you want to move?'
        if white_turn:
            greeting = 'White' + greeting
        else:
            greeting = 'Black' + greeting
        print( greeting )
        piece = input( 'From: ' )
        if len( piece ) == 2 and piece[0].isalpha() and piece[1].isdigit():
            if ascii_uppercase.index( piece[0].upper() ) <= len( board ) and int( piece[1] ) <= len( board ):
                piece = ( ascii_uppercase.index( piece[0].upper() ), len(board) - int( piece[1] ) )
            else:
                continue
        else:
            continue
        if get_color( board, piece[0], piece[1] ) != white_turn:
            continue
        moves = rm_check_moves( board, piece, get_legal_moves( board, piece[0], piece[1]), white_turn )
        if moves != []:
            move = input( 'To: ' )
            if len( move ) == 2 and move[0].isalpha() and move[1].isdigit():
                if ascii_uppercase.index( move[0].upper() ) <= len( board ) and int( move[1] ) <= len( board ):
                    move = ( ascii_uppercase.index( move[0].upper() ), len( board ) - int( move[1] ) )
                    if move in moves:
                        break
                else:
                    continue
            else:
                continue
    return piece, move


def can_promote( board, x, y, white ):
    if white and get_piece( board, x, y ) == 'P' and y == 0: return True
    elif not white and get_piece( x, y ) == 'p' and y == len(board)-1: return True
    else: return False


def promote( board, x, y, white ):
    while True:
        system('clear')
        disp_board( board )
        print( 'You can promote a piece. Do you want a (Q)ueen, a (B)ishop,  a K(n)ight or a (R)ook?' )
        choise = input()
        if len(choise) == 1 and choise.lower() in 'qnbr':
            if white:
                board[ y ][ x ] = choise.upper()
            else:
                board[ y ][ x ] = choise.lower()
            break


def main():
    board_string_1 = 'rnbqkbnrpppppppp................................PPPPPPPPRNBQkBNR'
    board = make_board(board_string_1, 8)
    white = True
    checked = False
    while True:
        piece, move = get_move( board, white, checked )
        move_pice( board, piece, move )
        if can_promote( board, move[0], move[1], white ):
            promote( board, move[0], move[1], white )
        if find_king( board, not white ) in get_all_moves_wo_check( board, white ):
            checked = True
            if get_all_moves_wo_check( board, not white ) == []:
                break
        else:
            checked = False
        white = not white
    system('clear')
    disp_board( board )
    print( 'checkmate' )


main()
