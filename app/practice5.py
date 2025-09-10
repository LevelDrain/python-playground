import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import AgglomerativeClustering

# いくつかのリンゴベクトルを作る
apples = {
    "A": np.array([1, 2, 3]),
    "B": np.array([2, 1, 3]),
    "C": np.array([0, 1, 2]),
    "D": np.array([1, 2, 4]),
    "E": np.array([3, 2, 1]),
    "F": np.array([0, 0, 1]),
    "G": np.array([2, 2, 2]),
    "H": np.array([1, 1, 1])
}

names = list(apples.keys())
vectors = np.array(list(apples.values()))

# 階層的クラスタリング
clustering = AgglomerativeClustering(n_clusters=2)
labels = clustering.fit_predict(vectors)

# 3Dプロット準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# クラスタごとに色を変えてプロット
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan']
for i, vec in enumerate(vectors):
    ax.scatter(vec[0], vec[1], vec[2], s=100, color=colors[labels[i] % len(colors)], label=names[i])
    ax.text(vec[0], vec[1], vec[2], names[i])

ax.set_xlabel('color')
ax.set_ylabel('shape')
ax.set_zlabel('taste')
ax.set_title('Apple Clusters in 3D Space')

plt.show()