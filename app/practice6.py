import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

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

#データをまとめて行列に
labels = list(apples.keys())
data = np.array(list(apples.values()))

# 階層的クラスタリング（ユークリッド距離 + Ward法）
z=linkage(data, method='ward', metric='euclidean')

# デンドログラムの描画
plt.figure(figsize=(8, 4))
dendrogram(z, labels=labels, leaf_rotation=0, leaf_font_size=10)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Apple')
plt.ylabel('Distance')
plt.tight_layout()
plt.show()