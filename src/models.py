import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base): 
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)  
    username = Column(String(25), nullable=False)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String(40), nullable=False)

class Planetas(Base):
    __tablename__='planetas'

    id = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(40))
    galaxia_planeta = Column(String(40))
    sistema_planeta = Column(String(40))

class Personajes(Base):
    __tablename__='personajes'

    id = Column(Integer, primary_key=True)
    nombre_personaje = Column(String(40))
    apellidos_personaje = Column(String(40))
    raza_personaje = Column(String(40)) 
    sexo_personaje = Column(String(40))
    bando_personaje = Column(String(40)) 


class Favoritos(Base):
    __tablename__ = 'favoritos'

    user_from_id = Column(Integer, ForeignKey('user.id'),primary_key=True)
    user_from_idRelationship = relationship(User)
    planeta_id = Column(String,ForeignKey('planetas.id')) 
    user_to_idRelationship = relationship(Planetas)
    personaje_id = Column(String,ForeignKey('personajes.id')) 
    personaje_idRelationship = relationship(Personajes)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
