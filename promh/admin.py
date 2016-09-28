from django.contrib import admin

# Register your models here.
from .models import Rig
from .models import ProcessComplex
from .models import Platform
from .models import Well
from .models import Casing
from .models import Liner
from .models import DrainholeLiner
from .models import Wellhead

class RigAdmin(admin.ModelAdmin):
	list_display = ('rig_name', 'rig_description', 'pub_date', 'was_published_recently')

class ProcessComplexAdmin(admin.ModelAdmin):
	list_display = ('process_complex_code', 'process_complex_description', 'pub_date', 'was_published_recently')

class PlatformAdmin(admin.ModelAdmin):
	list_display = ('platform_code', 'platform_description', 'rig', 'process_complex', 'pub_date', 'was_published_recently')

class WellAdmin(admin.ModelAdmin):
	list_display = ('well_code', 'well_jobtype', 'well_category', 'well_layer', 'platform', 'pub_date', 'was_published_recently')

class CasingAdmin(admin.ModelAdmin):
	list_display = ('well', 'casing_size_30', 'casing_size_30_status', 'casing_size_20', 'casing_size_20_status', 'casing_size_13_3by8', 'casing_size_13_3by8_status', 'casing_size_11_3by4', 'casing_size_11_3by4_status', 'casing_size_9_5by8', 'casing_size_9_5by8_status', 'pub_date', 'was_published_recently')

class LinerAdmin(admin.ModelAdmin):
	list_display = ('well', 'liner_size_7', 'liner_size_7_status', 'liner_size_5', 'liner_size_5_status', 'pub_date', 'was_published_recently')	

admin.site.register(Rig, RigAdmin)
admin.site.register(ProcessComplex, ProcessComplexAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Well, WellAdmin)
admin.site.register(Casing, CasingAdmin)
admin.site.register(Liner, LinerAdmin)
admin.site.register(DrainholeLiner)
admin.site.register(Wellhead)