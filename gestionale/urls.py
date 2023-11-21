from django.urls import include, path

from . import views

urlpatterns = [


    path("test", views.index, name="index"),
    path("index2", views.index2, name="index2"),
    path("esami", views.index)
]