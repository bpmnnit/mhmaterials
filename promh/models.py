from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from decimal import Decimal
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
import datetime

def get_color(n):
	if n == 2:
		return "red"
	elif n == 1:
		return "yellow"
	elif n == 0:
		return "green"

# Create your models here.
@python_2_unicode_compatible
class Rig(models.Model):
	rig_name = models.CharField(max_length=50, unique=True)
	rig_description = models.TextField(max_length = 1024)
	pub_date = models.DateTimeField('Date Published')
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.rig_name

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

@python_2_unicode_compatible
class ProcessComplex(models.Model):
	process_complex_code = models.CharField(max_length=20, unique=True)
	process_complex_description = models.TextField(max_length=1024)
	pub_date = models.DateTimeField('Date Published')
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.process_complex_code

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)	

@python_2_unicode_compatible
class Platform(models.Model):
	platform_code = models.CharField(max_length=20, unique=True)
	platform_description = models.TextField(max_length=1024)
	pub_date = models.DateTimeField('Date Published')
	process_complex = models.ForeignKey('ProcessComplex', on_delete=models.CASCADE)
	rig = models.ForeignKey('Rig', on_delete=models.CASCADE)
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.platform_code

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)	

@python_2_unicode_compatible
class Well(models.Model):
	MHS = 'MHS'
	MHN = 'MHN'

	WELL_AREA_CHOICES = (
		(MHS, 'MHS'),
		(MHN, 'MHN'),
	)
	well_area = models.CharField(choices=WELL_AREA_CHOICES, max_length=10)
	well_code = models.CharField(max_length=20, unique=True)
	well_description = models.TextField(max_length=1024)
	well_category = models.CharField(max_length=20)
	well_jobtype = models.CharField(max_length=20)
	well_layer = models.CharField(max_length=100)
	well_remarks = models.TextField(max_length=1024)
	pub_date = models.DateTimeField('Date Published')
	platform = models.ForeignKey('Platform', on_delete=models.CASCADE)
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.well_code

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)	

@python_2_unicode_compatible
class Casing(models.Model):

	REQUIRED = 0
	INUSE = 1
	USEDUP = 2

	CASING_USAGE_CHOICES = (
		(REQUIRED, 'Required'),
		(INUSE, 'In Use'),
		(USEDUP, 'Used Up'),
	)
	casing_size_30 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	casing_size_30_status = models.PositiveSmallIntegerField(choices=CASING_USAGE_CHOICES, default=REQUIRED)
	casing_size_20 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	casing_size_20_status = models.PositiveSmallIntegerField(choices=CASING_USAGE_CHOICES, default=REQUIRED)
	casing_size_13_3by8 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	casing_size_13_3by8_status = models.PositiveSmallIntegerField(choices=CASING_USAGE_CHOICES, default=REQUIRED)
	casing_size_11_3by4 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	casing_size_11_3by4_status = models.PositiveSmallIntegerField(choices=CASING_USAGE_CHOICES, default=REQUIRED)
	casing_size_9_5by8 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	casing_size_9_5by8_status = models.PositiveSmallIntegerField(choices=CASING_USAGE_CHOICES, default=REQUIRED)
	pub_date = models.DateTimeField('Date Published')
	well = models.ForeignKey(Well, on_delete=models.CASCADE, unique=True)
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.well.well_code + ' Casing'

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

	def casing_size_30_status_color(self):
		return get_color(self.casing_size_30_status)

	def casing_size_20_status_color(self):
		return get_color(self.casing_size_20_status)

	def casing_size_13_3by8_status_color(self):
		return get_color(self.casing_size_13_3by8_status)

	def casing_size_11_3by4_status_color(self):
		return get_color(self.casing_size_11_3by4_status)

	def casing_size_9_5by8_status_color(self):
		return get_color(self.casing_size_9_5by8_status)									

