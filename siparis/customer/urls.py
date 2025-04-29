# customer/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import admin_dashboard, custom_login, reservation_form,delete_reservation



urlpatterns = [
    path('', views.home, name='home'),  # boş url customer/views.py'daki home fonksiyonuna gidecek

    path('reservation/delete/<int:id>/', delete_reservation, name='delete_reservation'),  # Silme URL'si
    
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),  # Çıkış URL'si
    path('login/', custom_login, name='login'),
    path('dashboard/', admin_dashboard, name='dashboard'),
    path('reservation/', reservation_form, name='reservation'),



]
