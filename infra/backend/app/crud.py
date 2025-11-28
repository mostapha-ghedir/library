from .models import books_collection
from .schemas import Book
from bson import ObjectId

def create_book(book: Book):
    result = books_collection.insert_one(book.dict())
    return str(result.inserted_id)

def get_books():
    return list(books_collection.find({}, {"_id": 0, "title": 1, "author": 1}))

def get_book(title: str):
    return books_collection.find_one({"title": title}, {"_id": 0, "title": 1, "author": 1})

def update_book(title: str, author: str):
    books_collection.update_one({"title": title}, {"$set": {"author": author}})
    return get_book(title)

def delete_book(title: str):
    books_collection.delete_one({"title": title})
    return {"message": "Deleted"}