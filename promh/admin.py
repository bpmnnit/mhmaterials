from django.contrib import admin

# Register your models here.
from .models import Rig
from .models import ProcessComplex
from .models import Platform
from .models import Well
from .models import Stock

class RigAdmin(admin.ModelAdmin):
	list_display = ('rig_name', 'rig_description', 'pub_date', 'was_published_recently')

class ProcessComplexAdmin(admin.ModelAdmin):
	list_display = ('process_complex_code', 'process_complex_description', 'pub_date', 'was_published_recently')

class PlatformAdmin(admin.ModelAdmin):
	list_display = ('platform_code', 'platform_description', 'rig', 'process_complex', 'pub_date', 'was_published_recently')

class WellAdmin(admin.ModelAdmin):
	list_display = ('well_area', 'well_code', 'well_description', 'well_category', 'well_jobtype', 'well_layer', 'well_remarks', 'platform', 'user', 'casing_size_30', 'casing_size_30_status', 'casing_size_20', 'casing_size_20_status', 'casing_size_18_5by8', 'casing_size_18_5by8_status', 'casing_size_13_3by8', 'casing_size_13_3by8_status', 'float_joint_11_3by4', 'float_joint_11_3by4_status', 'casing_size_9_5by8', 'casing_size_9_5by8_status', 'prem_casing_9_5by8', 'prem_casing_9_5by8_status', 'btc_9_5by8', 'btc_9_5by8_status', 'chrome_casing_9_5by8', 'chrome_casing_9_5by8_status', 'float_joint_9_5by8', 'float_joint_9_5by8_status', 'float_joint_liner_11_3by4_large', 'float_joint_liner_11_3by4_large_status', 'liner_size_7', 'liner_size_7_status', 'liner_hanger_7', 'liner_hanger_7_status', 'chrome_liner_size_7', 'chrome_liner_size_7_status', 'chrome_liner_hanger_7', 'chrome_liner_hanger_7_status', 'liner_size_5', 'liner_size_5_status', 'liner_hanger_5', 'liner_hanger_5_status', 'float_shoe_size_20', 'float_shoe_size_20_status', 'float_shoe_size_18_5by8', 'float_shoe_size_18_5by8_status', 'float_shoe_size_13_3by8', 'float_shoe_size_13_3by8_status', 'float_shoe_size_9_5by8', 'float_shoe_size_9_5by8_status', 'float_collar_size_13_3by8', 'float_collar_size_13_3by8_status', 'float_collar_size_9_5by8', 'float_collar_size_9_5by8_status', 'btc_pin_prem_box_cross_over_9_5by8', 'btc_pin_prem_box_cross_over_9_5by8_status', 'btc_box_prem_pin_cross_over_9_5by8', 'btc_box_prem_pin_cross_over_9_5by8_status', 'wellhead_a_section', 'wellhead_a_section_status', 'wellhead_b_section', 'wellhead_b_section_status', 'wellhead_c_section', 'wellhead_c_section_status', 'wellhead_xmas_tree', 'wellhead_xmas_tree_status', 'pub_date', 'was_published_recently')

admin.site.register(Rig, RigAdmin)
admin.site.register(ProcessComplex, ProcessComplexAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Well, WellAdmin)
admin.site.register(Stock)