from django.urls import path
from . import views

urlpatterns = [
    path('',views.workOne,name='work1')
]
