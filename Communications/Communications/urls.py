from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Communications/', include('User.urls')),
    path('api/Communications/', include('File.urls')),
    path('api/Communications/', include('Message.urls')),
    path('api/Communications/', include('Record.urls')),
    path('api/Communications/', include('ChatFile.urls')),
]
