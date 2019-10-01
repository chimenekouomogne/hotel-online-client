from django.shortcuts import render
from django.http import HttpResponse

# ce module views n'existait pas donc je l'ai crée

def parent(request):
	return render(request, 'layouts/parent3.html')






def blank(request):
	return render(request, 'sb_admin/blank.html')


def page404(request):
	return render(request, 'sb_admin/404.html')


def ajouterPersonnel(request):
	return render(request, 'sb_admin/personnelAjout.html')


def personnel(request):
	return render(request, 'sb_admin/personnel.html')


	
def soso(request):
    return render(request, 'temple.html')

def sony(request):
    return render(request, 'petitDossier/petitemple.html')


