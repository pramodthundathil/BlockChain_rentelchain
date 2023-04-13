from django.forms import ModelForm
from .models import Properties 

class PropertyAddForm(ModelForm):
    class Meta:
        model = Properties
        fields = ["name","rentpermomth","place","district","state","description","image"]