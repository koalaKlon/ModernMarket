from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'store'

urlpatterns = [
    path('', views.index, name='home'),
    path('basket', views.product, name='product'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),

#    path('', views.product_list, name='product_list'),
    path('<str:category_slug>/', views.product_list, name='product_list_by_category'),
#    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
