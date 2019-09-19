import os


def fetch_info():
    os.system('clear')
    sectret = input( 'Skriv inn det hemmelige ordet: ' ).lower()
    lives = int( input( 'Hvor mange forsøk får brukeren: ' ) )
    os.system('clear')
    return sectret, lives


def chars_in_secret( secret ):
    chars = []
    for c in secret:
        if c in chars:
            continue
        else:
            chars.append( c )
    return tuple( chars )


def progress( chars, secret ):
    prog = ''
    for c in secret:
        if c in chars:
            prog += c
        else:
            prog += '*'
    return prog


def has_won(correct_chars, secret_chars):
    ans = True
    for c in secret_chars:
        if c in correct_chars:
            continue
        else:
            ans = False
            break
    return ans


def hangman():
    info = list( fetch_info() )
    secret = info[0]
    lives = info[1]
    secret_chars = chars_in_secret( secret )
    correct_chars = []
    while lives > 0:
        guess = input('Gjett på én bokstav i ordet: ').lower()
        if guess[0] in secret_chars:
            correct_chars.append(guess[0])
            print('Stemmer, bokstaven er i ordet.')
        else:
            lives -= 1
            print(f'Bokstaven {guess[0]} er ikke i ordet.')
            if lives is 0:
                print('Du har ingen liv igjen')
            else:
                print( f'Du har {lives} liv igjen, prøv på nytt.' )
        print(progress(correct_chars, secret))
        if has_won(correct_chars, secret_chars):
            break
    if lives > 0:
        print( f'Du klarte de med {lives} liv igjen.' )
    else:
        print( 'Du klarte de ikke.' )


while True:
    hangman()
    inp = input('En gang til? (J/n): ')
    if inp != 'J':
        break
