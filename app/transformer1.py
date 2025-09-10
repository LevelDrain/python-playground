import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleSelfAttention(nn.Module):
    def __init__(self, embed_size):
        super().__init__()
        self.embed_size = embed_size
        self.embed_size=embed_size
        # Q, K, V を作る線形層
        self.query = nn.Linear(embed_size, embed_size)
        self.key = nn.Linear(embed_size, embed_size)
        self.value = nn.Linear(embed_size, embed_size)

    def forward(self, x):
        # x: (seq_len, embed_size)
        Q=self.query(x)
        K=self.key(x)
        V=self.value(x)

        # Attentionスコアを計算 (seq_len, seq_len)
        scores = torch.matmul(Q, K.T) / (self.embed_size ** 0.5)
        attention=F.softmax(scores, dim=-1)

        out = torch.matmul(attention, V)  # (seq_len, embed_size)
        return out, attention

# 超ミニデータ
sentences = [
    "私は猫です",
    "私は犬です",
]

# 単語をIDに変換
word2idx = {}
idx = 0
for sent in sentences:
    for w in sent.split():
        if w not in word2idx:
            word2idx[w] = idx
            idx += 1

idx2word = {i: w for w, i in word2idx.items()}
vocab_size = len(word2idx)

# 単語IDのリストに変換
data = [[word2idx[w] for w in sent.split()] for sent in sentences]

print("単語→ID:", word2idx)
print("ID化データ:", data)

embed_size = 16 #超小さい
embedding = nn.Embedding(vocab_size, embed_size)

# 試しにID化データのEmbeddingを取得
x=torch.tensor(data[0])  # 最初の文章
x_embed = embedding(x)

attention_layer = SimpleSelfAttention(embed_size)

out, attention = attention_layer(x_embed)

print("出力ベクトル:", out.shape)        # (seq_len, embed_size)
print("Attentionスコア:", attention.shape)    # (seq_len, seq_len)