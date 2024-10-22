from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Article

class ArticleListView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        
        if request.user.is_authenticated:
            # Zalogowani użytkownicy widzą pełne dane
            data = [{'title': article.title, 'year': article.year} for article in articles]
        else:
            # Niezalogowani widzą tylko tytuł
            data = [{'title': article.title} for article in articles]

        return Response(data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "Wylogowano z powodu wygaśnięcia sesji."})
