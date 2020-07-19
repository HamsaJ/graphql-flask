from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from . import models
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    Post = models.Post
    User = models.User

    # Create the fixtures
    # Add users
    Jama = User(username="Jama001", password="pasword1")
    db_session.add(Jama)
    Ali = User(username="Ali001", password="pasword1")
    db_session.add(Ali)
    Mohammed = User(username="Mohammed001", password="pasword1")
    db_session.add(Mohammed)

    # Add posts
    post1 = Post(author_id=1, title="test", body="Hello world from Jama")
    db_session.add(post1)
    post2 = Post(author_id=3, title="test", body="Hello world from Mohammed")
    db_session.add(post2)
    post3 = Post(author_id=2, title="test", body="Hello world from Ali")
    db_session.add(post3)

    db_session.commit()

def get_db_session():
    return db_session