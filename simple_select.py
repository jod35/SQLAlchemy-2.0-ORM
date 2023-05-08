from main import session
from models import User,Comment
from sqlalchemy import select


users = session.query(User).all()


for user in users:
    print(user) 
