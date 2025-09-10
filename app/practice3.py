import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('Agg') 

# 3次元リンゴベクトルセット
apples={
    "A":np.array([1, 2, 3]),
    "B":np.array([2, 1, 3]),
    "C":np.array([0, 1, 2]),
    "D":np.array([1, 2, 4])
}

# 3Dプロット準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# リンゴをプロット
for name, vec in apples.items():
    ax.scatter(vec[0], vec[1], vec[2], s=100, label=name) #sは大きさ
    ax.text(vec[0], vec[1], vec[2], f'{name}', size=12, zorder=1)

ax.set_xlabel('color')
ax.set_ylabel('shape')
ax.set_zlabel('taste')
ax.set_title('Apple Vectors in 3D Space')

ax.legend()
# plt.show()
plt.savefig('plot.png')