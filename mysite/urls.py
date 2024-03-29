from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from polls import views


"""router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)"""

urlpatterns = [
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]


# urlpatterns += router.urls