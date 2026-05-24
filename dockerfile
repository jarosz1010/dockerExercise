# 1. Obraz bazowy z Pythonem
FROM python:3.10-slim

# 2. Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# 3. Skopiowanie pliku zależności i ich instalacja
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 4. Skopiowanie reszty kodu aplikacji
COPY . .

# 5. Określenie portu, na którym działa aplikacja
EXPOSE 5000

# 6. Komenda uruchamiająca aplikację
CMD ["python", "app.py"]