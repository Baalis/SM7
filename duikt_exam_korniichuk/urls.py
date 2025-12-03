from django.contrib import admin
from django.urls import path
from duikt_task_korniichuk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('install/', views.install, name='install'),
    path('duikt_page_korniichuk/', views.show_page, name='duikt_page_korniichuk'),
    path('', views.show_page, name='home'),  # головна сторінка
]
