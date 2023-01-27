from django.urls import path
from . import views

# local host 8000

# this like app.use() in express
urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('finches/', views.FinchList.as_view(), name="finch_list"),
  path('finches/new/', views.FinchCreate.as_view(), name="finch_create"),
  path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
  path('finches/<int:pk>/update',views.FinchUpdate.as_view(), name="finch_update"),
  path('finches/<int:pk>/delete',views.FinchDelete.as_view(), name="finch_delete"),
  
]
