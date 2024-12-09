"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render

def view_sum(request):
    return HttpResponse("Hello I am sum")

def view_sub(request):
    resp= HttpResponse("Hello I am calling sub")
    return resp

def view_mult(request):
    resp= render(request, 'calc.html')
    return resp

def view_div(request):
    resp= HttpResponse("Hello I am calling div")
    return resp

def view_calc(request):
    a=int(request.POST.get("t1",0))
    b=int(request.POST.get("t2",0))
    if request.method=='GET':
        
        resp= render(request, 'calc.html')
        return resp
    elif request.method=='POST':
        if 'btnsum' in request.POST:
            # result=request.GET.get("result","NA")
            result=a+b
        elif 'btnsub' in request.POST:
            # result=request.GET.get("result","NA")
            result=a-b
        elif 'btnmult' in request.POST:
            # result=request.GET.get("result","NA")
            result=a*b
        elif 'btndiv' in request.POST:
            # result=request.GET.get("result","NA")
            result=a/b

        d1={'a':a,'b':b,'result':result}
        print("a=",a ,"b=",b, "result=",result)
        resp= render(request, 'calc.html',context=d1)
        return resp
def check_numeric(request):
    Numeric_list=['btn1','btn2','btn3','btn4','btn5','btn6','btn7','btn8','btn9','btn0']
    for b in Numeric_list:
        if b in request.POST:
            return b[3]
    return b[-1]

def simplecalc(request):
    if request.method=='GET':
        resp= render(request, 'simplecalc.html')
        return resp
    elif request.method=='POST':
        numeric= check_numeric(request)
        if (numeric!="-1"):
            output= request.POST.get('res','NA')
            output+=numeric   # output+numeric ==>  0+numeric
            d1={'res':output}
            resp= render(request,'simplecalc.html',context=d1)
            return resp


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sum/', view_sum),
    path('sub/', view_sub),
    path('mult/', view_mult),
    path('div/', view_div),
    path('calc/', view_calc),
    path('simplecalc/', simplecalc),
    path('ems/',include('EMS.urls')),

]
