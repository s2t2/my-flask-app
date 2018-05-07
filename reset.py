from app import db

db.drop_all()

db.create_all()

print("THE DATABASE HAS BEEN RESET")
