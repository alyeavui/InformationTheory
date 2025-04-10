import os
import random
import string
import numpy as np
from Crypto.Cipher import AES, ChaCha20
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from scipy.stats import entropy
from typing import List, Tuple


def generate_random_plaintext(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def generate_low_entropy_plaintext(length: int) -> str:
    return 'A' * length 


def calculate_entropy(data: bytes) -> float:
    probabilities = np.bincount(list(data), minlength=256) / len(data)
    return entropy(probabilities, base=2)


def aes_encrypt(plaintext: str) -> bytes:
    key = os.urandom(32) 
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = plaintext.ljust((len(plaintext) + 15) // 16 * 16) 
    return cipher.encrypt(padded_plaintext.encode())


def rsa_encrypt(plaintext: str) -> bytes:
    key = RSA.generate(2048)
    cipher = PKCS1_OAEP.new(key)
    return cipher.encrypt(plaintext.encode())


def chacha20_encrypt(plaintext: str) -> bytes:
    key = os.urandom(32)
    nonce = os.urandom(12)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.encrypt(plaintext.encode())


def generate_dataset(num_samples: int) -> List[Tuple[bytes, int]]:
    dataset = []
    for _ in range(num_samples // 2):
        plaintext = generate_random_plaintext(128)
        low_entropy_plaintext = generate_low_entropy_plaintext(128)

        for encrypt_func in [aes_encrypt, rsa_encrypt, chacha20_encrypt]:
            encrypted_data = encrypt_func(plaintext)
            entropy_value = calculate_entropy(encrypted_data)
            dataset.append((encrypted_data, 1)) 

            encrypted_data_low = encrypt_func(low_entropy_plaintext)
            entropy_value_low = calculate_entropy(encrypted_data_low)
            dataset.append((encrypted_data_low, 0))  
    return dataset

dataset = generate_dataset(100)

import pickle
with open('encrypted_dataset.pkl', 'wb') as f:
    pickle.dump(dataset, f)

print("Dataset generated and saved successfully!")