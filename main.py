from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, DBBook

app = FastAPI(title = "Könyvtár API")

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class BookResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True

# ideiglenes "adatbázis"
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Üdvözlünk a Könyvtár API-ban!"}

@app.post("/books/", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = next(get_db())):
    db_book = DBBook(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(DBBook).all()