from src.config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date

class Medic(Base):
    __tablename__ = "medic"
    id_medic = Column(Integer, primary_key= True, autoincrement= True)
    cedula = Column(Integer)
    name = Column(String)
    lastname = Column(String)
    gender = Column(String)
    speciality = Column(String)
    phone = Column(Integer) 
    email = Column(String)
    medical_history = Column(String)
    address = Column(String)
    schedule = Column(Date) 
    experience = Column(String) 
    education = Column(String)      
    certifications = Column(String)
    consultation = Column(String)