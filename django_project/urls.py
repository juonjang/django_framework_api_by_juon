
from django.contrib import admin
# django_project/urls.py
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', include('todos.urls')),
]
