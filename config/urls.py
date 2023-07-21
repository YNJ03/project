from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    ### 127.0.0.1:8000/
    path('', include('mainapp.urls')),
    
    ### 127.0.0.1:8000/main
    path('main/', include('mainapp.urls')),
]
