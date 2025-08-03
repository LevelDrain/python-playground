FROM python:3.11-slim

# 必須パッケージのインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    && pip install --upgrade pip \
    && rm -rf /var/lib/apt/lists/*

# Jupyter と必要パッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 作業ディレクトリを設定
WORKDIR /app

# ポート開放
EXPOSE 8888

# Jupyter Notebookの起動
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# コンテナ起動法（メモ）
# docker build -t python-playground .
# docker run -p 8888:8888 -v "$PWD":/app python-playground
