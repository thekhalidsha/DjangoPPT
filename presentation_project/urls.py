# presentation_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('presentation_app.urls')),  # Include presentation_app URLs
]
