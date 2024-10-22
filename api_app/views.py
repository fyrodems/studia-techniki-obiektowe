from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Article
from rest_framework.response import Response

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            # return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class PublicArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        data = [{'title': article.title} for article in articles]
        return Response(data)

class PrivateArticleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = Article.objects.all()
        data = [{'title': article.title, 'year': article.year} for article in articles]
        return Response(data)
    
def article_list_view(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})