from sqlalchemy.orm import Session
import models, schemas

def get_posts(db: Session):
    return db.query(models.Post).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

