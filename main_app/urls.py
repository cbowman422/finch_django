from django.urls import path
from . import views

# local host 8000

# this like app.use() in express
urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('finches/', views.FinchList.as_view(), name="finch_list"),
]
