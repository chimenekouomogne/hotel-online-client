from django.db import models

# Create your models here.

class Hotel(models.Model):
	nom=models.CharField(max_length=200, unique=True)
	localite=models.CharField(max_length=255)
	telephone=models.IntegerField()
	photo=models.URLField()
	etoile=models.IntegerField(default=3)

	def __str__(self):
		return(self.nom)


class Client(models.Model):
	email=models.EmailField(max_length=100)
	nom=models.CharField(max_length=200)

	def __str__(self):
		return(self.email)

class Service(models.Model):
	typeService=models.CharField(max_length=200)
	disponibilite=models.BooleanField(default=True)
	created_at=models.DateTimeField(auto_now_add=True)
	hotel=models.ManyToManyField(Hotel, related_name='services',blank=True)
	# related_name indique le nom à utiliser pour la relation inverse depuis l'objet lié vers celui ci
	# ce sera le nom utilisé dès qu'on voudra connaitre tous les services d'un hotel

	def __str__(self):
		return(self.typeService)

class Reservation(models.Model):
	created_at=models.DateTimeField("crée le", auto_now_add=True)  # date de creation, 'crée le' est le nom que je veux attribué à ce champs
	contacted=models.BooleanField(default=False)       # indique si la reservation a été traité ou pas
	client=models.ForeignKey(Client, on_delete=models.CASCADE)  #on_delete ie dès qu'on suprime le client ça suprime la reservation
	service=models.OneToOneField(Service, on_delete=models.CASCADE,verbose_name='service sollicité ') # dans le cas ou il ya des relations entre les classes,
	# j'utilise verbose_name pour attribuer un nom à mes champs

	def __str__(self):
		return(self.client)


class Chambre(models.Model):
	code=models.CharField(max_length=100)
	categorie=models.CharField(max_length=100)
	disponibilite=models.BooleanField(default=True)
	hotel=models.ForeignKey(Hotel, on_delete=models.CASCADE, blank=True, related_name="chambre")
	photo=models.ImageField(upload_to="media/", blank=True)
	prix=models.IntegerField(default=5000)

	def __str__(self):
		return(self.code)














class Abstraite(models.Model):
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True



class Post(Abstraite):
	titre=models.CharField(max_length=255)
	corps=models.TextField()
	
	def __str__ (self):
		return(self.titre)
		

class Article(Abstraite):
	titre = models.CharField(max_length=100)
	auteur = models.CharField(max_length=42)
	contenu = models.TextField(null=True)
	
	def __str__ (self):
		return(self.titre)
