from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    cart = Column(Text, nullable=True)
    create_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, nullable=True)

    carts = relationship("Cart", back_populates="client")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)
    create_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, nullable=True)

    carts = relationship("Cart", back_populates="product")


class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    id_client = Column(Integer, ForeignKey('clients.id'), nullable=False)
    id_product = Column(Integer, ForeignKey('products.id'), nullable=False)
    qt = Column(String, nullable=False)
    status = Column(Integer, nullable=False)
    create_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, nullable=True)

    client = relationship("Client", back_populates="carts")
    product = relationship("Product", back_populates="carts")
