# Name: Peter Kelt
# Date: 01-20-2013
# cipher.py - Use cyclic cipher to encrypt messages.

plain_phrase = raw_input('Enter sentence to encrypt: ')
shift = int(raw_input('Enter shift value: '))

encoded_phrase = ''

for c in plain_phrase:
    ascii_c = ord(c)
    cipher_c = ascii_c + shift

    # Check if upper or lower case alphabetic character, apply encryption.
    if (ascii_c >= 65 and ascii_c < 91):
        if cipher_c > 91:
            cipher_c = cipher_c%91 + 65
        encoded_phrase = encoded_phrase + chr(cipher_c)
    elif (ascii_c >= 97 and ascii_c < 123):
        if cipher_c > 123:
            cipher_c = cipher_c%123 + 97
        encoded_phrase = encoded_phrase + chr(cipher_c)
    else:
        encoded_phrase = encoded_phrase + c

print encoded_phrase
