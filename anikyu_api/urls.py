from django.urls import include, path
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from anikyu_api import views

"""router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'animes', views.AnimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

"""

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('anime/', views.AnimeList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)