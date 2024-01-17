from django.urls import path
from admin_app import views

urlpatterns = [
    path('admin_index',views.admin_index,name='admin_index'),
    path('movie_genres',views.movie_genres,name='movie_genres'),
    path('genre_card',views.genre_card,name='genre_card'),
    path('view_genres/<int:id>',views.view_genres,name='view_genres'),
    path('del_genres/<int:id>',views.del_genres,name='del_genres'),
    path('add_movies',views.add_movies,name='add_movies'),
    path('view_movies',views.view_movies,name='view_movies'),
    path('edit_movies/<int:id>',views.edit_movies,name='edit_movies'),
    path('del_movies/<int:id>',views.del_movies,name='del_movies'),
    path('add_cast',views.add_cast,name='add_cast'),
    path('cast_card',views.cast_card,name='cast_card'),
    path('view_cast<int:id>',views.view_cast,name='view_cast'),
    path('edit_cast/<int:id>',views.edit_cast,name='edit_cast'),
    path('del_cast/<int:id>',views.del_cast,name='del_cast'),
    path('add_songs',views.add_songs,name='add_songs'),
    path('view_songs',views.view_songs,name='view_songs'),
    path('edit_songs/<int:id>',views.edit_songs,name='edit_songs'),
    path('del_songs/<int:id>',views.del_songs,name='del_songs'),
    path('subscription',views.subscription,name='subscription'),
    path('view_plans',views.view_plans,name='view_plans'),
    path('edit_plans/<int:id>',views.edit_plans,name='edit_plans'),
    path('del_plans/<int:id>',views.del_plans,name='del_plans'),
]