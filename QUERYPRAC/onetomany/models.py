from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.name}'
        
class Board(models.Model):
    title = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 해당 유저가 지워지면, 모든 게시글들이 삭제됨
    
    def __str__(self):
        return f'{self.title}'
        
class Comment(models.Model):
    content = models.CharField(max_length=20)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 해당 유저가 지워지면, 모든 게시글들이 삭제됨
    
    def __str__(self):
        return f'{self.content}'