from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

# الاتصال ب MongoDB
MONGO_URL = "mongodb://mongodb:27017/libraryDB"
client = AsyncIOMotorClient(MONGO_URL)
db = client.libraryDB

@app.get("/", response_class=HTMLResponse)
async def read_books(request: Request):
    books_cursor = db.books.find()
    books = await books_cursor.to_list(length=100)
    return templates.TemplateResponse("index.html", {"request": request, "books": books})

@app.get("/api/books")
async def api_books():
    books_cursor = db.books.find()
    books = await books_cursor.to_list(length=100)
    return books
