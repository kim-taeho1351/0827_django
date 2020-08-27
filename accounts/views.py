from django.shortcuts import render, redirect # return값 redircet 추가 
from django.contrib.auth.models import User # User model 연결 
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
    # POST method 요청이 들어올때
        if request.POST['password1'] == request.POST['password2']:
        # 입력한 password1과 password2가 만약 같으면
            User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            # 새로운 회원을 만들고
        return redirect('index')
        # index로 돌아간다. 
    return render(request, 'signup.html')
    # 위의 경우가 아닐때 그냥 signup페이지를 다시 리턴한다. 
    
def login(request):
    if request.method == 'POST':
    # POST method 요청이 들어올떄 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 입력받은 아이디와 비밀번호가 데이터베이스에 있는지 확인한다. 
        if user is not None:
        # 해당 데이터의 유저가 있다면 
            auth.login(request, user)
            return redirect('index')
            # 로그인하고 index로 리다이렉트한다.
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
            # 없다면, 에러를 표시하고, login페이지 로 이동(새로고침)
    else:
        return render(request, 'login.html')
        # POST 요청이 아닐경우 login 페이지 새로고침

def logout(request):
    auth.logout(request)
    return redirect('index')

def userpage(request):
    if request.user.is_authenticated:
        return render(request, 'userpage.html')
    else:
        return render(request, 'index.html', {'error': 'Only site member can accesss userpage'})
