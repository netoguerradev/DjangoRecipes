from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('app/', include('app.urls')) #subdomain app/home/
]
