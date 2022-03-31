import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(50)) 
    mass = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    homeworld = Column(String(50))
    url = Column(String(50))
    description = Column(String(50))
    _id = Column(String(50))

class Planets(Base):
    __tablename__ = 'planets'
    uid = Column(Integer, primary_key=True)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    surface_water = Column(String(50))
    name = Column(String(50))
    url = Column(String(50))
    description = Column(String(50))
    _id = Column(String(50))
    characters_uid = Column(Integer, ForeignKey('characters.id'))
    characters = relationship(Characters)

class Starships(Base):
    __tablename__ = 'starships'
    uid = Column(Integer, primary_key=True)
    model = Column(String(50))
    starship_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(String(50))
    length = Column(String(50))
    crew = Column(String(50))
    passengers = Column(String(50))
    max_atmosphering_speed = Column(String(50))
    hyperdrive_rating = Column(String(50))
    MGLT = Column(String(50))
    cargo_capacity = Column(String(50))
    consumables = Column(String(50))
    name = Column(String(50))
    url = Column(String(50))
    description = Column(String(50))
    _id = Column(String(50))

class Pilots(Base):
    __tablename__ = "pilots"
    pilot_uid = Column(Integer, primary_key=True)
    pilot_name = Column(String(50), ForeignKey('characters.id'))
    characters = relationship(Characters)
    starship_name = Column(String(50), ForeignKey('starships.id'))
    starships = relationship(Starships)

class FavoritesChar(Base):
    __tablename__ = "favoritesChar"
    Fav_Charact = Column(String(50), ForeignKey('characters.id'), primary_key=True)
    Name_charact = Column(String(50), ForeignKey('characters.name'))
    characters = relationship(Characters)

class FavoritesPlan(Base):
    __tablename__ = "favoritesPlan"
    Fav_Planets = Column(String(50), ForeignKey('planets.id'), primary_key=True)
    Name_planet = Column(String(50), ForeignKey('planets.name'))
    planets = relationship(Planets)

class FavoritesStar(Base):
    __tablename__ = "favoritesStar"
    Fav_Starships = Column(String(50), ForeignKey('starships.id'), primary_key=True)
    Name_Starship = Column(String(50), ForeignKey('starships.name'))
    starships = relationship(Starships)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')