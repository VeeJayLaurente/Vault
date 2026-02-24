from django.urls import path
from . import views

urlpatterns = [
    path('', views.onboarding, name="onboarding"),
    path('home', views.home, name="home"),
    path('login',views.login, name="login"),
    path('register', views.register, name="register"),
    path('monet',views.monet,name="monet"),
    path('gogh',views.gogh,name="gogh"),
    path('picasso',views.picasso,name="picasso"),
    path('dali',views.dali,name="dali"),
    path('user',views.user,name="user"),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/delete/', views.delete_account, name='delete_account'),
    path('logout/', views.logout_view, name='logout'),
    path('favorite/toggle/', views.toggle_favorite, name='toggle_favorite'),
]
