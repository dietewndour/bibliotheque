from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 🔥 ADMIN
    path('api/', include('api.urls')),  # ton API
]