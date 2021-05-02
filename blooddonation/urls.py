from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("super",views.ins_upd_del,name="insert"),
    path("form",views.fpage,name="form"),
    # path("menu.html",views.disp,name="menu")
    path("blooddonation",views.disp,name="blooddonation")
]