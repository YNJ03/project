"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 127.0.0.1:8000/
    path('', views.Index),
    
    # 127.0.0.1:8000/index/
    path('index/', views.Index),
    
    # 127.0.0.1:8000/details_sunspot
    path('details_sunspot/', views.Details_sunspot),
    
    # 127.0.0.1:8000/details_cme
    path('details_cme/', views.Details_cme),
    
    # 127.0.0.1:8000/details_cme2
    path('details_cme2/', views.Details_cme2),
    
    # 127.0.0.1:8000/details_kp
    path('details_kp/', views.Details_kp),
    
    # 127.0.0.1:8000/details_kp2
    path('details_kp2/', views.Details_kp2),
    
    # 127.0.0.1:8000/details_frequency
    path('details_frequency/', views.Details_frequency),
    
    # 127.0.0.1:8000/details_frequency2
    path('details_frequency2/', views.Details_frequency2),
    
    # 127.0.0.1:8000/details_xline
    path('details_xline/', views.Details_xline),
    
    # 127.0.0.1:8000/details_xline2
    path('details_xline2/', views.Details_xline2),
    
    # 127.0.0.1:8000/details_thermo
    path('details_thermo/', views.Details_thermo),
    
    # 127.0.0.1:8000/details_thermo2
    path('details_thermo2/', views.Details_thermo2),
    
    # 127.0.0.1:8000/details_elino
    path('details_elino/', views.Details_elino),
    
    # 127.0.0.1:8000/details_elino2
    path('details_elino2/', views.Details_elino2),
    
    # 127.0.0.1:8000/details_radioflux
    path('details_radioflux/', views.Details_radioflux),
    
    # 127.0.0.1:8000/details_radioflux2
    path('details_radioflux2/', views.Details_radioflux2),
    
    # 127.0.0.1:8000/any2
    path('any2/', views.any2),
    
    # 127.0.0.1:8000/silsi
    path('silsi/', views.silsi),
    
    # 127.0.0.1:8000/silsi2
    path('silsi2/', views.silsi2),
    
    # 127.0.0.1:8000/details
    path('details/', views.Details),
    
    # 127.0.0.1:8000/details2
    path('details2/', views.Details2),
    
    # 127.0.0.1:8000/details3
    path('details3/', views.Details3),
    
    # 127.0.0.1:8000/details4
    path('details4/', views.Details4),
    
    # 127.0.0.1:8000/details5
    path('details5/', views.Details5),
    
    # 127.0.0.1:8000/sun3_4
    path('sun3_4/', views.sun3_4),
    
    # 127.0.0.1:8000/sun3_3
    path('sun3_3/', views.sun3_3),
    
    # 127.0.0.1:8000/sun3_2
    path('sun3_2/', views.sun3_2),
    
    # 127.0.0.1:8000/sun3_1
    path('sun3_1/', views.sun3_1),
    
    # 127.0.0.1:8000/sun2_1
    path('sun2_1/', views.sun2_1),
    
    # 127.0.0.1:8000/sun1_2
    path('sun1_2/', views.sun1_2),
    
    # 127.0.0.1:8000/sun1_1
    path('sun1_1/', views.sun1_1),

]
