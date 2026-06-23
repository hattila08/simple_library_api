# Könyvtár CRUD API (FastAPI & SQLite)

Ez egy egyszerű könyvtár kezelő API, amely Python nyelven, a **FastAPI** keretrendszer segítségével készült. Az adatok perzisztens tárolásáért egy **SQLite** adatbázis felel, az objektum-relációs leképezést (ORM) pedig az **SQLAlchemy** biztosítja.

A projekt célja a modern backend fejlesztési minták alapjainak tanulmánya.

## Funkciók

Az API teljes körű CRUD műveleteket biztosít a könyvek kezeléséhez:

* `POST /books/` - Új könyv hozzáadása az adatbázishoz
* `GET /books/` - Az összes elérhető könyv listázása
* `GET /books/{book_id}` - Egy adott könyv ID alapján
* `PUT /books/{book_id}` - Egy létező könyv adatainak módosítása
* `DELETE /books/{book_id}` - Könyv törlése az adatbázisból

## Alkalmazott Technológiák

* **Python 3.9.2**
* **FastAPI** – Gyors, aszinkron webes keretrendszer
* **Uvicorn** – ASGI webszerver a futtatáshoz
* **SQLAlchemy** – ORM az adatbázis-kezeléshez
* **Pydantic** – Adatvalidáció
* **SQLite** – Beépített, fájl-alapú relációs adatbázis

## Telepítés és Futtatás helyi környezetben

Kövesd az alábbi lépéseket a projekt elindításához a saját gépeden:

### 1. Repozitórium klónozása
```bash
git clone https://github.com/hattila08/simple_library_api.git
cd simple_library_api
```

### 2. Virtuális környezet létrehozása és aktiválása
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:
```bash
python3 -m venv venv
source venv/Scripts/activate
```

### 3. Függőségek telepítése
```bash
pip install -r requirements.txt
```

### 4. A szerver elindítása
```bash
uvicorn main:app --reload
```
A szerver elindulása után az alkalmazás a http://127.0.0.1:8000 címen lesz elérhető.