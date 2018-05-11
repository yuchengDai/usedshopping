from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from hashlib import sha1
from django.http import JsonResponse
from user.models import UserAccount



# Create your views here.
def register(request):
    # return HttpResponse('注册')
    return render(request,'register.html')

#注册处理
def handle_register(request):
    if request.method == 'POST':
        error_msg=''
        post = request.POST
        uname = post.get('username')
        upwd1 = post.get('password1')
        upwd2 =  post.get('password2')
        if upwd2 != upwd1:
            error_msg="两次密码不一致,请重新输入"
            return render(request,'register.html',{ 'error_msg':error_msg})
            # return HttpResponse('两次密码不一致')
        s1 = sha1()
        s1.update(upwd1.encode('utf-8'))
        upwd = s1.hexdigest()

        user = User()
        user.user_name = uname
        user.user_password = upwd 
        user.save()
        # user1 = UserAccount()
        # user1.user_id
        # return HttpResponse('注册成功')
        return render(request,'login.html')

def my_login_required(view_function):
    def wrap(request, *args, **kwargs):
        # check session
        if 'uid' not in request.session.keys():
            return redirect(my_login) 
        return view_function(request,*args,**kwargs)
    return wrap

def my_login(request):
    if request.method=='POST':
        error_msg=''
        user = UserAccount()
        post = request.POST 
        uname = post.get('username')
        upwd = post.get('password')
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        upwd1 = s1.hexdigest()
        member = User.objects.filter(user_name=uname,user_password=upwd1).first()
        # print(member)
        # for i in member:
        #     print(i)
        if member is not None:
            request.session['uid'] = member.id
            print(user.user_id)     
            return render(request,'index.html')
            # return HttpResponse('登录成功')
        error_msg = '用户名或密码错误'
        return render(request,'login.html',{ 'error_msg':error_msg })
    return render(request,"login.html")
# @my_login_required
def Userinfo(request):
    # print(request.session['uid'])
    if request.method == 'GET':
        # print(UserAccount.objects.get(user_id=request.session['uid']))
        # if UserAccount.objects.get(user_id=request.session['uid']) is None:
        # print('rugjgj')
        user = UserAccount.objects.all()
        print(user[1])
        if str(request.session['uid']) not in str(user):
            user = UserAccount()
            user.user_id = request.session['uid']
            user.save()
        # print('rugjgj')
        users = UserAccount.objects.filter(user_id=request.session['uid'])
        return render(request,'userinfo.html',{'users':users})
        # return render(request,'userinfo.html')
    if request.method=='POST':
        user = UserAccount.objects.get(user_id=request.session['uid'])
        # print(user.user_id)
        # user = UserAccount()

        post = request.POST
        user.ushou = post.get('ushou')
        # print(user.ushou)
        user.uname = post.get('uname')
        user.uphone = post.get('uphone')
        user.upost = post.get('upost')
        user.save()
        users = UserAccount.objects.filter(user_id=request.session['uid'])
        
        return render(request,'userinfo.html',{'users':users})
    return render(request,'userinfo.html')
def update(request):
    if request.method =='POST':
        mes = ''
        user = User.objects.get(id=request.session['uid'])
        user.user_password = request.POST.get('password')
        user.user_name =request.POST.get('username')
        s1 = sha1()
        s1.update(user.user_password.encode('utf-8'))
        user.user_password = s1.hexdigest()
        user.save()
        mes = '修改成功'
        return render(request,'update.html',{'mes':mes})
    return render(request,'update.html')


    



