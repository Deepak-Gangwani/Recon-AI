from django.urls import path
from . import views
from django.conf.urls import handler404
from django.conf.urls import handler403
from .views import custom_page_not_found

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('take-attendance/', views.take_attendance_view, name='take_attendance'),
    path('show-attendance/', views.show_attendance_view, name='show_attendance'),
    path('success_page/', views.success_page, name='success_page'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-register/', views.admin_register, name='admin_register'),
    path('login/', views.user_login, name='login'),
    path('admin', views.user_logout, name='logout'),
    path('success/', views.success, name='success'),
    path('accounts/login/', views.login_redirect, name='login_redirect'),
    path('internet-failure/', views.internet_failure, name='internet_failure'),
    path('reconnect/', views.reconnect, name='reconnect'),
    path('no-location-access/', views.no_location_access, name='no_location_access'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact_view, name='contact')


    # Add other URL patterns as needed
]

handler404 = custom_page_not_found
handler403 = views.custom_permission_denied_view
