def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in plaintext:
        if "A" <= i <= "Z":
            new_i = chr((ord(i) - ord("A") + shift) % 26 + ord("A"))
            ciphertext += new_i

        elif "a" <= i <= "z":
            new_i = chr((ord(i) - ord("a") + shift) % 26 + ord("a"))
            ciphertext += new_i

        else:
            ciphertext += i

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for i in ciphertext:
        if "A" <= i <= "Z":
            new_i = chr((ord(i) - ord("A") - shift) % 26 + ord("A"))
            plaintext += new_i

        elif "a" <= i <= "z":
            new_i = chr((ord(i) - ord("a") - shift) % 26 + ord("a"))
            plaintext += new_i

        else:
            plaintext += i

    return plaintext