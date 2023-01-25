from django.shortcuts import render

# view class handles requests
from django.views.generic.base import TemplateView
# from django.views import View

# A class to handle sending a type of request
from django.http import HttpResponse
# Create your views here.

# adds artist class for mock database data
class Finch:
  def __init__(self, name, bio):
    self.name = name
    self.bio = bio

finches = [
  Finch("Bird", "Bird stuff"),
]

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
    context["finches"] = finches # this is where we add the key into our context object for the view to use
    return context