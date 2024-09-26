# home/urls.py
from django.urls import path
from .views import landing_page, login_selection, user_login, admin_registration, admin_management, feedback, \
    nearby_parking, container

urlpatterns = [
    path('', landing_page, name='landing_page.html'),  # Home page URL
    path('landing_page.html', landing_page, name='landing_page.html'),
    path('login_selection.html', login_selection, name='login_selection.html'),
    path('user_login.html', user_login, name='user_login.html'),
    path('admin_registration.html', admin_registration, name='admin_registration.html'),
    path('admin_management.html', admin_management, name='admin_management.html'),
    path('feedback.html', feedback, name='feedback.html'),
    path('nearby_parking.html', nearby_parking, name='nearby_parking.html'),
    path('Container.html', container, name='Container.html'),
]
