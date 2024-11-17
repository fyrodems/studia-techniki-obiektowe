from django.urls import path

from .views import login_view, logout_view, article_list_view, PublicArticleView, PrivateArticleView

urlpatterns = [
    path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'), 
    path('articles/public/', PublicArticleView.as_view(), name='public-articles'),
    path('articles/private/', PrivateArticleView.as_view(), name='private-articles'),
    path('articles/', article_list_view, name='article-list'),
]

