from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses/", response_model=schemas.Address)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    logger.info("create new record")
    return crud.create_address(db=db, address=address)


@app.get("/addresses/{id}", response_model=schemas.Address)
def read_address(id: int, db: Session = Depends(get_db)):
    db_address = crud.get_address(db, address_id=id)
    logger.info("retrieve record by id")
    if db_address is None:
        logger.error("id not found")
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@app.put("/addresses/{id}", response_model=schemas.Address)
def update_address(id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    db_address = crud.update_address(db, address_id=id, address=address)
    logger.info("update record by id")
    if db_address is None:
        logger.error("id not found")
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@app.delete("/addresses/{id}", response_model=schemas.Address)
def delete_address(id: int, db: Session = Depends(get_db)):
    db_address = crud.delete_address(db, address_id=id)
    logger.info("delete record by id")
    if db_address is None:
        logger.error("id not found")
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address
