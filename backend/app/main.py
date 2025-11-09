from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud
from .schemas import ItemCreate, Item
from .database import SessionLocal, engine, Base

# DB テーブル作成（開発用。migrations は alembic を使う）
Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB セッション依存
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=Item)
def create_item_endpoint(item: ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item)

@app.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db, skip, limit)

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
