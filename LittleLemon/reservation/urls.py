from django.urls import path, include
from .views import index
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls)),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]