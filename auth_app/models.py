from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Users(User):
	doctor = "Doctor"
	patient = "Patient"
	USER_TYPE_CHOICE = (
		(doctor, "Doctor"),
		(patient, "Patient"),
	)
	user_type = models.CharField("User Type", max_length=50, choices=USER_TYPE_CHOICE)
	country = models.CharField("Country", max_length=100)
	city = models.CharField("City", max_length=100)
	address = models.CharField("Address", max_length=100)
	phone = PhoneNumberField("Phone Number")
	image = models.ImageField("Avatar", default="profile2.png", upload_to='users/', null=True, blank=True)

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"

class Appointment(models.Model):
	doctorname = models.CharField(max_length=50)
	doctoremail = models.EmailField(max_length=50)
	patientname = models.CharField(max_length=50)
	patientemail = models.EmailField(max_length=50)
	appointmentdate = models.DateField(max_length=10)
	appointmenttime = models.TimeField(max_length=10)
	symptoms = models.CharField(max_length=100)
	status = models.BooleanField()
	prescription = models.CharField(max_length=200)
