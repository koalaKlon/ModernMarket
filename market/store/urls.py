from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'store'

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)