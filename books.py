from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {'author': 'John', 'title': 'Python 101', 'category': 'Python'},
    {'author': 'Doe', 'title': 'Python 102', 'category': 'Programming'},
    {'author': 'Smith', 'title': 'Python 103', 'category': 'Programming'},
    {'author': 'John', 'title': 'C++ 101', 'category': 'C++'},
    {'author': 'Doe', 'title': 'Java 102', 'category': 'Java'},
    {'author': 'Smith', 'title': 'Java 103', 'category': 'Java'},
]

# The order of functions is important to fastapi.
# If you put the '/books/{title}' function before the '/books/mybook' function, 
# when i wrote: http://127.0.0.1:8000/books/mybook, it would return the content of
# '/books/{title}' function, because the interpretation of fastapi is top to bottom :).

@app.get('/books')
async def get_all_books():
    return BOOKS

@app.route('/books/mybook')
async def get_all_books():
    return {'my_favorite_book': 'Python 101'}

@app.get('/books/{title}')
async def get_all_books(title : str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book