allowed_num=['1', '2', '3', '4', '5', '6', '7', '8']
allowed_char=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def black_white(num, char, inp): #num and char is a list of allowed numbers and characters, and inp is inptut
    if inp[0].lower() not in char or inp[1] not in num or len(inp) != 2:
        return 'error the first symbol has to be a character a-h \n and the second symbol has to be a number 1-8'
    for x in range(len( char )):
        if char[x] == inp[0].lower():
            for y in range( len( num ) ):
                if num[y] == inp[1]:
                    tmp = ( x + y ) % 2
                    if tmp == 0:
                        return 'black'
                    else:
                        return 'white'

print(black_white(allowed_num, allowed_char, input('pos: ')))
