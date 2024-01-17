from django.urls import path
from ott_app import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('tv_shows',views.tv_shows,name='tv_shows'),
    path('movies',views.movies,name='movies'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('songs',views.songs,name='songs'),
    path('show_details/<int:id>',views.show_details,name='show_details'),
    path('filtered_movies/<str:name>',views.filtered_movies,name='filtered_movies'),
    path('pricing',views.pricing,name='pricing'),
    path('purchase_plan/<int:subscription_id>',views.purchase_plan,name='purchase_plan'),
]