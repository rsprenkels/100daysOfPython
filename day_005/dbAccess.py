'''
Created on 28 apr. 2018

@author: Ron
'''

from sqlalchemy import create_engine, select, MetaData, Table

class User:
    def __init__(self, name, age, city):
        self.name  = name
        self.age   = age
        self.city  = city
        

engine = create_engine('mysql+pymysql://ron:pass@localhost:3306/python')
connection = engine.connect()
metadata = MetaData()
userTable = Table('user', metadata, autoload=True, autoload_with=engine)

print([c.name for c in userTable.columns])

def runQuery():
    resProxy = connection.execute("select name, age from user")
    results = resProxy.fetchall()
    print('users:')
    for user in results:
        print('{:>10} {}'.format(user.name, user.age))

def insertUser():
    ins = userTable.insert().values(name='Bart', age=20, city='Enschede')
    print('inserting user')
    connection.execute(ins)
    
def insert(thisUser):
    ins = userTable.insert().values(
        name=thisUser.name,
        age=thisUser.age,
        city=thisUser.city)
    print('inserting user ' + thisUser.name)
    connection.execute(ins)
    

def deleteUser(thisUser):
    connection.execute(userTable.delete().where(userTable.c.name == thisUser.name))

bart = User('Bart', 20, 'Enschede')
runQuery()
insert(bart)
runQuery()
deleteUser(bart)
runQuery()

