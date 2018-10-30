from django.shortcuts import render
from django.http import HttpResponse
from app_one.models import User


def index(requests):
    return HttpResponse ("Hello world!")


def help(requests):
    user_list=User.objects.order_by('First_name')
    user_dict={'User_rec':user_list}
    return render(requests,"index.html",context=user_dict)


