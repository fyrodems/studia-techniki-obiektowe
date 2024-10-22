from django.urls import path
# from .views import LoginView

from .views import login_view, logout_view, article_list_view, PublicArticleView, PrivateArticleView

urlpatterns = [
    path('login/', login_view, name='login'),  # Formularz logowania
    path('logout/', logout_view, name='logout'),  # Wylogowanie
    path('articles/public/', PublicArticleView.as_view(), name='public-articles'),
    path('articles/private/', PrivateArticleView.as_view(), name='private-articles'),
    path('articles/', article_list_view, name='article-list'),
]

