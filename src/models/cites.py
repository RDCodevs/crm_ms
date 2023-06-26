from src.config.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.models.pacients import Pacient
from src.models.medic import Medic
from sqlalchemy.sql import func

class Cites(Base):
    __tablename__ = "cites"

    id_cite = Column(Integer, primary_key= True, autoincrement= True)
    query_type = Column(String)
    query_description = Column(String)
    site = Column(String)
    number_cite = Column(String) #
    consulting_room = Column(String)
    horary = Column(DateTime)
    id_pacient = Column(Integer, ForeignKey(Pacient.id_pacient))
    pacient = relationship('Pacient', foreign_keys='Cites.id_pacient')

    id_medic = Column(Integer, ForeignKey(Medic.id_medic))
    medic = relationship('Medic', foreign_keys='Cites.id_medic')
    
    state = Column(String)
    admin = Column(Integer, nullable= True)
    assistant = Column(Integer, nullable= True)
    observations = Column(Text)
    reminder_sent = Column(Boolean)
    register_by = Column(Integer, nullable= True)
    created_date = Column(DateTime, server_default= func.now(), nullable= False)