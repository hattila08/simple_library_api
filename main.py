from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, DBBook

app = FastAPI(title = "Könyvtár API")

class BookCreate(BaseModel):
    title: str
    author: str
    year: int

class BookResponse(BookCreate):
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
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = DBBook(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(DBBook).all()

@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).where(DBBook.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Könyv nem található")
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).where(DBBook.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Könyv nem található")
    db.delete(db_book)
    db.commit()
    return {"success": True}

@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookCreate, db: Session = Depends(get_db)):
    db_book = db.query(DBBook).where(DBBook.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Könyv nem található")
    db_book.title = book.title
    db_book.author = book.author
    db_book.year = book.year
    db.commit()
    db.refresh(db_book)
    return db_book