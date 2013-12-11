from django.conf.urls import patterns, url
from appli.views import accueil, form_question


urlpatterns = patterns('',
	#url(r'^listing_ens/$', 'appli.views.Liste_enseignant', name='listing_ens'),
	#url(r'^listing_que/$', 'appli.views.tri_question', name='tri_question'),
	#url(r'^connexion/$', 'appli.views.page_connexion', name='connexion'),
	url(r'^accueil/$', 'appli.views.accueil', name='accueil'),

	url(r'^form_question/$', 'appli.views.form_question', name='form_question'),
	url(r'^ajout_question/$' , 'appli.views.choixquestion_view', name="choix_question")
	#url(r'^error/$', 'appli.views.error', name='error')
)