@python_2_unicode_compatible
class Liner(models.Model):

	REQUIRED = 0
	INUSE = 1
	USEDUP = 2

	LINER_USAGE_CHOICES = (
		(REQUIRED, 'Required'),
		(INUSE, 'In Use'),
		(USEDUP, 'Used Up'),
	)

	liner_size_7 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	liner_size_7_status = models.PositiveSmallIntegerField(choices=LINER_USAGE_CHOICES, default=REQUIRED)
	liner_size_5 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	liner_size_5_status = models.PositiveSmallIntegerField(choices=LINER_USAGE_CHOICES, default=REQUIRED)
	pub_date = models.DateTimeField('Date Published')
	well = models.ForeignKey(Well, on_delete=models.CASCADE, unique=True)
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.well.well_code + ' Liner'

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

	def liner_size_7_status_color(self):
		return get_color(self.liner_size_7_status)

	def liner_size_5_status_color(self):
		return get_color(self.liner_size_5_status)	

@python_2_unicode_compatible
class DrainholeLiner(models.Model):

	REQUIRED = 0
	INUSE = 1
	USEDUP = 2

	DRAINHOLELINER_USAGE_CHOICES = (
		(REQUIRED, 'Required'),
		(INUSE, 'In Use'),
		(USEDUP, 'Used Up'),
	)

	liner_size_5 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	liner_size_5_status = models.PositiveSmallIntegerField(choices=DRAINHOLELINER_USAGE_CHOICES, default=REQUIRED)
	liner_size_3_1by2 = models.DecimalField(decimal_places=3, default=Decimal('0.000'), max_digits=10)
	liner_size_3_1by2_status = models.PositiveSmallIntegerField(choices=DRAINHOLELINER_USAGE_CHOICES, default=REQUIRED)
	pub_date = models.DateTimeField('Date Published')
	well = models.ForeignKey(Well, on_delete=models.CASCADE, unique=True)
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.well.well_code + ' Drainhole Liner'

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

	def drainholeliner_size_5_status_color(self):
		return get_color(self.liner_size_5_status)

	def drainholeliner_size_3_1by2_status_color(self):
		return get_color(self.liner_size_3_1by2_status)

@python_2_unicode_compatible
class Wellhead(models.Model):
	REQUIRED = 0
	INUSE = 1
	USEDUP = 2

	WELLHEAD_USAGE_CHOICES = (
		(REQUIRED, 'Required'),
		(INUSE, 'In Use'),
		(USEDUP, 'Used Up'),
	)

	wellhead_a_section = models.PositiveSmallIntegerField(default=0)
	wellhead_a_section_status = models.PositiveSmallIntegerField(choices=WELLHEAD_USAGE_CHOICES, default=REQUIRED)
	wellhead_b_section = models.PositiveSmallIntegerField(default=0)
	wellhead_b_section_status = models.PositiveSmallIntegerField(choices=WELLHEAD_USAGE_CHOICES, default=REQUIRED)
	wellhead_c_section = models.PositiveSmallIntegerField(default=0)
	wellhead_c_section_status = models.PositiveSmallIntegerField(choices=WELLHEAD_USAGE_CHOICES, default=REQUIRED)	
	wellhead_xmas_tree = models.PositiveSmallIntegerField(default=0)
	wellhead_xmas_tree_status = models.PositiveSmallIntegerField(choices=WELLHEAD_USAGE_CHOICES, default=REQUIRED)
	pub_date = models.DateTimeField('Date Published')
	well = models.ForeignKey(Well, on_delete=models.CASCADE, unique=True)
	user = models.ForeignKey(User, default=1)

	def __str__(self):
		return self.well.well_code + ' Wellhead'

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

	def wellhead_a_section_status_color(self):
		return get_color(self.wellhead_a_section_status)
	
	def wellhead_b_section_status_color(self):
		return get_color(self.wellhead_b_section_status)

	def wellhead_c_section_status_color(self):
		return get_color(self.wellhead_c_section_status)
		
	def wellhead_xmas_tree_status_color(self):
		return get_color(self.wellhead_xmas_tree_status)				