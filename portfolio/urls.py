from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('datar/', views.datar, name='datar'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('auths/', views.auth_page, name='auth_page'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete-message/<int:id>/',views.delete_message,name='delete_message'),

]
