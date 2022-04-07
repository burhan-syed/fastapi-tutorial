from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # , connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# without orm
# while True:
#     try:
#         conn = psycopg2.connect(
#             host='localhost', database='fastapi-tut', user='postgres', password='9987', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('db connected')
#         break
#     except Exception as error:
#         print('db connection failed')
#         print(error)
#         time.sleep(2)

# temp in memory db
# my_posts = [
#     {"title": "post 1",
#      "content": "post 1 content",
#      "id": 1},
#     {'title': 'post2', 'content': 'post2 content', 'id': 2},
# ]


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p


# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
