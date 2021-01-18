from django.urls import path
from .views import index

# this is where the main url is stored
urlpatterns = [
    path('', index)
]
