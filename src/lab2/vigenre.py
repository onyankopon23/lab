def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    id_key = 0
    keyword_up = keyword.upper()
    for i in plaintext:
        if "A" <= i <= "Z":
            shift = ord(keyword_up[id_key % len(keyword_up)]) - ord("A")
            new_i = chr((ord(i) - ord("A") + shift) % 26 + ord("A"))
            ciphertext += new_i
            id_key += 1
        elif "a" <= i <= "z":
            shift = ord(keyword_up[id_key % len(keyword_up)]) - ord("A")
            new_i = chr((ord(i) - ord("a") + shift) % 26 + ord("a"))
            ciphertext += new_i
            id_key += 1
        else:
            ciphertext += i

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    id_key = 0
    keyword_up = keyword.upper()
    for i in ciphertext:
        if "A" <= i <= "Z":
            shift = ord(keyword_up[id_key % len(keyword_up)]) - ord("A")
            new_i = chr((ord(i) - ord("A") - shift) % 26 + ord("A"))
            plaintext += new_i
            id_key += 1
        elif "a" <= i <= "z":
            shift = ord(keyword_up[id_key % len(keyword_up)]) - ord("A")
            new_i = chr((ord(i) - ord("a") - shift) % 26 + ord("a"))
            plaintext += new_i
            id_key += 1
        else:
            plaintext += i
    return plaintext