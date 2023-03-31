from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('about/', views.about, name='about'),
    path('about/', views.about, name='about'),
]