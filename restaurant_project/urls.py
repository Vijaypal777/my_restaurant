from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from base_app.views import HomeView, AboutView, MenuView, BookTableView, FeedbackView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base_app.urls')),
    path('', HomeView, name="Home"),
    path('about/', AboutView, name="About"),
    path('menu/', MenuView, name="Menu"),
    path('booktable/', BookTableView, name="Book_Table"),
    path('feedback/', FeedbackView, name="Feedback"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 