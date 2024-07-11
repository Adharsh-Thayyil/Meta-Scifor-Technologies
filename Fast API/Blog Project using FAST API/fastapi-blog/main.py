from fastapi import FastAPI, Depends, Request, Form
from sqlalchemy.orm import Session
from database import SessionLocal, engine, metadata
import crud
import models
import schemas
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

metadata.create_all(bind=engine)
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_posts(request: Request, db: Session = Depends(get_db)):
    posts = crud.get_posts(db)
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})

@app.post("/")
def create_posts(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    post = schemas.PostCreate(title=title, content=content)
    crud.create_post(db, post)
    return {"message": "Post created successfully"}
