from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Doctor
from .forms import DoctorForm
import json


class DoctorFormTestCase(TestCase):

	# def setup(self):

	# 	user = get_user_model().object.create_user('Amy')


	def test_valid_data(self):

		form = DoctorForm({

			'first_name': "Amy",
			'last_name': "Anderson",
			'email': "Aanderson@gmail.com",
			})

		self.assertTrue(form.is_valid())
		doctor = form.save()

		self.assertEqual(doctor.first_name, "Amy")
		self.assertEqual(doctor.last_name, "Anderson")
		self.assertEqual(doctor.email, "Aanderson@gmail.com")


	def test_get_doctors(self):
		""" Getting doctors from a populated database """

		doctorA = Doctor(first_name="Joe", last_name= "Alpha", email= "Janderson@gmail.com")

		doctorB = Doctor(first_name="Dan", last_name= "Beta", email= "Janderson@gmail.com")

		doctorA.save()
		doctorB.save()

		response = self.client.get("/doctors/")

		self.assertEqual(response.status_code, 200)

		data = json.loads(response.content)
		self.assertEqual(len(data), 2)


	def test_get_doctors(self):
		""" Get 1 doctor from a database """

		doctorA = Doctor(first_name="Joe", last_name= "Alpha", email= "Janderson@gmail.com")

		doctorB = Doctor(first_name="Dan", last_name= "Beta", email= "Janderson@gmail.com")

		doctorA.save()
		doctorB.save()

		response = self.client.get("/doctors/1")

		self.assertEqual(response.status_code, 200)

		data = json.loads(response.content)

		print(data)
		
		self.assertEqual(len(data), 1)
		self.assertEqual(data.first_name, "Joe")











	


