from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    senha = Column(String, nullable=False)
    carrinho = Column(Text, nullable=True)
    create_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, nullable=True)


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    preco = Column(Integer, nullable=False)
    descricao = Column(String, nullable=False)
    create_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, nullable=True)


class Carrinho(Base):
    __tablename__ = 'carrinho'
    id = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    id_produto = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    qtd = Column(String, nullable=False)
    status = Column(Integer, nullable=False)
    create_at = Column(DateTime, nullable=False)
    update_at = Column(DateTime, nullable=True)

        # Define the relationships with Pessoa and Produto classes
    pessoa = relationship("Pessoa", back_populates="carrinhos")
    produto = relationship("Produto", back_populates="carrinhos")

# Add the reverse relationships to the Pessoa and Produto classes
Pessoa.carrinhos = relationship("Carrinho", back_populates="pessoa")
Produto.carrinhos = relationship("Carrinho", back_populates="produto")