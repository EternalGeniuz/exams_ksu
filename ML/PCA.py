from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Загрузка данных
data = load_iris()
X = data.data

# Применение PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Визуализация данных
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=data.target, cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
