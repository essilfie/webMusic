from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    """
    This function here will return a response
    """
    return HttpResponse("Hello")

