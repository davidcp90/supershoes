from django.shortcuts import render

def home(request):
    data = {}
    data['title']='Home'
    return render(request, 'home.html', data)
