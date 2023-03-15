from datetime import datetime

from sqlalchemy import Integer, Column, String, Double, DateTime

from main import db


class Expense(db.Model):
    __tablename__ = 'expense'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    amount = Column(Double, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)
