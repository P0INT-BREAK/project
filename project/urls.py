from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Protfolio.urls')),
    path('auth/',include('authentication_app.urls')),
]
