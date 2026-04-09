from django.contrib import admin
from django.urls import path
from inventory_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('loading/', views.loading, name='loading'),

    path('home/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('products/', views.products, name='products'),
    path('orders/', views.orders, name='orders'),
    path('analytics/', views.analytics, name='analytics'),
    path('export-csv/', views.export_csv, name='export_csv'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]