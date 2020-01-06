from django.urls import path
from . import views


urlpatterns = [
    path('',views.workTwo,name='work2')
]
