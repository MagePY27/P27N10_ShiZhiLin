from django.shortcuts import render
from django.http import HttpResponse,QueryDict
from django.shortcuts import render
from hello.models import User


def index(request):
    return render(request, 'hello/hello.html')

#将所有用户列出#
def list(request):
    user = User.objects.all()
    return render(request, 'hello/list.html', {'user':user})

#新增用户界面#
def add_view(request):
    return render(request, 'hello/add.html')

#新增用户后提交动作#
def add_submit(request):
    try:
        if request.method == "POST":
            data = QueryDict(request.body).dict()
            data.pop('csrfmiddlewaretoken')
            print(data)
            res = User.objects.get_or_create(**data)
            if res:
                res = 1
                return render(request,'hello/addResult.html',{'res':res})
    except:
        res = 0
        return render(request,'hello/addResult.html',{'res':res})

#更新用户界面#
def update_view(request,uid):
    print(request.method,uid)
    user = User.objects.get(id=uid)
    return render(request, 'hello/update.html',{'user':user})

#更新用户后提交动作#
def update(request,uid):
    print(uid)
    if request.method == "POST":
        data = QueryDict(request.body).dict()
        data.pop('csrfmiddlewaretoken')
        print(data)
        res = User.objects.filter(id=uid).update(**data)
    return render(request, 'hello/updateResult.html', {'res': res})

#删除用户动作#
def delete(request,uid):
    print("uid is:",uid)
    print(request.method)
    u = User.objects.get(id=uid)
    res = u.delete()
    return render(request, 'hello/deleteResult.html', {'res': res})

#查询用户界面#
def search_view(request):
    return render(request,'hello/search.html')

#查询用户后的提交动作#
def search(request):
    print("hello this is search function")
    print(request.body)
    if request.method == "POST":
        data = QueryDict(request.body).dict()
        print(request.method, data)
        data.pop('csrfmiddlewaretoken')
        #print(data)
        user = User.objects.filter(name__icontains = data.get('name'))
        print(user)
        return render(request, 'hello/searchResult.html',{'user': user})

