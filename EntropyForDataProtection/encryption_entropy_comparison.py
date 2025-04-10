from matplotlib import pyplot as plt


algorithms = ['AES', 'RSA', 'ChaCha20']
entropies = [7.98, 7.95, 7.99]

plt.figure(figsize=(8, 5))
plt.bar(algorithms, entropies, color=['blue', 'green', 'red'])
plt.title('Сравнение энтропии шифрования')
plt.ylabel('Энтропия (бит/байт)')
plt.ylim(7.8, 8.0)
plt.show()