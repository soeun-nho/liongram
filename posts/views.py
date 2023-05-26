from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post

def url_view(request):
    print('url_view')
    #data = {'code': '001', 'msg': 'ok'}
    return HttpResponse('<h1>url_view</h1>')
    #return JsonResponse(data)

def url_parameter_view(request,username):
    print('user_parameter_view()')
    print(username)
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == 'GET':
         print(f'request.GET: {request.GET}')
    elif (request.method=='POST'):
        print(f'request.GET: {request.POST}')
    return render(request, 'view.html')

class class_view(ListView):
    model =Post
    template_name = 'cbv_view.html'

def function_list_view(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html', {'object_list': object_list})

#인덱스 페이지
def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context = {
        'post_list': post_list,
    }
    return render(request, "index.html",context)

#templates 다음 posts부터
def post_list_view(request):
    post_list = Post.objects.all()
    #post_list = Post.objects.filter(writer=request.user) #Post.writer가 현재 로그인인 것만 조회
    context = {
        'post_list': post_list,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request,id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, "posts/post_detail.html", context)

def post_create_view(request):
    if request.method=="GET":
        return render(request, "posts/post_form.html")
    else:
        image = request.FILES.get('image')
        content=request.POST.get("content")
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content
        )
        return redirect('index')

def post_update_view(request,id):
    return render(request, "posts/post_form.html")

def post_delete_view(request,id):
    return render(request, "posts/post_confirm_delete.html")

