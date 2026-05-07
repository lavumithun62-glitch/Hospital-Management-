from sqlalchemy import Column, Integer, String
from app.database.db import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)
    doctor_name = Column(String)
    patient_name = Column(String)
    appointment_date = Column(String)
    appointment_time = Column(String)
    status = Column(String, default="Pending")
