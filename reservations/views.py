from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .choices import Status 

@login_required
def reservation_lists(request):
    return render(request, 'reservations/reservation_lists.html')

@login_required
def pending_list(request):
    res = Reservation.objects.filter(user=request.user, status=Status.PENDING)
    return render(request, 'reservations/status_list.html', {'reservations': res, 'title': 'pending'})

@login_required
def confirmed_list(request):
    res = Reservation.objects.filter(user=request.user, status=Status.CONFIRMED)
    return render(request, 'reservations/status_list.html', {'reservations': res, 'title': 'confirmed'})

@login_required
def cancelled_list(request):
    res = Reservation.objects.filter(user=request.user, status=Status.CANCELLED)
    return render(request, 'reservations/status_list.html', {'reservations': res, 'title': 'cancelled'})

@login_required
def completed_list(request):

    res = Reservation.objects.filter(user=request.user, status=Status.COMPLETED)
    return render(request, 'reservations/status_list.html', {'reservations': res, 'title': 'completed'})
