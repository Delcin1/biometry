from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import Session, sessionmaker


engine = create_engine("postgresql://user:example@db/biometry")
engine.connect()


Base = declarative_base()


class BioData(Base):
    __tablename__ = 'bdata'
    id = Column(Integer, primary_key=True)
    frame = Column(Integer, nullable=False)
    objid = Column(Integer, nullable=False)
    leftcord = Column(Integer, nullable=False)
    topcord = Column(Integer, nullable=False)
    wcord = Column(Integer, nullable=False)
    hcord = Column(Integer, nullable=False)
    chance = Column(Float, nullable=False)


Base.metadata.create_all(engine)


def dbmodel(a, b, c, d, e, f, g):
    session = Session(bind=engine)

    c1 = BioData(
        frame=int(a),
        objid=int(b),
        leftcord=int(c),
        topcord=int(d),
        wcord=int(e),
        hcord=int(f),
        chance=float(g)
    )

    # print(c1.content)

    session.add(c1)

    # print(session.new)

    session.commit()

# print(session.query(Post).all())

# print(session.query(Post).count())


def delete_data():
    session = Session(bind=engine)
    BioData.__table__.drop(engine)
    #session.query.delete(synchronize_session='fetch')
    session.commit()
