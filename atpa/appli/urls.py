from django.conf.urls import patterns, url
from appli.views import home, page_connexion, accueil, form_question

urlpatterns = patterns('',
	url(r'^home/$', 'appli.views.home', name='home'),
	url(r'^home/(\w+)?$', 'appli.views.home', name='home_name'), 
	#url(r'^listing_ens/$', 'appli.views.Liste_enseignant', name='listing_ens'),
	#url(r'^listing_que/$', 'appli.views.tri_question', name='tri_question'),
	#url(r'^connexion/$', 'appli.views.page_connexion', name='connexion'),
	url(r'^accueil/$', 'appli.views.accueil', name='accueil'),

	url(r'^form_question/$', 'appli.views.form_question', name='form_question')#,

	#url(r'^error/$', 'appli.views.error', name='error')
)

