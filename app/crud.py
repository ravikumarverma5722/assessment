from sqlalchemy.orm import Session
from .models import Address
from .schemas import AddressCreate, AddressUpdate


def get_address(db: Session, address_id: int):
    return db.query(Address).filter(Address.id == address_id).first()


def create_address(db: Session, address: AddressCreate):
    db_address = Address(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address


def update_address(db: Session, address_id: int, address: AddressUpdate):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address:
        for var, value in vars(address).items():
            setattr(db_address, var, value) if value else None
        db.commit()
        db.refresh(db_address)
    return db_address


def delete_address(db: Session, address_id: int):
    db_address = db.query(Address).filter(Address.id == address_id).first()
    if db_address:
        db.delete(db_address)
        db.commit()
        return db_address
