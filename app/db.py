from sqlalchemy import create_engine
engine = create_engine('mysql://ODBC:@localhost:3306/invent_management', echo=False)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class UserRights(Base):
        __tablename__ = 'tbl_user_rights'

        right_id = Column(Integer, primary_key=True)
        right_name = Column(String(100))
       
        

        def __init__(self, right_name):
                self.name = right_name
                self.right_id = right_id
                
                

        def __repr__(self):
                return "<MyTable(%s )>" % (self.name)



class Add_asset(Base):
        __tablename__ = 'tbl_assets'

        assest_id = Column(Integer, primary_key=True)
        name = Column(String(100))
        serial = Column(String(100))
        andela_serial = Column(String(100))
        date_bought = Column(String(100))
        description = Column(String(100))
        avail = Column(String(100))
        

        def __init__(self, name, serial,andela_serial,date_bought,description,avail):
                self.name = name
                self.serial = serial
                self.andela_serial = andela_serial
                self.date_bought = date_bought
                self.description = description
                self.avail = avail
                

        def __repr__(self):
                return "<MyTable(%s,%s,%s,%s,%s)>" % (self.name, self.serial, self.andela_serial, self.date_bought, self.description, self.avail )


 
class Add_staff(Base):
    __tablename__ = 'tbl_staff'

    staff_id = Column(Integer, primary_key=True)
    f_name = Column(String(100))
    s_name = Column(String(100))
    username = Column(String(100))
    password = Column(String(100))
    email = Column(String(100))
    right_id =Column(String(100))
    department_id =Column(String(100))
    password=Column(String(100))
    

    def __init__(self, f_name, s_name,username,right_id, email,department_id,password):
           
            self.f_name = f_name
            self.s_name = s_name
            self.username = username
            self.department_id = department_id
            self.right_id = right_id
            self.email = email
            self.password = password

                        

    def __repr__(self):
            return "<MyTable(%s,%s,%s,%s,%s)>" % (self.f_name, self.s_name, self.username, self.right_id, self.email,self.department_id,self.password)

class Issue_asset(Base):
    __tablename__ = 'tbl_assets_transactions'

    transaction_id = Column(Integer, primary_key=True)
    asset_id = Column(String(100))
    staff_id = Column(String(100))
    admin_id = Column(String(100))
    date_borrowed = Column(String(100))
    date_returned =Column(String(100))
    status =Column(String(100))
    comment =Column(String(100))
    

    def __init__(self, staff_id,asset_id, admin_id,date_borrowed,date_returned,status,comment):
           
            self.asset_id = asset_id
            self.staff_id = staff_id
            self.admin_id = admin_id
            self.date_borrowed = date_borrowed
            self.date_returned = date_returned
            self.status = status
            self.comment = comment
            

    def __repr__(self):
            return "<MyTable( %s,%s,%s,%s,%s,%s,%s)>" % (self.staff_id,self.asset_id,  self.username, self.admin_id, self.date_borrowed, self.date_returned, self.status, self.comment)


class Department(Base):
    __tablename__ = 'tbl_department'

    department_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    
    def __init__(self, department_id,name):
            
           
            self.department_id = department_id
            self.name = name
           
            

    def __repr__(self):
            return "<MyTable(%s,%s)>" % (self.department_id,self.name)

