from django.shortcuts import render

# view class handles requests
from django.views.generic.base import TemplateView
# from django.views import View

# A class to handle sending a type of request
from django.http import HttpResponse

# import models
from .models import Finch

from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

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
            context["finches"] = Finch.objects.filter(name__icontains=name)
            # We add a header context that includes the search param
            context["header"] = f"Searching for {name}"
        else:
            context["finches"] = Finch.objects.all()
            # default header for not searching 
            context["header"] = "Trending Artists"
        return context




class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'img', 'bio', 'verified_finch']
    template_name = "finch_create.html"
    # this will get the pk from the route and redirect to finch view
    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})

    
class FinchDetail(DetailView):
    model = Finch
    template_name = "finch_detail.html"


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'img', 'bio', 'verified_finch']
    template_name = "finch_update.html"

    def get_success_url(self):
        return reverse('finch_detail', kwargs={'pk': self.object.pk})


class FinchDelete(DeleteView):
    model = Finch
    template_name = "finch_delete_confirmation.html"
    success_url = "/finches/"