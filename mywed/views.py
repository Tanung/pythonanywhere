from django.shortcuts import render , redirect
#from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from .models import Animal_Type, Animal


def index(req):
    return render(req, "mywed/index.html")


def login_user(req):
    if req.method == 'POST':
        user = User.objects.get(username=req.POST['username'])
        user = authenticate(username=user.username, password=req.POST['password'])
        if user:
            login(req, user)
            return redirect('/')

        else:
            return render(req, 'mywed/login.html')

    else:
        return render(req, 'mywed/login.html')

def logout_user(req):
    logout(req)
    return redirect('/')

def register(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect("/")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

    form = UserCreationForm
    return render(req, "mywed/register.html", context={"form":form})



#def detail(request, question_id):
#    question = Question.objects.get(id=question_id)
#    choices = Choice.objects.filter(question=question)
#    return render(request, 'mywed/detail.html', { 'question': question, 'choices': choices})

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
