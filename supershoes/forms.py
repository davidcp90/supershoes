from django.forms import ModelForm
from supershoes.models import *

class ArticleForm(ModelForm):
    """Auto generated form to create Articles models."""
    class Meta:
        model = Articles
        fields = '__all__' 

class StoreForm(ModelForm):
    """Auto generated form to create Stores models."""
    class Meta:
        model = Stores
        fields = '__all__' 