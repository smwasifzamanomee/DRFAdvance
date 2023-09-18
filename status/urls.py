from django.urls import path

# from .views import  StatusListCreateAPIView, StatusDetailUpdateDeleteAPIView

from .views import StatusViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'status', StatusViewSet, basename='status')

urlpatterns = [
    # path('status/', StatusAPIView.as_view(), name='status-list'),
    # path('status/', StatusListCreateAPIView.as_view(), name='status-list'),
    # path('status/list/', StatusListAPIView.as_view(), name='status-list'),
    # path('status/create/', StatusCreateAPIView.as_view(), name='status-create'),
    # path('status/<id>/', StatusDetailUpdateDeleteAPIView.as_view(), name='status-detail'),
    # path('status/update/<id>/', StatusUpdateAPIView.as_view(), name='status-update'),
    # path('status/delete/<id>/', StatusDeleteAPIView.as_view(), name='status-delete'),
] + router.urls