# Gunakan image Python resmi sebagai dasar
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /app

RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Salin file requirements.txt ke dalam container dan install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Salin seluruh aplikasi Flask ke dalam container
COPY . .

# Tentukan perintah untuk menjalankan aplikasi
CMD ["flask", "run", "--host=0.0.0.0"]
