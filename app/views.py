from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return board(request)
    return 



def welcome(request):
    return render(request, 'app/welcome.html')
    

def board(request):
    context = {
        'items': []
    }
    return render(request, 'app/board.html', context)