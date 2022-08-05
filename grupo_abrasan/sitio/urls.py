from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

from . import views
app_name="sitio"
urlpatterns=[
   #----------------- I N V E N T A R I O --------------------------------
   
   path("",views.panel, name="home"),
   path("nosotros",views.nosotros, name="nosotros"),
   path("mision",views.mision, name="mision"),
   path("vision",views.vision, name="vision")
   
   
   ]