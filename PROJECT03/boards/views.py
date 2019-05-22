from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    boards = Board.objects.all()
    return render(request, 'boards/index.html', {'boards' : boards})
    
def new(request):
    if request.method == 'POST':
        # create 수행
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        
        return redirect('boards:index')
    else:
        # new 페이지 보여줌
        return render(request, 'boards/new.html')