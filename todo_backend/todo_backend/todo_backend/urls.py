from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet, UserViewSet, TaskListView, CategoryViewSet, get_news
#from tasks.views import *  # Ou de acordo com as funções/views que você precisa importar
#from tasks import views
from knox import views as knox_views







router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')
router.register('tasks', TaskViewSet, basename='tasks')
router.register('users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('api/auth/', include('knox.urls')),  # URLs de autenticação do Knox
    #path('api/tasks/', TaskListView.as_view(), name='task-list'),
    path('api/auth/login/', knox_views.LoginView.as_view(), name='login'),
    #path('api/auth/login/', LoginView.as_view(), name='login'),  # Defina o endpoint para login
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/tasks-list/', TaskListView.as_view(), name='task-list'),
    path('api/news/', get_news, name='get_news'),
    #path('api/news/', get_news.as_view(), name='news'),
]
