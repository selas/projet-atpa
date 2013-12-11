from django import forms

class ContactForm(forms.Form):
	login = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)
	
class ChoixQuestion(forms.Form):
	OPTION = (	
				( "1" , "choix simple" ),
				( "2" , "choix multiple" ),
				( "3" , "alpha-numerique" )
			)
	Choix = forms.MultipleChoiceField(widget=forms.Select, choices = OPTION)