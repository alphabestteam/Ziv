from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Sumo.urls')),
    path('api/', include('Fight.urls')),
    path('api/', include('Gamble.urls')),
    path('api/', include('Gambler.urls')),

]
