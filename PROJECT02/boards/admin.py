from django.contrib import admin
from .models import Board, Comment
# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display =('title', 'content', 'image', 'created_at', 'updated_at',)

admin.site.register(Board, BoardAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at')
    
admin.site.register(Comment, CommentAdmin)