import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randint(0, 256, size=1024)
sns.histplot(data, bins=50, kde=True)
plt.title('Распределение вероятностей байтов')
plt.xlabel('Значение байта')
plt.ylabel('Частота')
plt.show()