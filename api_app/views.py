from django.shortcuts import render

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

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import logout
from django.shortcuts import redirect

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
    # Sprawdź, czy użytkownik był zalogowany, ale sesja wygasła
    if not request.user.is_authenticated and 'is_logged_out' in request.session:
        messages.warning(request, "Sesja wygasła. Zostałeś wylogowany.")
        del request.session['is_logged_out']  

    # Jeśli użytkownik jest zalogowany, pokaż artykuły prywatne
    if request.user.is_authenticated:
        request.session['is_logged_out'] = True  
        articles = Article.objects.all()  
    else:
        articles = Article.objects.values('title')  # Niezalogowani widzą tylko tytuły artykułów

    return render(request, 'articles/index.html', {'articles': articles, 'user_authenticated': request.user.is_authenticated})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Witaj {username}, jesteś zalogowany!")
                return redirect('article-list')  
            else:
                messages.error(request, "Nieprawidłowe dane logowania.")
        else:
            messages.error(request, "Nieprawidłowe dane logowania.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'articles/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('article-list')