from datetime import datetime, timezone
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Categoria(Model):
    __tablename__="categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    imagen = Column(ImageColumn, nullable=True)
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    actualizado_en = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    
    productos = relationship(
        "Producto",
        back_populates="categoria"
    )
    
    def __repr__(self):
        return self.nombre
    
class Producto(Model):
    __tablename__="producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    imagen = Column(ImageColumn, nullable=True)
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    actualizado_en = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    categoria = relationship(
        "Categoria",
        back_populates="productos"
    )
    
    def __repr__(self):
        return self.nombre