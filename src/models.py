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

    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    apellidos = Column(String(250))
    contraseña = Column(String(250))
    email = Column(String(250), nullable=False)
    fecha_suscripcion = Column(String(250))

class Planeta(Base):
    __tablename__ = 'planeta'
  
    id = Column(Integer, primary_key=True)
    name = Column(String(250),nullable=False)
    descripcion = Column(String(250))
    population = Column(String(250))
    Diameter = Column(String(250))
    atmósfera = Column(String(250))
    temperatura = Column(String(250))
    superficie = Column(String(250))
    Orbital_period =Column(String(250))
    Surface_water =Column(String(250))


class Vehicles(Base): 
     __tablename__ = 'vehicles'
     id = Column(Integer, primary_key=True)
     name = Column(String(250),nullable=False)
     Model = Column(String(250))
     cargo_capacity= Column(String(250))
     consumables=Column(String(250))
     Cost_in_credits=Column(String(250))
     Created= Column(String(250))
     Manufacturer= Column(String(250))
     Length= Column(String(250))
     Max_atmosphering_speed= Column(String(250))
     Passengers= Column(String(250))
     Vehicle_classe= Column(String(250))


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
   
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)


class FavoritosPersonaje(Base):
    __tablename__ = 'favorito_personaje'
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id')) 
    usuario = relationship(Personaje)
    favorito_id = Column(Integer, ForeignKey('favoritos.id')) 
    usuario = relationship(Favoritos)

class FavoritosPlaneta(Base):
    __tablename__ = 'favorito_planeta'

    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('planeta.id')) 
    planeta = relationship(Planeta)
    favorito_id = Column(Integer, ForeignKey('favoritos.id')) 
    usuario = relationship(Favoritos)

class Favoritosvehicle(Base):
    __tablename__ = 'favorito_vehicle'
   
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id')) 
    vehicle = relationship(Vehicles)
    favorito_id = Column(Integer, ForeignKey('favoritos.id')) 
    usuario = relationship(Favoritos)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
