from django.urls import path
from . import views


urlpatterns = [
    path('',views.Contact.as_view(),name='contact'),
    path('success',views.Contact.as_view(),name='success')
    
]
