from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text

Base = declarative_base()


class Pagina_models(Base):
    __tablename__ = "paginas"
    __table_args__ = {"schema": "projeto_de_bloco_tp5"}

    id_pagina = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    titulo = Column(String(255), nullable=False)
    data_hora = Column(DateTime, nullable=False)
    status_code = Column(Integer, nullable=True)
    sucesso = Column(Boolean, nullable=False, default=True)

    estados = relationship("Estado_models", back_populates="pagina")


class Estado_models(Base):
    __tablename__ = "estados"
    __table_args__ = {"schema": "projeto_de_bloco_tp5"}

    id_estado = Column(Integer, primary_key=True, autoincrement=True)
    pagina_id = Column(
        Integer,
        ForeignKey("projeto_de_bloco_tp5.paginas.id_pagina"),
        nullable=False,
    )
    nome = Column(String(100), nullable=False)
    sigla = Column(String(5), nullable=False)
    capital = Column(String(100), nullable=False)

    pagina = relationship("Pagina_models", back_populates="estados")


class ErroScraping_models(Base):
    __tablename__ = "erros_scraping"
    __table_args__ = {"schema": "projeto_de_bloco_tp5"}

    id_erro = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255), nullable=False)
    mensagem = Column(Text, nullable=False)
    data_hora = Column(DateTime, nullable=False)
