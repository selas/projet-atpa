# -*- coding: utf-8 -*-
from django.db import models

TYPEREP_CHOICES = (
	('Choix simple', 'Choix simple'),
	('Choix multiple', 'Choix multiple'),
	('Choix alphanumerique', 'Choix alphanumerique')
)

class Enseignant(models.Model):
	login_ens = models.CharField( "Votre login" , max_length = 50)
	password_ens = models.CharField( "Mot de passe" , max_length = 20)
	def __unicode__(self):
		return self.login_ens

#class TypeReponse(models.Model):
#	libelle_t = models.CharField("Type de question", max_length=20, choices=TYPEREP_CHOICES)
#	def __unicode__(self):
#		return self.libelle_t

#class TypeReponse(models.Model):
#	libelle_t = models.CharField(max_length = 20)
#	def __str__(self):
#		if self.libelle_t == 0 :
#			return "Choix simple"
#		elif self.libelle_t == 1 :
#			return "Choix composé"
#		else:
#			return "Choix numérique"


class Question(models.Model):
	libelle_q = models.CharField("Votre question" , max_length = 250)
	temps_q = models.IntegerField("Temps pour répondre" , max_length = 3 )
	enseigant_q = models.ForeignKey(Enseignant)
	typeReponse_q = models.CharField("Type de question", max_length=20, choices=TYPEREP_CHOICES)
	def __unicode__(self):
		return self.libelle_q

class Reponse(models.Model):
	question_r = models.ForeignKey(Question)
	libelle_r = models.CharField( "Votre réponse" , max_length = 100)
	reponseValide_r = models.BooleanField("Cette réponse est-elle bonne ou non", default=True)
	def __unicode__(self):
		return self.libelle_r


