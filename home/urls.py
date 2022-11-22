from django.urls import path
from .views import * 

app_name = 'home' 

urlpatterns = [
    path('', homepage, name='home'),
    path('who-we-are', aboutus, name='who-we-are'),
   
    path('start-a-project', StartAProject.as_view(), name='start-a-project'),
     path('thank-you', thankyou, name='thank-you'),
]