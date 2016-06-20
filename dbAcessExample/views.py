from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Log


def index(request):

    #this is where all the black magic ob business logic happends

    #get all the users
    users=User.objects.all()

    output=users[0].name + " " + str(users[0].birth_date)


    #get all logs of one user
    logs=Log.objects.filter(user=users[0])

    output=output+"<ul>"
    for log in logs:
        output=output+"<li>"+str(log.date) + " " + log.content

    output=output+"</ul>"

    #more queries https://docs.djangoproject.com/en/1.9/topics/db/queries/
    
    return HttpResponse(output)
# Create your views here.
