from django.shortcuts import render
from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class BookingDetail(generics.RetriveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
