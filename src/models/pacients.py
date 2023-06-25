from src.config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Pacient(Base):
    __tablename__ = "pacients"

    id_pacient = Column(Integer, primary_key= True, autoincrement= True)
    name = Column(String)
    lastname = Column(String)
    gender = Column(String)
    weight = Column(Float)
    height = Column(Float)
    ethnicity = Column(String)
    allergies = Column(String)
    HTA = Column(Integer) 
    cie_code = Column(Integer) 
    birthday = Column(Date)      
    blood_type = Column(String)
    address = Column(String)
    phone = Column(Integer) 