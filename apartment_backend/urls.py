from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/visitors/', include('visitors.urls')),
    path('api/parking/', include('parking.urls')),
    path('api/firesafety/', include('firesafety.urls')),
]
