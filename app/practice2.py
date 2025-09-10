import numpy as np

# いくつかのリンゴベクトルを作る
apple_a=np.array([1, 2, 3]) # [色, 形, 味]
apple_b=np.array([2, 1, 3])
apple_c=np.array([0, 0, 1])
apple_d=np.array([1, 2, 4])

apples={"A":apple_a, "B":apple_b, "C":apple_c, "D":apple_d}

# 似てる度（内積）を計算
def similarity(apple1, apple2):
    return np.dot(apple1, apple2)

# 最も似てる組を探す
max_sim=-1
best_pair=None

for name1, vec1 in apples.items():
    for name2, vec2 in apples.items():
        if name1 < name2:  # 重複を避けるため
            sim = similarity(vec1, vec2)
            print(f"{name1}と{name2}の似てる度: {sim}")
            if sim > max_sim:
                max_sim = sim
                best_pair = (name1, name2)

print(f"\n一番似てるリンゴは:{best_pair} (似てる度: {max_sim})")