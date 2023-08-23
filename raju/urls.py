from django.urls import path

from raju import views


urlpatterns=[
    path('',views.index,name="index")
]