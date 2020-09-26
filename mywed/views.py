from django.shortcuts import render , redirect
from django.http import HttpResponse
#from django.contrib.auth import authenticate
#from django.contrib.auth import login as login_id
#from django.contrib.auth.models import User
from .models import Question, Choice


def index(req):
    return render(req, "mywed/index.html")

def login(req):
    return render(req, "mywed/login.html")





def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'mywed/detail.html', { 'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
