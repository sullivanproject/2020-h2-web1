from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('update/<int:post_id>', views.update, name='update'),
    path('delete/<int:post_id>', views.delete, name='delete'),
]
