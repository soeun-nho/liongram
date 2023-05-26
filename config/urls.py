from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static

from posts.views import index,url_view,url_parameter_view,function_view,class_view,function_list_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("url/",url_view), 
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()),
    path('list/', function_list_view),
    
    path('', index, name='index'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('posts/', include('posts.urls', namespace='posts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)