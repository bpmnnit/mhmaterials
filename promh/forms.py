from django import forms
from django.contrib.auth.models import User

from .models import Well, Platform, Casing, Liner, DrainholeLiner, Wellhead, Rig, ProcessComplex

class WellForm(forms.ModelForm):
	#platform = forms.ModelChoiceField(queryset = Platform.objects.all())

	class Meta:
		model = Well
		fields = ['well_code', 'well_area', 'well_description', 'well_category', 'well_jobtype', 'well_layer', 'well_remarks', 'platform']

class CasingForm(forms.ModelForm):
	#platform = forms.ModelChoiceField(queryset = Platform.objects.all())

	class Meta:
		model = Casing
		fields = ['casing_size_30', 'casing_size_20', 'casing_size_13_3by8', 'casing_size_11_3by4', 'casing_size_9_5by8']

class LinerForm(forms.ModelForm):
	#platform = forms.ModelChoiceField(queryset = Platform.objects.all())

	class Meta:
		model = Liner
		fields = ['liner_size_7', 'liner_size_5']

class DrainholeLinerForm(forms.ModelForm):

	class Meta:
		model = DrainholeLiner
		fields = ['liner_size_5', 'liner_size_3_1by2']

class WellheadForm(forms.ModelForm):

	class Meta:
		model = Wellhead
		fields = ['wellhead_a_section', 'wellhead_b_section', 'wellhead_c_section', 'wellhead_xmas_tree']

class RigForm(forms.ModelForm):

	class Meta:
		model = Rig
		fields = ['rig_name', 'rig_description']

class ProcessComplexForm(forms.ModelForm):

	class Meta:
		model = ProcessComplex
		fields = ['process_complex_code', 'process_complex_description']

class PlatformForm(forms.ModelForm):
	
	class Meta:
		model = Platform
		fields = ['platform_code', 'platform_description', 'process_complex', 'rig']	

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']