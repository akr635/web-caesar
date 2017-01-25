def alphabet_position(letter):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letter in alphabet_lower:
        alphabet_position = alphabet_lower.index(letter)
    elif letter in alphabet_upper:
        alphabet_position = alphabet_upper.index(letter)
    return alphabet_position

def rotate_character(char, rot):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char in alphabet_lower:
        rotate_position = (alphabet_position(char) + rot) % 26
        rotate_character = alphabet_lower[rotate_position]
    elif char in alphabet_upper:
        rotate_position = (alphabet_position(char) + rot) % 26
        rotate_character = alphabet_upper[rotate_position]
    else:
        rotate_character = char
    return rotate_character

def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted += rotate_character(char, rot)
    return encrypted
