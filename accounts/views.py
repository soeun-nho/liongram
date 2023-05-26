from django.shortcuts import render,redirect


from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, SignUpForm


# Create your views here.
def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == 'GET':
        form = SignUpForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        # POST 요청 시 데이터 확인 후 회원 생성
        form = SignUpForm(request.POST)

        if form.is_valid():
            #회원가입 처리
            instance = form.save() 
            return redirect('index')           
        else:
            #리다이렉트
            return redirect('accounts:signup')
        
