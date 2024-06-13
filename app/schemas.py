# app/schemas.py
from pydantic import BaseModel

class ConfigurationBase(BaseModel):
    country_code: str
    business_name: str
    registration_number: str
    additional_details: str

class ConfigurationCreate(ConfigurationBase):
    pass

class ConfigurationUpdate(ConfigurationBase):
    pass

class Configuration(ConfigurationBase):
    id: int

    class Config:
        orm_mode = True
