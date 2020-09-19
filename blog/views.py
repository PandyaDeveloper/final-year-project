from django.shortcuts import *
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from random import *
from .models import *
from .utils import *
from socket import *

# Create your views here.
def login(request):
    return render(request,"blog/login.html")

def c(request):
    return render(request,"blog/create.html")

def reg(request):
    return render(request,"blog/registration.html")

def otp(request):
    return render(request,"blog/otpver.html")

def post(request):
    p = postd.objects.all()
    if(p):
        return render(request,"blog/post.html",{'key1':p})
    else:
        del request.session['Email']
        return render(request,"blog/login.html")

#Create your processing view here.

def regis(request):
    em = request.POST['ema']

    user = us.objects.filter(Email=em)

    if(user):
        return render(request,"blog/login.html")
    else:
        p = request.POST['pass']
        cp = request.POST['cpass']
        if(p==cp):
            agew = request.POST['age']
            g = request.POST['gender']
            nu = request.POST['num']
            na = request.POST['nam']

            link="127.0.0.1:8000"

            otpw = randint(1000,9999)

            newuser = us.objects.create(Email=em,password=p,otp=otpw,is_verified=False,is_active=True)
            newu = info.objects.create(email=newuser,name=na,age=agew,number=nu,gender=g)
            email_subject = "Login Verification"
            sendmail(email_subject,'mailtemplate',em,{'name':na,'otp':otpw,'link':link})
            return render(request,"blog/login.html")
        else:
            return render(request,"blog/registration.html")

def vlog(request):
    print("lol")

    ema = request.POST['eml']
    pa = request.POST['pasw']

    one_user = us.objects.filter(Email=ema)
    if(one_user):
        if(one_user[0].password == pa):
                if(one_user[0].is_verified==False):
                    request.session['Email'] = one_user[0].Email
                    return HttpResponseRedirect(reverse("otp"))
                else:
                    request.session['Email'] = one_user[0].Email
                    return HttpResponseRedirect(reverse("post"))
                    
    else:
        return render(request,"blog/registration.html")

def votp(request):
    d = request.session['Email']
    m = request.POST['tp']

    nu = us.objects.filter(Email=d)

    if(nu):
        if(str(nu[0].otp) == m):
            nu[0].is_verified = True
            nu[0].save()
            return render(request,"blog/post.html")
    else:
        return render(request,"blog/login.html")

def crea(request):
    title = request.POST['ta']
    detail = request.POST['dt']
    usep = request.session['Email']

    s = socket()

    port= 64898 #Should same as server side port

    s.connect(('127.0.0.1',port))
    s.send(detail.encode('utf-8'))
    sen = s.recv(1024)
    sen = str(sen)
    sen = sen[2:-1]

    up = us.objects.filter(Email=usep)

    if(up):
        npo = postd.objects.create(pus=up[0],pti=title,pde=detail,sen=sen)
        return HttpResponseRedirect(reverse("post"))
    else:
        return render(request,"blog/login.html")