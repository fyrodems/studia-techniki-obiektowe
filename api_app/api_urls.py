from django.urls import path
from .api.views import ArticleListView, LogoutView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
