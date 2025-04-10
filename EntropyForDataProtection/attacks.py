from Crypto.Cipher import AES, PKCS1_OAEP, ChaCha20
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
import itertools
import math

# 1. Brute-force атака на AES (слабый 16-битный ключ)
def aes_brute_force_attack():
    print("\n[Brute-force атака на AES]")
    key_space = itertools.product(range(256), repeat=2) 
    plaintext = b"secret data!!!"
    key = b"\x01\x02" + b"\x00" * 14  
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    for attempt in key_space:
        test_key = bytes(attempt) + b"\x00" * 14 
        test_cipher = AES.new(test_key, AES.MODE_ECB)
        try:
            decrypted = unpad(test_cipher.decrypt(ciphertext), AES.block_size)
            if decrypted == plaintext:
                print(f"Взломано! Ключ: {test_key.hex()}")
                return test_key.hex()
        except:
            continue
    print("Ключ не найден (попробуйте уменьшить диапазон).")
    return None

# 2. RSA Factorization Attack (простая атака разложения на множители)
def rsa_factorization_attack(n):
    print("\n[Factorization атака на RSA]")
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p, q = i, n // i
            print(f"Факторизация найдена: p = {p}, q = {q}")
            return p, q
    print("Факторизация не удалась.")
    return None

# 3. Bit-Flipping атака на ChaCha20
def chacha20_bit_flip_attack():
    print("\n[Bit-Flipping атака на ChaCha20]")
    key = b"this is 32byte key for chacha20" 
    nonce = b"12345678" 

    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = b"Hello! You are an admin!" 
    ciphertext = cipher.encrypt(plaintext)

    modified_ciphertext = bytearray(ciphertext)
    modified_ciphertext[10] ^= 1  

    decipher = ChaCha20.new(key=key, nonce=nonce)
    modified_plaintext = decipher.decrypt(bytes(modified_ciphertext))
    
    print(f"Оригинальный текст: {plaintext}")
    print(f"Изменённый текст:   {modified_plaintext.decode(errors='ignore')}")
    return modified_plaintext
