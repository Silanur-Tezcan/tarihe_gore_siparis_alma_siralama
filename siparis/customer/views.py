
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from datetime import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required



def home(request):
    if request.method == 'POST':
        # Formdan gelen verileri alıyoruz
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        details = request.POST.get('details')
        restaurant=request.POST.get('restaurant')

        # Tarih ve saati birleştiriyoruz
        reservation_datetime = datetime.combine(datetime.strptime(date, "%Y-%m-%d"), datetime.strptime(time, "%H:%M").time())

        # Veriyi veritabanına kaydediyoruz
        Reservation.objects.create(name=name, phone=phone, date=reservation_datetime, details=details,restaurant=restaurant)

        # Kaydedildikten sonra başarı sayfasına yönlendiriyoruz
        return redirect('home')  # Admin paneline yönlendir
    return render(request, 'home.html')


@login_required(login_url='/login/')
def admin_dashboard(request):
    reservations = Reservation.objects.all().order_by('date')
    return render(request, 'admin_dashboard.html', {'reservations': reservations})


def reservation_form(request):
    # Oturum kontrolü zaten Django tarafından yapılır, ek bir `is_authenticated` göndermeye gerek yok
    return render(request, 'reservation_form.html')


@login_required(login_url='/login/')
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('dashboard')
    return render(request, 'admin_dashboard.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Admin panele yönlendirme
        else:
            return render(request, 'login.html', {'error': 'Geçersiz kullanıcı adı veya şifre'})
    return render(request, 'login.html')