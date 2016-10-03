from django.conf.urls import url

from . import views

app_name = 'promh'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^(?P<well_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<platform_id>[0-9]+)/platform/$', views.platform_detail, name='platform_detail'),
	url(r'^(?P<processcomplex_id>[0-9]+)/processcomplex/$', views.processcomplex_detail, name='processcomplex_detail'),
	url(r'^(?P<rig_id>[0-9]+)/rig/$', views.rig_detail, name='rig_detail'),
	url(r'^create_well/$', views.create_well, name='create_well'),
	url(r'^create_rig/$', views.create_rig, name='create_rig'),
	url(r'^create_platform/$', views.create_platform, name='create_platform'),
	url(r'^create_proccesscomplex/$', views.create_processcomplex, name='create_processcomplex'),
	url(r'^(?P<well_id>[0-9]+)/create_casing/$', views.create_casing, name='create_casing'),
	url(r'^(?P<well_id>[0-9]+)/create_liner/$', views.create_liner, name='create_liner'),
	url(r'^(?P<well_id>[0-9]+)/create_drainholeliner/$', views.create_drainholeliner, name='create_drainholeliner'),
	url(r'^(?P<well_id>[0-9]+)/create_wellhead/$', views.create_wellhead, name='create_wellhead'),
	url(r'^(?P<well_id>[0-9]+)/delete_well/$', views.delete_well, name='delete_well'),
	# promh/[0-9]+ -> matches a well
	# url(r'^(?P<well_id>[0-9]+)/$', views.detail, name='detail'),
	#url(r'^(?P<process_complex_id>[0-9]+)/$', views.process_complex_detail, name='process_complex_detail'),
	#url(r'^(?P<platform_id>[0-9]+)/$', views.platform_detail, name='platform_detail'),
	#url(r'^(?P<well_id>[0-9]+)/$', views.well_detail, name='well_detail'),
	#url(r'^(?P<casing_id>[0-9]+)/$', views.casing_detail, name='casing_detail'),
	#url(r'^(?P<liner_id>[0-9]+)/$', views.liner_detail, name='liner_detail'),
	#url(r'^(?P<drainhole_liner_id>[0-9]+)/$', views.drainhole_liner_detail, name='drainhole_liner_detail'),
	#url(r'^(?P<wellhead_id>[0-9]+)/$', views.wellhead_detail, name='wellhead_detail'),
]