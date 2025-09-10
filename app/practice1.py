import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

dot_product = np.dot(vector_a, vector_b)

print(f"内積の結果: {dot_product}")

# 2次元のリンゴベクトル
apple_2d=np.array([1, 2]) # [色, 形]

# 3次元のリンゴベクトル
apple_3d=np.array([1, 2, 3]) # [色, 形, 味]

# 10次元のリンゴベクトル
apple_10d=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 次元数
print(f"2次元ベクトルの形状: {apple_2d.shape}")
print(f"3次元ベクトルの形状: {apple_3d.shape}")
print(f"10次元ベクトルの形状: {apple_10d.shape}")