from .models import Animal
from django.forms import ModelForm



class animalform(ModelForm):
    class Meta:
        model = Animal
        fields = ['name','img','video','detail']