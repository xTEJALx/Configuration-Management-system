# app/models.py
from sqlalchemy import Column, Integer, String
from .database import Base

class Configuration(Base):
    __tablename__ = "configurations"

    id = Column(Integer, primary_key=True, index=True)
    country_code = Column(String, unique=True, index=True)
    business_name = Column(String, index=True)
    registration_number = Column(String, index=True)
    additional_details = Column(String)
