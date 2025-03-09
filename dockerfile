# Python 3.10 bazasidan foydalanamiz
FROM python:3.10  

# Ishchi katalog yaratish
WORKDIR /app  

# Talab qilinadigan fayllarni yuklash
COPY pyproject.toml poetry.lock ./

# Poetry va kerakli kutubxonalarni o‘rnatish
RUN pip install poetry && poetry install --no-root --no-dev  

# Loyihadagi barcha fayllarni konteynerga yuklash
COPY . .

# Botni ishga tushirish
CMD ["poetry", "run", "python", "main.py"]