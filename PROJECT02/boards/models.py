from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def board_image_path(instance, filename):
    return f'boards/{instance.pk}번글/images/{filename}'

# Create your models here
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        upload_to = board_image_path, # 저장 경로 (/media/ 하위)
        processors = [ResizeToFill(200, 300)], # 처리할 작업 목록 (리사이즈)
        format = 'JPEG', # 파일 포맷
        options = {'quality': 90}, # 이미지 품질 (원본의 90%)
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '[' + str(self.id) + ']' + self.title + ':' + self.content
        
class Comment(models.Model):
    content = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'<Board({self.board_id}): Comment({self.id})>'