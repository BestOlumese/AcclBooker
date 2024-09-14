from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('today', views.today),
    path('completed', views.completed),
    path('uncompleted', views.uncompleted),
]