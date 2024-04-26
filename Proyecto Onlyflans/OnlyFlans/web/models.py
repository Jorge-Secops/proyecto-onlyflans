from django.db import models
from uuid import uuid4

# Create your models here.

class flan(models.Model):

    flan_uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class ContactForm(models.Model):
    
    contact_form_uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name
    

from django import forms
from .models import ContactForm

class ContactFormForm(forms.Form):
    
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']