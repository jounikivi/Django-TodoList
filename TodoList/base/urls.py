from django.urls import path
#from .import views
from .views import *


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
]
