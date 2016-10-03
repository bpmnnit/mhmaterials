from django import forms
from django.contrib.auth.models import User

from .models import Well, Platform, Casing, Liner, DrainholeLiner, Wellhead, Rig, ProcessComplex

class WellForm(forms.ModelForm):
	#platform = forms.ModelChoiceField(queryset = Platform.objects.all())

	class Meta:
		model = Well
		fields = ['well_code', 'well_area', 'well_description', 'well_category', 'well_jobtype', 'well_layer', 'well_remarks', 'pub_date', 'platform']

class CasingForm(forms.ModelForm):
	#platform = forms.ModelChoiceField(queryset = Platform.objects.all())

	class Meta:
		model = Casing
		fields = ['casing_size_30', 'casing_size_30_status', 'casing_size_20', 'casing_size_20_status', 'casing_size_13_3by8', 'casing_size_13_3by8_status', 'casing_size_11_3by4', 'casing_size_11_3by4_status', 'casing_size_9_5by8', 'casing_size_9_5by8_status', 'pub_date']

class LinerForm(forms.ModelForm):
	#platform = forms.ModelChoiceField(queryset = Platform.objects.all())

	class Meta:
		model = Liner
		fields = ['liner_size_7', 'liner_size_7_status', 'liner_size_5', 'liner_size_5_status', 'pub_date']

class DrainholeLinerForm(forms.ModelForm):

	class Meta:
		model = DrainholeLiner
		fields = ['liner_size_5', 'liner_size_5_status', 'liner_size_3_1by2', 'liner_size_3_1by2_status', 'pub_date']

class WellheadForm(forms.ModelForm):

	class Meta:
		model = Wellhead
		fields = ['wellhead_a_section', 'wellhead_a_section_status', 'wellhead_b_section', 'wellhead_b_section_status', 'wellhead_c_section', 'wellhead_c_section_status', 'wellhead_xmas_tree', 'wellhead_xmas_tree_status', 'pub_date']

class RigForm(forms.ModelForm):

	class Meta:
		model = Rig
		fields = ['rig_name', 'rig_description', 'pub_date']

class ProcessComplexForm(forms.ModelForm):

	class Meta:
		model = ProcessComplex
		fields = ['process_complex_code', 'process_complex_description', 'pub_date']

class PlatformForm(forms.ModelForm):
	
	class Meta:
		model = Platform
		fields = ['platform_code', 'platform_description', 'process_complex', 'rig', 'pub_date']	

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']