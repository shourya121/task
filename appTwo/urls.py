from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name="appTwo"
urlpatterns = [
        path('', views.index, name='index'),

    path('appTwo/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
]
urlpatterns += [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
