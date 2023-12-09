# spotify_list_music

## Скрипт для выведения списка песен в плейлисте

##### Создайте свой файл .env в папке с файлом `spotify.py` и заполните его своими данными по аналогии с `.env.example`

```
SPOTIPY_CLIENT_ID='lalala123'
SPOTIPY_CLIENT_SECRET='lalala123'
SPOTIPY_REDIRECT_URI='http://localhost:8080/callback'
```

##### Создайте виртуальное окружение:

```
python -m venv venv
```

##### Активируйте его:

```
source venv/Scripts/activate
```

##### Установите пакеты из requirements.txt:

```
pip install -r requirements.txt
```

##### Запустите скрипт:

```
python spotify.py
```
