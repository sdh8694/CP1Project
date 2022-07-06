from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register ,name = 'register'),
    path('login/', views.login ,name = 'login'),
    path('logout/', views.logout ,name = 'logout'),
    path('searchmovie/', views.SearchMovie ,name = 'searchmovie'),
    path('movview/', views.movieview ,name = 'movview'),
    path('movSel/', views.movieSelect, name = 'movSel'),
    #path('mainpage/', views.mainpage, name = 'mainpage'),
    #path('csvToModel/', views.csvTomodel, name = 'csvToModel'),
    path('movSelmsg/', views.movieSelectMsg, name = 'movSmsg'),
    #path('mainpage', views.mainpage, name = 'mainpage'),
]