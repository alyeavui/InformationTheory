from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def shannon_entropy(data):
    _, counts = np.unique(list(data), return_counts=True)
    probabilities = counts / len(data)
    return entropy(probabilities, base=2)

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

plaintext = os.urandom(190)

ciphertext_rsa = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

entropy_rsa = shannon_entropy(ciphertext_rsa)
print(f"RSA Entropy: {entropy_rsa:.4f}")