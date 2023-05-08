from models import Base, User, Comment
from connect import engine


print("CREATING TABLES >>>> ")
Base.metadata.create_all(bind=engine)