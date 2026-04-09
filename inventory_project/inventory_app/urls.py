from django.urls import path
from inventory_app import views

urlpatterns = [
    path('home/', views.dashboard, name='dashboard'),
    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('loading/', views.loading, name='loading'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]