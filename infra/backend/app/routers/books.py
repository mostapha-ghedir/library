# app/routers/books.py
from fastapi import APIRouter
from app.crud import create_book, get_books
from app.models import Book

router = APIRouter(prefix="/books")

@router.post("/")
def add_book(book: Book):
    create_book(book)
    return {"message": "Book added successfully!"}

@router.get("/")
def list_books():
    return get_books()