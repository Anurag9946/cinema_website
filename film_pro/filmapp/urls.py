
from django.urls import path
from . import views

app_name = 'filmapp'

urlpatterns = [

    path('', views.index, name='index'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('review/', views.review, name='review'),
    path('add_review/', views.add_review, name='add_review'),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]


