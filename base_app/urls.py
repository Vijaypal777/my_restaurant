from django.urls import path
from .views import ProtectedView
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', ProtectedView.as_view(), name='protected_view'),  # Protected route
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='logout_success'), name='logout'),
    path('logout-success/', TemplateView.as_view(template_name='logout.html'), name='logout_success'),
    
]
