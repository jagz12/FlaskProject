from app import db, Users, People

db.drop_all() 
db.create_all() 

testuser = Users(first_name='Bav', last_name='Singh')
testperson = People(first_name='Jane', last_name='Doe', height=2.1)
db.session.add(testperson)
db.session.add(testuser)
db.session.commit()