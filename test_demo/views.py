import json

from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse


# Create your views here.
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)


def index(request):
    return render(request, 'index.html', '您还未登录！')


# 搜索的表单
def search_form(request):
    return render_to_response('search_form.html')


# 搜索的业务逻辑处理代码
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


def login_pages(requests):
    return render(requests, 'login.html')


def login_pages2(requests):
    return render(requests, 'login2.html')


# 登录
def login(request):
    request.encoding = 'utf-8'
    if 'username' in request.POST and request.POST['username']:
        input_name = request.POST['username']
        input_password = request.POST['password2']
        input_verify_code = request.POST['verify_code2']

        if input_name == 'aaa' and input_password == '123456' and input_verify_code == '1234':
            output_name = "欢迎您111：" + input_name
            return render(request, 'index.html', {"data": output_name})

    return render(request, 'index.html', {"data": "系统繁忙，请稍后重试！"})


def login2(request):
    request.encoding = 'utf-8'
    if 'name' in request.POST and request.POST['name']:
        input_name = request.POST['name']
        input_password = request.POST['password']
        input_verify_code = request.POST['verify_code']

        if input_name == 'aaa' and input_password == '123456' and input_verify_code == '1234':
            output_name = "欢迎：" + input_name
            return HttpResponse(json.dumps({"code2": 1, "data2": output_name}))

    return HttpResponse(json.dumps({"code": 1, "data": "系统繁忙，请稍后重试！"}))
