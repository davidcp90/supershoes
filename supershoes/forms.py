from django.forms import ModelForm
from supershoes.models import *

class ArticleForm(ModelForm):
    """Auto generated form to create Article models."""
    class Meta:
        model = Article