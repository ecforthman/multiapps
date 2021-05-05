import re
from string import ascii_uppercase


# ------------- encryption -------------------------------------------------

def encrypt_word(word_in, offset):
    word_out = ""
    for word_index, word_char in enumerate((word_in).upper()):
        for alphabet_index, alphabet_char in enumerate(ascii_uppercase):
            if word_char == alphabet_char:
                if (alphabet_index + offset) < 26 :
                    word_out += ascii_uppercase[alphabet_index + offset]
                    break
                else:
                    word_out += ascii_uppercase[alphabet_index + offset - 26]
                    break
    return word_out


def encrypt_file(msg_string, word_in, offset):
    key_word = encrypt_word(word_in, offset)
    offsets = vigenere_offsets(word_in)
    offsets_index = 0
    file_string = msg_string.upper()
    out_string = ""

    for c in file_string:
        matchChar = re.search(r'[A-Z]',  c)
        if matchChar:
            c = encrypt_word(c , offsets[offsets_index])
            if offsets_index < len(offsets) - 1:
                offsets_index += 1
            else:
                offsets_index = 0
        out_string += c
    return out_string


# ------------ decryption ---------------------------------------------------

def decrypt_word(word_in, offset):
    word_out = ""
    for i, x in enumerate((word_in).upper()):
        for j, y in enumerate(ascii_uppercase):
            if x ==  y:
                if  j >= offset:
                    word_out += ascii_uppercase[ j - offset]
                    break
                else:
                    word_out += ascii_uppercase[ j - offset  + len(ascii_uppercase)]
                    break
    return word_out


def decrypt_file(msg_string, word_in, offset_in):
    key = decrypt_word(word_in.rstrip('\r\n'), offset_in)
    offsets = vigenere_offsets(key)
    offsets_index = 0
    line_number = -1
    out_string = ""
    for c in msg_string:
        matchChar = re.search(r'[A-Z]',  c)
        if matchChar:
            c = decrypt_word(c , offsets[offsets_index])
            if offsets_index < len(offsets) - 1:
                offsets_index += 1
            else:
                offsets_index = 0
        out_string += c
    return(out_string)

# ---------------- common ----------------------------------


def vigenere_offsets(word_in):
    vigenere_offsets = []
    for i, x in enumerate(word_in.upper()):
        for j, y in enumerate(ascii_uppercase):
            if x ==  y:
                vigenere_offsets.append(j)
    return vigenere_offsets