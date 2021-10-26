from django.shortcuts import render, HttpResponse

# Create your views here.
def taskList(request):
    return HttpResponse('Todo List')