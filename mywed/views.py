from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
# Create your views here.
#def index(req):
    #return render(req, "mywed/index.html")

#def united(req):
    #return render(req, "mywed/united.html")

def Homepage(req):
    return render(req, "mywed/Homepage.html")

def History(req):
    return render(req, "mywed/History.html")
def h1(req):
    return render(req, "mywed/h1.html")
def h2(req):
    return render(req, "mywed/h2.html")
def h3(req):
    return render(req, "mywed/h3.html")
def h4(req):
    return render(req, "mywed/h4.html")
def h5(req):
    return render(req, "mywed/h5.html")

def Culture(req):
    return render(req, "mywed/Culture.html")
def c1(req):
    return render(req, "mywed/c1.html")
def c2(req):
    return render(req, "mywed/c2.html")
def c3(req):
    return render(req, "mywed/c3.html")
def c4(req):
    return render(req, "mywed/c4.html")

def Planet(req):
    return render(req, "mywed/Planet.html")

def Science(req):
    return render(req, "mywed/Science.html")

def Communities(req):
    return render(req, "mywed/Communities.html")

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return render(request, 'mywed/detail.html', { 'question': question, 'choices': choices})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)