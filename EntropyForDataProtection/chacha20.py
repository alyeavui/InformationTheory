from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def shannon_entropy(data):
    _, counts = np.unique(list(data), return_counts=True)
    probabilities = counts / len(data)
    return entropy(probabilities, base=2)

def encrypt_chacha():
    key = os.urandom(32)
    nonce = os.urandom(16)
    plaintext = os.urandom(1024)

    cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext)

    return ciphertext

ciphertext_chacha = encrypt_chacha()
entropy_chacha = shannon_entropy(ciphertext_chacha)
print(f"ChaCha20 Entropy: {entropy_chacha:.4f}")