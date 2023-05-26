from django.db import models
from django.contrib.auth import get_user_model

# 나중에 User 모델 새로 커스텀할 때 그대로 사용할 수 있는 방법
# 장고에서 사용하고 있는 User 모델 일단 쓰고.. 그걸 to ='User' 로 연결
User = get_user_model()
# Create your models here.

class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) #생성되면 자동으로 입력하게 하는 속성 auto_now..
    view_count = models.IntegerField(verbose_name='조회수', default=0) #처음은 0
    writer = models.ForeignKey(to =User, on_delete=models.CASCADE, null=True, blank=True)


#null = DB에 null 값 넣어줄 건지 blank = 유효성 검사? 
class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to = 'Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
