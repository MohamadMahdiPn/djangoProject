from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='landingPage'),
    path('posts',views.posts , name='postsPage'),
    path('posts/<slug>',views.single_post , name='postDetailsPage')

]