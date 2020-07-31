from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req, "mywed/index.html")

def united(req):
    return render(req, "mywed/united.html")

def detail(request, question_id):
    return render(request, 'mywed/detail.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)