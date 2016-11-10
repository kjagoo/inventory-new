from sqlalchemy import create_engine
engine = create_engine('mysql://ODBC:@localhost:3306/invent_management', echo=False)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
class Add_asset(Base):
        __tablename__ = 'tbl_assets'

        assets_id = Column(Integer, primary_key=True)
        name = Column(String(100))
        serial = Column(String(100))
        andela_serial = Column(String(100))
        date_bought = Column(String(100))
        description = Column(String(100))
        

        def __init__(self, name, serial,andela_serial,date_bought,description):
                self.name = name
                self.serial = serial
                self.andela_serial = andela_serial
                self.date_bought = date_bought
                self.description = description
                

        def __repr__(self):
                return "<MyTable((%s, %s,%s,%s,%s)>" % (self.name, self.serial, self.andela_serial, self.date_bought, self.description)



new_record = Add_asset('Genius', 'me','100','2016-09-08','new')
session.add(new_record)
session.commit()
