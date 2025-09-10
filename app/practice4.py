import itertools
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('Agg')
# 3Dプロット準備
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

apples={
    "A":np.array([1, 2, 3]),
    "B":np.array([2, 1, 3]),
    "C":np.array([0, 1, 2]),
    "D":np.array([1, 2, 4]),
    "E":np.array([0, 5, 3]),
    "F":np.array([2, 0, 3]),
    "G":np.array([0, 1, 0]),
    "H":np.array([6, 2, 4])
}

pairs=list(itertools.combinations(apples.keys(), 2))
for p1, p2 in pairs:
    vec1, vec2 = apples[p1], apples[p2]
    sim=np.dot(apples[p1], apples[p2])
    print(f"{p1}と{p2}の似てる度: {sim}")

for p1, p2 in pairs:
    vec1, vec2 = apples[p1], apples[p2]
    sim = np.dot(vec1, vec2)
    alpha = min(1.0, 0.3 + 0.05 * sim)
    ax.plot([vec1[0], vec2[0]], [vec1[1], vec2[1]], [vec1[2], vec2[2]], 'gray', alpha=alpha)

ax.set_xlabel('color')
ax.set_ylabel('shape')
ax.set_zlabel('taste')
ax.set_title('Apple Vectors in 3D Space')

# plt.show()
plt.savefig('plot.png')