from rest_framework.response import Response
from rest_framework.decorators import api_view
from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

@api_view(['GET'])
def getData(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()

    questionSerializer = QuestionSerializer(questions, many = True)
    choiceSerializer = ChoiceSerializer(choices, many = True)
    return Response({'question': questionSerializer.data, 'choice': choiceSerializer.data})