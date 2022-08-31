from django.contrib import admin
from django.urls import path

from docs import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gen/', views.generated, name='gen'),
    path('admin/', admin.site.urls),
]

