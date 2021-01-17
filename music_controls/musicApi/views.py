from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    """
    This function takes in a request and returns a response
    """
    return HttpResponse("<h1>Hello</h1>")

