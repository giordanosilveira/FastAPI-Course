from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int
    
    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='Id is not required on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)
    published_date: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new title",
                "author": "Giordano",
                "description": "A new description for this book",
                "rating": 5,
                "published_date": 2021
            }
        }
    }
       
BOOKS = [
    Book(1, 'Python 101', 'John Doe', 'Python for beginners', 5, 2010),
    Book(2, 'Python 102', 'John Doe', 'Python for intermediate', 5, 2010),
    Book(3, 'Python 103', 'John Doe', 'Python for advanced', 4, 2015),
    Book(4, 'Java 101', 'Smith', 'Java for beginners', 4, 2016),
    Book(5, 'Java 102', 'Brandon Sanderson', 'Java for intermediate', 3, 2024),
    Book(6, 'Java 103', 'Ale Santos', 'Java for advanced', 3, 2024),
]




@app.get('/books/{book_id}', status_code=status.HTTP_200_OK) 
async def get_book(book_id : int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Tem not found")
        
@app.get('/books', status_code=status.HTTP_200_OK)
async def get_all_books():
    return BOOKS        

@app.get('/books/', status_code=status.HTTP_200_OK)
async def get_book_by_rating(rating: int = Query(gt=0, lt=6)):
    return [book for book in BOOKS if book.rating == rating]


@app.get('/books/published-date/{published_date}', status_code=status.HTTP_200_OK)
async def get_book_by_published_date(published_date: int = Path(gt=0)):
    return [book for book in BOOKS if book.published_date == published_date]


@app.put('/books/update-book/', status_code=status.HTTP_200_OK)
async def update_book(book_request: BookRequest):
    for book in BOOKS:
        if book.id == book_request.id:
            book.title = book_request.title
            book.author = book_request.author
            book.description = book_request.description
            book.rating = book_request.rating
            return book
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete('/books/delete-book/{book_id}', status_code=status.HTTP_200_OK)
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            book = BOOKS.pop(i)
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.post('/create-book/', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)
    return new_book


def find_book_id(book : Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book