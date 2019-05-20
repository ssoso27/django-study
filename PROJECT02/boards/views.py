from django.shortcuts import render, redirect
from .models import Board
from IPython import embed
# Create your views here.
def index(request):
    # boards = Board.objects.all()
    # boards = Board.objects.order_by('-id')
    boards = Board.objects.all()[::1]
    return render(request, 'boards/index.html', {'boards' : boards})
    
# def new(request):
#     return render(request, 'boards/new.html')

def new(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)
    else:
        return render(request, 'boards/new.html')
    
# def create(request):
#     # request : QueryDict 형태.
#     # GET 쿼리 가져옴
#     # title = request.GET.get('title')
#     # content = request.GET.get('content')
    
#     # POST body 가져옴
#     title = request.POST.get('title')
#     content = request.POST.get('content')
    
#     # db 조작 (by. Model)
#     board = Board(title=title, content=content) 
#     board.save()
    
#     # return render(request, 'boards/create.html')
#     return redirect(f'/boards/{board.pk}/')
    
def detail(request, pk):
    board = Board.objects.get(pk = pk)
    
    return render(request, 'boards/detail.html', {'board' : board})
    
def delete(request, pk):
    board = Board.objects.get(pk = pk)
    board.delete()
    return redirect('/boards/')
    
# def edit(request, pk):
#     board = Board.objects.get(pk = pk)
#     return render(request, 'boards/edit.html', {'board' : board})
    
# def update(request, pk):
#     board = Board.objects.get(pk = pk)
#     title = request.POST.get('title')
#     content = request.POST.get('content')
    
#     board.title = title
#     board.content = content
#     board.save()
    
#     return redirect('boards:detail', board.pk)
    
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == 'POST':
        # update
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        board.title = title
        board.content = content
        board.save()
        
        return redirect('boards:detail', board.pk)
    else :
        # edit
        return render(request, 'boards/edit.html', {'board': board})