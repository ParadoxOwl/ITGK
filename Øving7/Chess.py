import string


def make_board( board_string ):
    matrix = []
    for i in range( 5 ):
        row =[]
        for j in range( 5 ):
            str_pos = i*5 + j
            if board_string[ str_pos ] is '.':
                row.append( None )
            else:
                row.append( board_string[ str_pos ] )
        matrix.append(row)
    return matrix


def get_piece( board, x, y ):
    return board[ len( board ) - y ][ x - 1  ]


def get_color( board, x, y ):
    white = True
    piece = get_piece( board, x, y )
    if piece is None:
        return None
    if piece in string.ascii_lowercase:
        white = False
    return white



def pawn_on_start( is_white, y ):
    if is_white and y == 2:
        return True
    elif is_white is False and y ==4:
        return True
    else:
        return False


def pawn_moves( board, x, y, is_white ):
    direction = -1
    if is_white is True:
        direction = 1
    moves = []
    if get_piece( board, x, y + direction ) is None:
        moves.append(( x, y + direction ))
    if get_piece( board, x, y + 2 * direction ) is None and pawn_on_start( is_white, y ):
        moves.append( ( x, y + 2 * direction ) )
    if not is_white == get_color(board, x-1 , y + direction) and get_color(board, x-1 , y + direction) != None and x != 1:
        moves.append( ( x - 1, y + direction ) )
    if not is_white == get_color(board, x+1 , y + direction) and get_color(board, x+1 , y + direction) != None and x != 5:
        moves.append( ( x + 1, y + direction ) )
    return moves



def get_legal_moves( board, x, y ):
    moves = []
    piece = get_piece( board, x, y )
    white = get_color( board, x, y )
    if get_piece( board, x, y ).lower() != 'p':
        return moves
    else:
        return pawn_moves( board, x, y, white )


board_string_1 = 'rkn.r.p.....P..PP.PPB.K..'
board = make_board(board_string_1)
print( get_piece( board, 4, 2 ) )
print( get_legal_moves( board, 4, 2 ) )
print(get_legal_moves(board, 2, 4))
