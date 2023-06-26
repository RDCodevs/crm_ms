from src.config.database import Base
from sqlalchemy import Column, Integer, String, Float, Date, Time

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
    address = Column(String)
    schedule_start = Column(Time) 
    schedule_end = Column(Time)
    experience = Column(Integer)    
    certifications = Column(Integer, nullable= True)