from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric, Float, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import Session, sessionmaker






def dbmodel(a,b,c,d,e):
    engine = create_engine("postgresql://user:example@localhost/biometry")
    engine.connect()
    session = Session(bind=engine)

    Base = declarative_base()

    class BioData(Base):
       __tablename__ = 'bdata'
       id = Column(Integer, primary_key = True)
       frame = Column(Integer, nullable = False)
       objid = Column(Integer, nullable = False)
       fcord = Column(Integer, nullable = False)
       lcord = Column(Integer, nullable = False)
       chance = Column(Float, nullable = False)

    Base.metadata.create_all(engine)

    c1 = BioData(
       frame=int(a),
       objid=int(b),
       fcord=int(c),
       lcord=int(d),
       chance=float(e)
    )


    #print(c1.content)

    session.add(c1)

    #print(session.new)

    session.commit()

#print(session.query(Post).all())

#print(session.query(Post).count())