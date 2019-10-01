from django import forms


class ContactForm(forms.Form):
	sujet = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	envoyeur = forms.EmailField(label="votre adresse mail")
	renvoi = forms.BooleanField(help_text="cochez pour obtenir le mail envoyé", required=False)

