from config.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Petition_Status(Base):

    __tablename__ = 'petition_status'

    petition_id = Column(Integer, ForeignKey('petition.petition_id'), nullable=False)
    petition_status = Column(Boolean, nullable=False)

    petition = relationship("Petition", back_populates="petition_status")