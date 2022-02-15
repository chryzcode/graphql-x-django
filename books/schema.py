import graphene
from graphene_django.types import DjangoObjectType
from .models import Books

class BookType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ('id', 'title', 'excerpt')

class Query (graphene.ObjectType):
    all_books = graphene.List(BookType)

schema = graphene.Schema(query=Query)