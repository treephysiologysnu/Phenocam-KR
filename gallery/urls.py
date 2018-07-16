from django.urls import include, path
from gallery import views

urlpatterns = [
    path('', views.index, name='index'),
]