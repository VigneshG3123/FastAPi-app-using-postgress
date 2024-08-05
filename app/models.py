from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, index=True)
    choices = relationship("Choice", back_populates="question")

class Choice(Base):
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship("Question", back_populates="choices")
