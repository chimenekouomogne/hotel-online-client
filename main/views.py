from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Hotel, Client, Service, Reservation, Chambre

# Create your views here.


def indexHotel(request):
	return render(request, 'hotelBloc/indexHotel.html')

def reservation(request):
	if request.method=='POST':
		email=request.POST.get('email')
		nom=request.POST.get('nom')

		client=Client.objects.filter(email=email)
		if not client.exists(): # ici je cree l'objet s'il n'existe pas
			client=Client.objects.create(email=email, nom=nom)

		cod=request.POST.get('codechambre')
		chambr=Chambre.objects.get(code=cod)
		service=Service.objects.get(typeService='Hebergement')
		reserver=Reservation.objects.create(client=client, service='service')
		# reserver=Reservation()
		# reserver.client=client
		# reserver.service=service
		# reserver.save()
		chambr.disponibilite=False
		chambr.save()

	#disponible=Service.objects.filter(disponibilite=True).order_by('-created_at')[:4]  # je demande qu'on affiche en groupe de 3 les services dispo et par ordre de creation 
	
	return render(request, 'hotelBloc/reservation.html')

	
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




