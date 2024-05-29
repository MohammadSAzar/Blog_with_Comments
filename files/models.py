# import random
# import string
#
# from django.db import models
# from django.shortcuts import reverse
# from django.core.validators import MinValueValidator, MaxValueValidator
#
# from .locations import provinces, city_choices, district_choices
#
#
# # --------------------------------- Choices ---------------------------------
# statuses = [
# 	('acc', 'Accepted'),
# 	('can', 'Canceled'),
# 	('pen', 'Pending'),
# ]
# boolean_choices = [
# 	('Has', 'Has'),
# 	('Has not', 'Has not'),
# ]
# rooms = [1, 2, 3, 4, 5, 6, 'بیشتر از 6', 'بدون اتاق']
# floors = ['همکف', 'زیر همکف', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 'بالاتر از 29']
#
# # --------------------------------- File Model ---------------------------------
# class File(models.Model):
# 	province = models.CharField(max_length=100, choices=provinces, blank=True, null=True)
# 	city = models.CharField(max_length=100, choices=city_choices(province), blank=True, null=True)
# 	district = models.CharField(max_length=100, choices=district_choices(province, city), blank=True, null=True)
# 	room = models.CharField(max_length=30, choices=rooms, blank=True, null=True)
# 	area = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(1000)], choices=rooms, blank=True, null=True)
# 	year = models.IntegerField(validators=[MinValueValidator(1350)], blank=True, null=True)
# 	floor = models.CharField(max_length=30, choices=floors, blank=True, null=True)
# 	parking = models.CharField(max_length=30, choices=boolean_choices, blank=True, null=True)
# 	elevator = models.CharField(max_length=30, choices=boolean_choices, blank=True, null=True)
# 	warehouse = models.CharField(max_length=30, choices=boolean_choices, blank=True, null=True)
# 	document = models.CharField(max_length=100, blank=True, null=True)
# 	description = models.TextField(max_length=1000, blank=True, null=True)
# 	status = models.CharField(max_length=30, choices=statuses, default='pen')
# 	datetime_created = models.DateTimeField(auto_now_add=True)
#
# 	# @property
# 	# def tracking_code(self):
# 	# 	number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# 	# 	choice_list = list(string.ascii_lowercase) + number_list + number_list
# 	# 	code = ''
# 	# 	for i in range(19):
# 	# 		code = code + random.choice(choice_list)
# 	# 	return code
#
# 	def get_absolute_url(self):
# 		return reverse('file_detail', args=[self.id])
