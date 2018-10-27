from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    print(request.POST.get('gender'))
    print(request.POST.getlist('favor'))
    print(request.POST.getlist('city'))
    obj=request.FILES.get('file')
    import os
    a=os.path.join('upload',obj.name)
    f=open(a,mode='wb')
    for i in obj.chunks():
        f.write(i)
    return render(request,'index.html')

from  django.views import View
class Home(View):

    def dispatch(self, request, *args, **kwargs):
        print(1)
        obj=super(Home,self).dispatch(request,*args,**kwargs)
        print(2)
        return obj

    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):
        print(request.method)
        return render(request,'home.html')

def index2(request):


    return render(request,"index2.html",{"user_dict":USER_DICT})


USER_DICT={
    "1":{"name":"root1","email":"1@qq.com"},
    "2":{"name":"root2","email":"2@qq.com"},
    "3":{"name":"root3","email":"3@qq.com"},
}
def detail(request,*args,**kwargs):
    # user=USER_DICT[nid]
    print(args,kwargs)
    # return render(request,'detail.html',{"user":user})
    return HttpResponse(1)

def login(request):
    return HttpResponse("cmdb")

from cmdb import models
def orm(requset):
    #  增
    # models.UserInfo.objects.create(username='alex',password=123)
    # dic={"username":"eric","password":"123"}
    # models.UserInfo.objects.create(**dic)
    # obj=models.UserInfo(username='jack',password=123)
    # obj.save()

    #  查
    # result=models.UserInfo.objects.all()
    # result=models.UserInfo.objects.filter(username='alex',password=123)
    # #   result  是django返回的一个列表，里面包含了对象
    # for row in result:
    #     print(row.id,row.username,row.password)
    # print(result)
    # 删
    # models.UserInfo.objects.filter(username='alex').delete()

    # 改
    models.UserInfo.objects.filter(id__gt=5).update(password=69)
    return  HttpResponse('orm')



