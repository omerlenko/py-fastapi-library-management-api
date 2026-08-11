from sqlalchemy import select
from sqlalchemy.orm import Session

import schemas
from db import models


def get_authors(db: Session) -> list[models.Author]:
    return list(db.scalars(select(models.Author)).all())

def get_author(db: Session, author_id: int) -> models.Author | None:
    return db.get(models.Author, author_id)

def create_author(db: Session, data: schemas.AuthorCreate) -> models.Author:
    author = models.Author(**data.model_dump())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_books(db: Session) -> list[models.Book]:
    return list(db.scalars(select(models.Book)).all())

def get_book(db: Session, book_id: int) -> models.Book | None:
    return db.get(models.Book, book_id)

def create_book(db: Session, data: schemas.BookCreate) -> models.Book | None:
    author = db.get(models.Author, data.author_id)
    if author is None:
        return None

    book = models.Book(**data.model_dump())
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
