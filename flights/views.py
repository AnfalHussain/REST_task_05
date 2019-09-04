from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer, RegisterSerializer, UpdateBooking2Serializer


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	serializer_class = BookingSerializer

	def get_queryset(self):
		query = Booking.objects.filter(date__gte=datetime.today(),
			user= self.request.user)
		return query




class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

	def get_serializer_class(self):
		if self.request.user.is_staff:
			return UpdateBookingSerializer
		else:
			return UpdateBooking2Serializer

		


	# def get_serializer(self, *args, **kwargs):
	# 	if self.request.user.is_staff:
	# 		serializer_class = UpdateBookingSerializer
	# 	else:
	# 		serializer_class = UpdateBooking2Serializer
			
	# 	serializer_class = self.get_serializer_class()
	# 	kwargs['context'] = self.get_serializer_context()
	# 	return serializer_class(*args, **kwargs)

	# def get_serializer_class(self):


	# 	assert self.serializer_class is not None, (
	# 		if self.request.user.is_staff:
	# 			serializer_class = UpdateBookingSerializer
	# 		else:
	# 			serializer_class = UpdateBooking2Serializer

 #            % self.__class__.__name__
 #        )

	# 	return self.serializer_class	


	# def perform_update(self, serializer):
	# 	if self.request.user.is_staff:
	# 		serializer_class = UpdateBookingSerializer
	# 	else:
	# 		serializer_class = UpdateBooking2Serializer

	# 	serializer.save()

	# def define_serializer_class(self, UpdateBookingSerializer, UpdateBooking2Serializer ):
	# 	if self.request.user.is_staff:
	# 		serializer_class = UpdateBookingSerializer
	# 	else:
	# 		serializer_class = UpdateBooking2Serializer

	# 	return serializer_class 	

	

	# if self.request.user.is_staff:
	# 	serializer_class = UpdateBookingSerializer

	# serializer_class = UpdateBooking2Serializer	


	# def partial_update(self, request, *args, **kwargs):
	# 	if self.request.user.is_staff:
	# 		serializer_class = UpdateBookingSerializer

	# 	serializer_class = UpdateBooking2Serializer	

	# 	return self.update(request, *args, **kwargs)




class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class BookFlight(CreateAPIView):
	serializer_class = UpdateBookingSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, flight_id=self.kwargs['flight_id'])


class Register(CreateAPIView):
	serializer_class = RegisterSerializer
