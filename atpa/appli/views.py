# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from appli.models import Enseignant, Question

def home(request,name=None):
    if (name):
        return HttpResponse("test hello world !!!! %s" % name)
    else:
        return HttpResponse("Hello World")

def  accueil(request):
	question_list_simple = Question.objects.filter(typeReponse_q="Choix simple")
	question_list_multiple = Question.objects.filter(typeReponse_q="Choix multiple")
	question_list_alphanumerique = Question.objects.filter(typeReponse_q="Choix alphanumerique")
	return render(request, 'appli/accueil.html' , { 'question_list_simple' : question_list_simple, 'question_list_multiple' : question_list_multiple, 'question_list_alphanumerique' : question_list_alphanumerique })

#def Liste_enseignant(request):
#	prof_list = Enseignant.objects.all()
#	return render_to_response('appli/premier_essai.html' , { 'prof_list' : prof_list })


def page_connexion(request):
	 return render_to_response('appli/connexionEnseigant.html')


def form_question(request):
	 return render_to_response('appli/formQuestion.html')



#def acceuil(request):
	#Mettre le traitement pour le formulaire de connexion
#	 return render_to_response('appli/accueil.html')

#def error(request):
#	 return render('appli/connexionEnseigant.html')


