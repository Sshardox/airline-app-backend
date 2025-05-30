from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database.session import Base

class Flight(Base):
    __tablename__ = "flights"


    id = Column(Integer, primary_key=True, autoincrement=True)
    departureDate = Column(DateTime)
    departureAirportCode = Column(String(15))
    departureAirportName = Column(String(50))
    departureCity = Column(String(50))
    departureLocale = Column(String(50))
    arrivalDate = Column(DateTime)
    arrivalAirportCode = Column(String(15))
    arrivalAirportName = Column(String(50))
    arrivalCity = Column(String(50))
    arrivalLocale = Column(String(50))
    ticketPrice = Column(Integer)
    ticketCurrency = Column(String(15))
    flightNumber = Column(Integer)
    seatCapacity = Column(Integer)

    booking = relationship("Booking", back_populates="flight")