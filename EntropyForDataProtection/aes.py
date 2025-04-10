from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import numpy as np
from scipy.stats import entropy

def encrypt_aes():
    key = os.urandom(32)  
    iv = os.urandom(16)
    plaintext = os.urandom(1024)  

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return ciphertext

def shannon_entropy(data):
    _, counts = np.unique(list(data), return_counts=True)
    probabilities = counts / len(data)
    return entropy(probabilities, base=2)

ciphertext_aes = encrypt_aes()
entropy_aes = shannon_entropy(ciphertext_aes)
print(f"AES Entropy: {entropy_aes:.4f}")