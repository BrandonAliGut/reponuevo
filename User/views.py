from django.shortcuts import render

def index(request):
    print("hello sisteme Malo")
    return render(request, 'index.html', {})