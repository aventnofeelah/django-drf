from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, CategoryViewSet, PriorityViewSet, TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
router = DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'priorities', PriorityViewSet)
router.register(r'tasks', TaskViewSet)

#urlpatterns = router.urls
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.index_render, name='index_path'),
    path('contact/', views.contact_view, name='contact_path'),
]


