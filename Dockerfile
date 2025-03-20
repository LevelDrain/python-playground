# ベースイメージを指定
FROM python:3.10

# 環境変数の設定（Pythonのバッファリングを無効化）
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのコードをコピー
COPY . /app/

# サーバーを起動（docker-composeでオーバーライド可）
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]