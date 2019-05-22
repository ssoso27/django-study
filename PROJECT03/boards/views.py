from django.shortcuts import render
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards' : boards})