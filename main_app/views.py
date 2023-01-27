from django.shortcuts import render

# view class handles requests
from django.views.generic.base import TemplateView
# from django.views import View

# A class to handle sending a type of request
from django.http import HttpResponse

# import models
from .models import Finch
# Create your views here

# # adds artist class for mock database data
# class Finch:
#   def __init__(self, name, bio):
#     self.name = name
#     self.bio = bio

# finches = [
#   Finch("Bird1", "Bird stuff"),
#   Finch("Bird2", "Bird stuff"),
#   Finch("Bird3", "Bird stuff"),
#   Finch("Bird4", "Bird stuff"),
#   Finch("Bird5", "Bird stuff"),
#   Finch("Bird6", "Bird stuff"),
#   Finch("Bird7", "Bird stuff"),
#   Finch("Bird8", "Bird stuff"),
# ]

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
  template_name = "home.html"
  # # Here we are adding a method that will be ran when we are dealing with a GET request
  # def get(self, request):
  #   # Here we are returning a generic response
  #   # This is similar to response.send() in express
  #   return HttpResponse("Spotify Home")



class About(TemplateView):
  template_name = "about.html"
  # # Here we are adding a method that will be ran when we are dealing with a GET request
  # def get(self, request):
  #   # Here we are returning a generic response
  #   # This is similar to response.send() in express
  #   return HttpResponse("Spotify About")


class FinchList(TemplateView):
  template_name = "finch_list.html"

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # to get the query parameter we have to acccess it in the request.GET dictionary object        
        name = self.request.GET.get("name")
        # If a query exists we will filter by name 
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param
            context["finches"] = Finch.objects.filter(name__icontains=name)
        else:
            context["finches"] = Finch.objects.all()
        return context
