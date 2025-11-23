from fastapi import APIRouter,Depends, HTTPException
from app.repositories.items import create_item, get_items, get_item
from app.schemas.item import ItemCreate, Item
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, Engine, Base

# DB テーブル作成（開発用。migrations は alembic を使う）
Base.metadata.create_all(bind=Engine)

# DB セッション依存
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/items",
    tags=["items"],
)

@router.post("/", response_model=Item)
def create_item_endpoint(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.get("/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_items(db, skip, limit)

@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item