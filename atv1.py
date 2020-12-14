def cesar_crypto(text):
    encryption = ""
    text =text.upper()
    for c in text:
        c_unicode = ord(c)
        c_index = ord(c) - ord("A")
        new_index = (c_index + 3) % 26
        new_unicode = new_index + ord("A")
        new_character = chr(new_unicode)
        encryption = encryption + new_character

    return encryption


print(cesar_crypto("criptografia"))