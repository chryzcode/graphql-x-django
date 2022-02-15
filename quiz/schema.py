import graphene
from graphene_django.types import DjangoObjectType
from graphene_django import DjangoListField
from .models import Category, Quizzes, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'name')

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id', 'title', 'category', 'quiz')

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ('title', 'quiz')

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('questions', 'answer_text')

class Query(graphene.ObjectType):
    
    # all_quizzes = DjangoListField(QuizzesType)
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())
    all_questions = graphene.Field(QuestionType, id=graphene.Int())

    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get(pk=id)

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)

    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)
    


schema = graphene.Schema(query=Query)