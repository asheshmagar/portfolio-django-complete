from django.urls import path
from . import views


urlpatterns = [
    path('',views.workThree,name='work3')
]
