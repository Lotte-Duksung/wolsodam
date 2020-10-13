from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

# Create your views here.
def main(requests):
    return render(requests, 'main.html')

def subscribe(requests):
    return render(requests, 'subscribe.html')

def subscribe2(requests):
    return render(requests, 'subscribe2.html')

def subscribe3(requests):
    return render(requests, 'subscribe3.html')

def subscribe4(requests):
    return render(requests, 'subscribe4.html')

def introduce(requests):
    return render(requests, 'introduce.html')

def QA(requests):
    return render(requests, 'QA.html')

def review(requests):
    return render(requests, 'review.html')

def product(requests):
    return render(requests, 'product.html')

def login(requests):
    if requests.method == 'POST':    # POST 방식으로 들어온 지 확인
        username = requests.POST['username'] # 사용자로부터 전달 받은 유저 이름을 넣음
        password = requests.POST['password'] # 사용자로부터 전달 받은 패스워드를 넣음
        user = auth.authenticate(requests, username=username, password=password) # 전달받은 변수를 유저 변수에 넣어줌
        if user is not None:    # 유저가 존재한다면
            auth.login(requests, user)   # 이 유저가 존재하므로 로그인 해줌 
            return redirect('main')     # 메인 페이지로 이동
        else:
            return render(requests, 'login.html')    # 존재하지 않으면 로그인 페이지에 남아있게됨
    else:        
        return render(requests, 'login.html')   # POST방식이 아닐 경우 로그인 페이지에 남아있게 됨

def signup(requests):
    if requests.method == "POST":    # 요청방식이 POST방식인지 확인
        if requests.POST['password1'] == requests.POST['password2']:   # 입력한 비밀번호와 비밀번호 확인 부분이 같은지 확인
            user = User.objects.create_user(    # 유저 생성하는 함수
                requests.POST['username'],   # 입력 받은 유저이름
                password = requests.POST['password1'],    # 입력 받은 패스워드
                email = requests.POST['email'],
                first_name = requests.POST['first_name'],
                last_name = requests.POST['last_name']
            )
            phone = requests.POST["phone"]  
            birth_date = requests.POST["birth_date"]
            profile = Profile(user=user, phone=phone, birth_date = birth_date)   #Profile 생성
            profile.save()  #Profile 저장
            auth.login(requests, user)   # 그 계정에 로그인을 하라는 요청을 다시 보냄
        return redirect('signup_complete')     # 메인으로 사용자가 갈 수 있게 리턴함
    return render(requests, 'signup.html')   # 요청 방식이 POST가 아니라면 회원가입 페이지에 머무름

def logout(requests):    #로그아웃에 대한 요청이 들어온다면, 
    if requests.method == 'POST':
        auth.logout(requests)    # auth.logout함수를 작동 => 로그아웃 진행됨
        return redirect('/') # 메인 페이지로 이동
    return render(requests, 'main.html')

def mypage(requests):
    return render(requests, 'mypage.html')

def signup_complete(requests):
    return render(requests, 'signup_complete.html')