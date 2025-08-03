FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "-i"]

# コンテナ起動法（メモ）
# docker build -t python-playground .
# docker run -it --rm python-playground