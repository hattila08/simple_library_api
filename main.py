from FastAPI import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title = "Könyvtár API")

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

# ideiglenes "adatbázis"
fake_db = []

@app.get("/")
def read_root():
    return {"message": "Üdvözlünk a Könyvtár API-ban!"}

@app.post("/books/")
def create_book(book: Book):
    fake_db.append(book)
    return {"message": "Könyv hozzáadva", "book": book}

@app.get("/books/")
def get_books():
    return fake_db