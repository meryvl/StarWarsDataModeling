import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    apellidos = Column(String(250))
    contraseña = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fecha_suscripcion = Column(String(250), nullable=False)

class Planeta(Base):
    __tablename__ = 'planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    descripcion = Column(String(250))
    population = Column(String(250))
    dimension = Column(String(250))
    atmósfera = Column(String(250))
    temperatura = Column(String(250))
    superficie = Column(String(250))

class Vehicles(Base): 
     __tablename__ = 'vehicles'
     id = Column(Integer, primary_key=True)


class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    descripcion = Column(String(250))
    height = Column(String(250))
    year= Column(String(250))
    kg = Column(String(250))
    birthdate = Column(String(250))
    planeta_id = Column(Integer, ForeignKey('planeta.id'))
    planeta = relationship(Planeta)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicles = relationship(Vehicles)




class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)


class FavoritosPersonaje(Base):
    __tablename__ = 'favorito_personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id')) 
    usuario = relationship(Personaje)
    favorito_id = Column(Integer, ForeignKey('favoritos.id')) 
    usuario = relationship(Favoritos)

class FavoritosPlaneta(Base):
    __tablename__ = 'favorito_planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id')) 
    planeta = relationship(Planeta)
    favorito_id = Column(Integer, ForeignKey('favoritos.id')) 
    usuario = relationship(Favoritos)

class Favoritosvehicle(Base):
    __tablename__ = 'favorito_vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id')) 
    vehicle = relationship(Vehicles)
    favorito_id = Column(Integer, ForeignKey('favoritos.id')) 
    usuario = relationship(Favoritos)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
