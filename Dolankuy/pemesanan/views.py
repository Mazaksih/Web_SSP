from django.shortcuts import render
from pemesanan.forms import FormBooking
# from django import HttpResponse

def booking(request):
    form=FormBooking()
    konteks={
        'form':form,
    }
    return render(request,'booking.html',konteks)

# def booking(request):
#     if request.method=="POST":
#         form = FormBooking(request.POST)
#         if form.is_valid():
#             form.save()
#         else:
#             form = FormBooking()
#         return render(request, 'booking.html', {'form' : form})