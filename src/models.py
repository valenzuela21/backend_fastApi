from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from src.utils.dbUtil import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String, default='user')
    is_active = Column(Boolean, default=False)
    created_on = Column(DateTime(timezone=False), default=datetime.now())
    updated_on = Column(DateTime(timezone=False), default=datetime.now())


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    rating = Column(Float, nullable=True)

    brand_id = Column(Integer, ForeignKey('brands.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    brand = relationship("Brand", back_populates="products")
    category = relationship("Category", back_populates="products")

    created_on = Column(DateTime(timezone=False), default=datetime.now)
    updated_on = Column(DateTime(timezone=False), default=datetime.now)


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="brand")  # Aquí 'Product' debe ser una cadena para que funcione

    created_on = Column(DateTime(timezone=False), default=datetime.now)
    updated_on = Column(DateTime(timezone=False), default=datetime.now)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products = relationship("Product", back_populates="category")  # Aquí 'Product' también es una cadena

    created_on = Column(DateTime(timezone=False), default=datetime.now)
    updated_on = Column(DateTime(timezone=False), default=datetime.now)
