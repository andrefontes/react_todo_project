from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
import requests
from django.http import JsonResponse


class TaskViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer

    def get_queryset(self):
        #return self.request.user.tasks.all()
        return Task.objects.all().order_by('id')
        # Filtra as tarefas do usuário logado
        #return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(user=user)

class UserViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = User.objects.create_user(username=username, password=password)
            return Response({'id': user.id, 'username': user.username})
        return Response({'error': 'Invalid data'}, status=400)


#class TaskViewList(APIView):
#    def get(self, request):
#        tasks = Task.objects.all()
#        serializer = TaskSerializer(tasks, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
    

#class TaskListView(generics.ListCreateAPIView):
#    queryset = Task.objects.all()
#    serializer_class = TaskSerializer


#class TaskListView(ListAPIView):
#    queryset = Task.objects.all()
#    serializer_class = TaskSerializer
#    pagination_class = PageNumberPagination

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination 



# Configuração de paginação
#class CategoryPagination(PageNumberPagination):
#    page_size = 10  # Quantidade de itens por página (ajuste conforme necessário)
#    page_size_query_param = 'page_size'
#    max_page_size = 100

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    #pagination_class = CategoryPagination  # Definindo a paginação



def get_news(request):
    api_key = '005bac6fcad647bba1137a9ed0f4e211'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    response = requests.get(url)
    news = response.json()
    return JsonResponse(news['articles'], safe=False)


