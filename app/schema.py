from . import models

import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = models.User
        interfaces = (relay.Node, )


class Post(SQLAlchemyObjectType):
    class Meta:
        model = models.Post
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allow only single column sorting
    all_posts = SQLAlchemyConnectionField(
        Post.connection, sort=Post.sort_argument())
    # Allows sorting over multiple columns, by default over the primary key
    all_user = SQLAlchemyConnectionField(User.connection)

schema = graphene.Schema(query=Query)