from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Hotel, Client, Service, Reservation, Chambre
from .forms import ContactForm

# Create your views here.


def indexHotel(request):
	return render(request, 'hotelBloc/indexHotel.html')

def reservation(request):

	disponible=Service.objects.filter(disponibilite=True).order_by('-created_at')[:4]  # je demande qu'on affiche en groupe de 3 les services dispo et par ordre de creation 
	
	return render(request, 'hotelBloc/reservation.html', {'dispo':disponible})

def historique(request):

	return render(request, 'hotelBloc/historique.html')

def differentsHotels(request):

	chamb=Chambre.objects.filter(disponibilite=True)
	paginator=Paginator(chamb, 3)
	page=request.GET.get('page')
	try:
		chambr=paginator.page(page)
	except PageNotAnInteger:      # si page n'est pas un entier
		chambr=paginator.page(1)
	except EmptyPage:       # si le numero de page est inexistante
		chambr=paginator.page(paginator.num_pages)		

	#service=get_object_or_404(Service, pk=6)
	service=Service.objects.get(pk=2)
	hote=service.hotel.all()
		
	return render(request, 'hotelBloc/differentsHotels.html',{'hot':hote, 'chambre':chambr})

def contacts(request):
	return render(request, 'hotelBloc/contacts.html')

"""def recherche(request):
	service=Service.objects.all()
	query=request.GET.get('query')
	#erreur                      j'ai cree cette variable indefinie pour avoir une erreur 500
	return render(request, 'hotelBloc/recherche.html',{'service':service, 'query':query})
"""				

def recherche(request):
	query=request.GET.get('query')
	if not query:
			services= Service.objects.all()
	else:
		services= Service.objects.filter(typeService__icontains=query)
		if not services.exists():
			services=Service.objects.filter(hotel__nom__icontains=query)
	titre="voici le resultat de la requete consernant le theme : %s"%query	
	return render(request, 'hotelBloc/recherche.html',{'services':services, 'titre':titre, 'query':query})						


"""if not services.exists():
				message='pas toujours trouver'
			else:
				services=["<li>{}</li>".format(service.typeService) for service in services]
				message="voici les services correspondants à votre requete <ul> {} </ul>".format("<li></li>".join(services))
"""



def mapage(request):
	return render(request, 'pagea.html')

def homepage(request):


	couleurs = { 'FF0000':'rouge' ,'ED7F10':'orange' ,'FFFF00':'jaune' }
	tab2 = ['math','physique','info']
	return render(request, 'sousMain/index2.html', {'moi': couleurs, 'toi': tab2 })


def experience(request):
	tab2 = [
		{'id':1, 'filiere':'math', 'effectif':200},
		{'id':2, 'filiere':'physique', 'effectif':700},
		{'id':3, 'filiere':'info', 'effectif':400},
	]
	return render(request, 'index.html', {'registre': tab2})


def basedo(request):
	post=Post.objects.all()
	return render(request, 'sousMain/index3.html', {'regis':post})



def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			sujet = form.cleaned_data['sujet']
			message = form.cleaned_data['message']
			envoyeur = form.cleaned_data['envoyeur']
			renvoi = form.cleaned_data['return']

			envoi = True
	else:
		form = ContactForm()

	return render(request, 'sousMain/contact.html', locals())	




	




#tab = ['bien', 'excellent','meilleur']
#	return render(request, 'sousMain/index2.html', { 'moi' :
#		tab })
# si j'entre: <p>La date actuelle est : {{ moi }} </p> ds le template lié à cette page ( index2.html), le resultat sera
# La date actuelle est : ['bien', 'excellent', 'meilleur'] 
