from django.shortcuts import render
from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetail(generics.RetrieveUpdateDestroyAPIView): # Retrieve 스펠링주의!
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
