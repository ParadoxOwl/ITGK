import binascii
import random
import string

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')


def encrypt( secret, key ):
    #Transform secret and key to hex
    S = toHex(bytes(secret, encoding = 'ascii'))
    K = toHex(bytes(key, encoding = 'ascii'))
    #Return code S ^ M
    return S^K


def decrypt( code, key ):
    K = toHex(bytes(key, encoding = 'ascii'))
    return toString(K^code)


def main():
    message = input( 'Hva er meldingen? ' )
    key = ''
    for i in range(len(message)):
        key += random.choice(string.ascii_letters)
    crypted = encrypt( message, key )
    print( f'Krypto: {crypted}\nMelding: {message}' )


print( encrypt( 'hei', 'abc' ) )
print( decrypt( 591626, 'abc' ) )
main()
