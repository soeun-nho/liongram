from django.contrib import admin
from .models import Post, Comment

# Register your models here.
#admin 사이트에서 코드 출력 가능하게 함
#데이터 CRUD 가능하게


class CommentInLine(admin.TabularInline):
    model=Comment
    extra=3
    min_num=3
    max_num=5
    verbose_name='댓글'
    verbose_name_plural ='댓글 '
    

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('id','image', 'content', 'created_at', 'view_count', 'writer')
    #list_editable=('content',)
    list_filter =['created_at']
    search_fields = ('id','writer__username')
    search_help_text='게시판 번호, 작성자 검색이 가능합니다. '
    inlines=[CommentInLine]

#admin.site.register(Comment)
