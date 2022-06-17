from django.contrib import admin
from django.urls import path, include
from block.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('block.urls')),
    path('register/', Register.as_view(), name='singup')
]
