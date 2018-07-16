from django.urls import include, path
from sites import views

urlpatterns = [
    path('<site_name>/', views.index, name='index'),
]