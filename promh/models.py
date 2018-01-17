from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from decimal import Decimal
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime

def get_color(n):
	if n == 2:
		return "text-danger"
	elif n == 1:
		return "text-warning"
	elif n == 0:
		return "text-success"

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

	REQUIRED = 0
	INUSE = 1
	USEDUP = 2

	USAGE_CHOICES = (
		(REQUIRED, 'Required'),
		(INUSE, 'In Use'),
		(USEDUP, 'Used Up'),
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

	casing_size_30 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_30_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	casing_size_20 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_20_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	casing_size_18_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_18_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	casing_size_13_3by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_13_3by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	float_joint_11_3by4 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_joint_11_3by4_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	casing_size_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	prem_casing_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	prem_casing_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	btc_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	btc_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	chrome_casing_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	chrome_casing_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	float_joint_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_joint_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	float_joint_liner_11_3by4_large = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_joint_liner_11_3by4_large_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	liner_size_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_size_7_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	liner_hanger_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_hanger_7_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	chrome_liner_size_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	chrome_liner_size_7_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	chrome_liner_hanger_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	chrome_liner_hanger_7_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	liner_size_5 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_size_5_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	liner_hanger_5 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_hanger_5_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	
	float_shoe_size_20 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_20_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	float_shoe_size_18_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_18_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	float_shoe_size_13_3by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_13_3by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	float_shoe_size_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)

	float_collar_size_13_3by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_collar_size_13_3by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	float_collar_size_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_collar_size_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)

	btc_pin_prem_box_cross_over_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	btc_pin_prem_box_cross_over_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	btc_box_prem_pin_cross_over_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	btc_box_prem_pin_cross_over_9_5by8_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)

	wellhead_a_section = models.PositiveSmallIntegerField(default=0)
	wellhead_a_section_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	wellhead_b_section = models.PositiveSmallIntegerField(default=0)
	wellhead_b_section_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)
	wellhead_c_section = models.PositiveSmallIntegerField(default=0)
	wellhead_c_section_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)	
	wellhead_xmas_tree = models.PositiveSmallIntegerField(default=0)
	wellhead_xmas_tree_status = models.PositiveSmallIntegerField(choices=USAGE_CHOICES, default=REQUIRED)

	def __str__(self):
		return self.well_code

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

	def casing_size_30_status_color(self):
		return get_color(self.casing_size_30_status)

	def casing_size_20_status_color(self):
		return get_color(self.casing_size_20_status)
	
	def casing_size_18_5by8_status_color(self):
		return get_color(self.casing_size_18_5by8_status)

	def casing_size_13_3by8_status_color(self):
		return get_color(self.casing_size_13_3by8_status)

	def float_joint_11_3by4_status_color(self):
		return get_color(self.float_joint_11_3by4_status)

	def casing_size_9_5by8_status_color(self):
		return get_color(self.casing_size_9_5by8_status)

	def prem_casing_9_5by8_status_color(self):
		return get_color(self.prem_casing_9_5by8_status)

	def btc_9_5by8_status_color(self):
		return get_color(self.btc_9_5by8_status)

	def chrome_casing_9_5by8_status_color(self):
		return get_color(self.chrome_casing_9_5by8_status)
		
	def float_joint_9_5by8_status_color(self):
		return get_color(self.float_joint_9_5by8_status)
		
	def float_joint_liner_11_3by4_large_status_color(self):
		return get_color(self.float_joint_liner_11_3by4_large_status)
		
	def liner_size_7_status_color(self):
		return get_color(self.liner_size_7_status)

	def liner_hanger_7_status_color(self):
		return get_color(self.liner_hanger_7_status)
	
	def chrome_liner_size_7_status_color(self):
		return get_color(self.chrome_liner_size_7_status)
		
	def chrome_liner_hanger_7_status_color(self):
		return get_color(self.chrome_liner_hanger_7_status)
		
	def liner_size_5_status_color(self):
		return get_color(self.liner_size_5_status)
		
	def liner_hanger_5_status_color(self):
		return get_color(self.liner_hanger_5_status)
		
	def float_shoe_size_20_status_color(self):
		return get_color(self.float_shoe_size_20_status)
		
	def float_shoe_size_18_5by8_status_color(self):
		return get_color(self.float_shoe_size_18_5by8_status)
		
	def float_shoe_size_13_3by8_status_color(self):
		return get_color(self.float_shoe_size_13_3by8_status)
		
	def float_shoe_size_9_5by8_status_color(self):
		return get_color(self.float_shoe_size_9_5by8_status)
		
	def float_collar_size_13_3by8_status_color(self):
		return get_color(self.float_collar_size_13_3by8_status)
		
	def float_collar_size_9_5by8_status_color(self):
		return get_color(self.float_collar_size_9_5by8_status)
		
	def btc_pin_prem_box_cross_over_9_5by8_status_color(self):
		return get_color(self.btc_pin_prem_box_cross_over_9_5by8_status)
		
	def btc_box_prem_pin_cross_over_9_5by8_status_color(self):
		return get_color(self.btc_box_prem_pin_cross_over_9_5by8_status)

	def wellhead_a_section_status_color(self):
		return get_color(self.wellhead_a_section_status)
		
	def wellhead_b_section_status_color(self):
		return get_color(self.wellhead_b_section_status)
		
	def wellhead_c_section_status_color(self):
		return get_color(self.wellhead_c_section_status)
		
	def wellhead_xmas_tree_status_color(self):
		return get_color(self.wellhead_xmas_tree_status)
		
@python_2_unicode_compatible
class Stock(models.Model):
	casing_size_30 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_20 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_18_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_13_3by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_joint_11_3by4 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	casing_size_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	prem_casing_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	btc_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	chrome_casing_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_joint_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_joint_liner_11_3by4_large = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_size_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_hanger_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	chrome_liner_size_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	chrome_liner_hanger_7 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_size_5 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	liner_hanger_5 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_20 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_18_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_13_3by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_shoe_size_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_collar_size_13_3by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	float_collar_size_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	btc_pin_prem_box_cross_over_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	btc_box_prem_pin_cross_over_9_5by8 = models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)
	wellhead_a_section = models.PositiveSmallIntegerField(default=0)
	wellhead_b_section = models.PositiveSmallIntegerField(default=0)
	wellhead_c_section = models.PositiveSmallIntegerField(default=0)
	wellhead_xmas_tree = models.PositiveSmallIntegerField(default=0)

	def __str__(self):
		return "Stock of the materials, MH Asset"

	def get_absolute_url(self):
		return reverse('update_stock', kwargs = { 'pk': self.pk })

# This is a demo of git for aishwarya
