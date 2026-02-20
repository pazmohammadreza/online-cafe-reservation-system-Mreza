from django.shortcuts import redirect, render

# Create your views here.

from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation , Comment
from .choices import Status 


@login_required
def reservation_lists(request):
    return render(request, 'reservations/reservation_list.html')

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

    res = Reservation.objects.filter(user=request.user, status=Status.COMPELETED)
    return render(request, 'reservations/status_list.html', {'reservations': res, 'title': 'completed'})

@login_required
def reservation_detail(request, pk):
    # اینجا اون رزرو خاص رو با استفاده از آیدی پیدا میکنیم
    reservation = get_object_or_404(Reservation, pk=pk)
   

    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment_text = request.POST.get('comment')
        
        new_comment = Comment.objects.create(
            user=request.user, # اگر مدل کامنت کاربر رو ذخیره می‌کنه
            comment= comment_text, # یا هر اسمی که برای متن کامنت در مدل گذاشتی
            rating=rating,
            reservation=reservation
        )
        # بعد از ذخیره، صفحه رو ریفرش میکنیم

        reservation.comment = new_comment
        reservation.save()

        return redirect('reservations:reservation_detail', pk=pk)

    return render(request, 'reservations/reservation_detail.html', {'res': reservation})