from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# --------------------------------- Choices ---------------------------------
statuses = [
	('acc', 'Accepted'),
	('can', 'Canceled'),
	('pen', 'Pending'),
]
boolean_choices = [
	('Has', 'Has'),
	('Has not', 'Has not'),
]
rooms = [1, 2, 3, 4, 5, 6, 'بیشتر از 6', 'بدون اتاق']
floors = ['همکف', 'زیر همکف', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 'بالاتر از 29']


# --------------------------------- Models ---------------------------------
class Province(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class City(models.Model):
	name = models.CharField(max_length=100)
	province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cities')

	def __str__(self):
		return self.name


class District(models.Model):
	name = models.CharField(max_length=100)
	city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')

	def __str__(self):
		return self.name


class RealEstate(models.Model):
	province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
	city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
	district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	room = models.CharField(max_length=30, blank=True, null=True)
	area = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(1000)], blank=True,null=True)
	year = models.IntegerField(validators=[MinValueValidator(1350)], blank=True, null=True)
	floor = models.CharField(max_length=30, blank=True, null=True)
	parking = models.CharField(max_length=30, blank=True, null=True)
	elevator = models.CharField(max_length=30, blank=True, null=True)
	warehouse = models.CharField(max_length=30, blank=True, null=True)
	document = models.CharField(max_length=100, blank=True, null=True)
	description = models.TextField(max_length=1000, blank=True, null=True)
	status = models.CharField(max_length=30, choices=statuses, default='pen')
	datetime_created = models.DateTimeField(auto_now_add=True)
