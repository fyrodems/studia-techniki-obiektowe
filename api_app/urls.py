from django.urls import path
from .views import LoginView
from .views import PublicArticleView, PrivateArticleView
from .views import article_list_view

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('articles/public/', PublicArticleView.as_view(), name='public-articles'),
    path('articles/private/', PrivateArticleView.as_view(), name='private-articles'),
    path('articles/', article_list_view, name='article-list'),
]
