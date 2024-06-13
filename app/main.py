# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .database import Base, engine, get_db
from . import models, schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/create_configuration/", response_model=schemas.Configuration)
def create_configuration(configuration: schemas.ConfigurationCreate, db: Session = Depends(get_db)):
    db_configuration = models.Configuration(**configuration.dict(exclude_unset=True))
    db.add(db_configuration)
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

@app.get("/get_configuration/{country_code}", response_model=schemas.Configuration)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return db_configuration

@app.post("/update_configuration/", response_model=schemas.Configuration)
def update_configuration(configuration: schemas.ConfigurationUpdate, db: Session = Depends(get_db)):
    db_configuration = db.query(models.Configuration).filter(models.Configuration.country_code == configuration.country_code).first()
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    for var, value in vars(configuration).items():
        setattr(db_configuration, var, value) if value else None
    db.commit()
    db.refresh(db_configuration)
    return db_configuration

@app.delete("/delete_configuration/{country_code}", response_model=schemas.Configuration)
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_configuration = db.query(models.Configuration).filter(models.Configuration.country_code == country_code).first()
    if db_configuration is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    db.delete(db_configuration)
    db.commit()
    return db_configuration
