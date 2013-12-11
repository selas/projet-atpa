from django import forms

class Connexion(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)


class AjoutQuestion(forms.Form):

	TYPEREP_CHOICES = (
		('Choix simple', 'Choix simple'),
		('Choix multiple', 'Choix multiple'),
		('Choix alphanumerique', 'Choix alphanumerique')
	)


	intituleQuestion = forms.CharField(max_length=100)
	temps = forms.IntegerField()
	typeReponse = forms.CharField(max_length=100)#, choices=TYPEREP_CHOICES)

	intituleReponse = forms.CharField(max_length = 100)

	reponseValide_r = forms.BooleanField()#, default=True)

	OPTION = (	
				( "1" , "choix simple" ),
				( "2" , "choix multiple" ),
				( "3" , "alpha-numerique" )
			)
	Choix = forms.MultipleChoiceField(widget=forms.Select, choices = OPTION)

