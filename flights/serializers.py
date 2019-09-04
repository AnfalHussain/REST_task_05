from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Flight, Booking


class FlightSerializer(serializers.ModelSerializer):
	class Meta:
		model = Flight
		fields = ['destination', 'time', 'price', 'id']


class BookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'id']


class BookingDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['flight', 'date', 'passengers', 'id']



class UpdateBooking2Serializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['passengers']


class UpdateBookingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Booking
		fields = ['date', 'passengers']


	# def perform_update(self, serializer):
	#     if self.request.user.is_staff:
	#         myDate = self.kwargs['date']
	#         mypassengers = self.kwargs['passengers']



	# def update(self, request, *args, **kwargs):
	#     partial = kwargs.pop('partial', False)
	#     instance = self.get_object()
	#     serializer = self.get_serializer(instance, data=request.data, partial=partial)
	#     serializer.is_valid(raise_exception=True)
	#     self.perform_update(serializer)
	#     return Response(serializer.data)
	#     serializer.save()



class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password', 'first_name', 'last_name']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		first_name = validated_data['first_name']
		last_name = validated_data['last_name']
		new_user = User(username=username, first_name=first_name, last_name=last_name)
		new_user.set_password(password)
		new_user.save()
		return validated_data