from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {'author': 'John', 'title': 'Python 101', 'category': 'Python'},
    {'author': 'Doe', 'title': 'Python 102', 'category': 'Python'},
    {'author': 'Smith', 'title': 'Python 103', 'category': 'Python'},
    {'author': 'John', 'title': 'C++ 101', 'category': 'C++'},
    {'author': 'Doe', 'title': 'Java 102', 'category': 'Java'},
    {'author': 'Smith', 'title': 'Java 103', 'category': 'Java'},
]

# The order of functions is important to fastapi.
# If you put the '/books/{title}' function before the '/books/mybook' function, 
# when i wrote: http://127.0.0.1:8000/books/mybook, it would return the content of
# '/books/{title}' function, because the interpretation of fastapi is top to bottom :).



@app.get('/books/')
async def get_all_books():
    return BOOKS

@app.get('/books/{author}/')
async def get_all_books_by_author(author : str) -> list:
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return

@app.route('/books/mybook')
async def get_all_books():
    return {'my_favorite_book': 'Python 101'}

@app.get('/books/{title}')
async def get_all_books(title : str):
    for book in BOOKS:
        if book.get('title').casefold() == title.casefold():
            return book
        
@app.get("/books/")
async def read_category_by_query(category : str):
    print(category)
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author : str, category : str = ''):
    books_to_return = []
    for book in BOOKS:
        print(book.get('author'), book_author)
        if book.get('author').casefold() == book_author.casefold() and \
            book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    
    
@app.put('/books/update_book/')
async def update_book(update_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title') == update_book.get('title'):
            BOOKS[i] = update_book
            
@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


            