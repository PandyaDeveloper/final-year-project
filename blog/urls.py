from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.login,name="login"),
    path("reg",views.reg,name="reg"),
    path("otp",views.otp,name="otp"),
    path("post",views.post,name="post"),
    path("regis",views.regis,name="regis"),
    path("vlog",views.vlog,name="vlog"),
    path("votp",views.votp,name="vtp"),
    path("cre",views.crea,name="sen"),
    path("c",views.c,name="c"),
]