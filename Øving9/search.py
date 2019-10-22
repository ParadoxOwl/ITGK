import string


def read_from_file( filename ):
    f = open( filename, 'r' )
    txt = f.read()
    f.close()
    return txt


def remove_symbols( text ):
    for symb in string.printable:
        if symb not in string.ascii_letters and not symb.isspace() :
            text = text.replace( symb, '' )
    return text.lower()


def count_words( filename ):
    text = remove_symbols( read_from_file( filename ) )
    words = text.split()
    d = {}
    for word in words:
        if word.isalpha():
            try:
                d[word] += 1
            except KeyError:
                d[words] = 1


story = read_from_file( 'alice_in_wonderland.txt' )
print(remove_symbols( story ))
