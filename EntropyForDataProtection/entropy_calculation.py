import numpy as np
from scipy.stats import entropy

def shannon_entropy(data):
    _, counts = np.unique(data, return_counts=True)
    probabilities = counts / len(data)
    return entropy(probabilities, base=2)

def cross_entropy(p, q):
    p = np.asarray(p)
    q = np.asarray(q)
    return -np.sum(p * np.log2(q))

example_data = np.random.randint(0, 256, size=1024, dtype=np.uint8)
print("Shannon Entropy:", shannon_entropy(example_data))
