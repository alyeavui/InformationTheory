import os
import random

def generate_encrypted_stream(length=256):
    return os.urandom(length)

streams = [generate_encrypted_stream() for _ in range(10)]

for i, stream in enumerate(streams):
    print(f"Stream {i + 1}: {stream.hex()}")