from django.forms import ModelForm
import django.forms as forms
from .models import Article

class ArticleForm(forms.Form):
    title = forms.CharField(label='Title: ', widget=forms.TextInput(attrs={'maxlength': 50, 'class':'form_input'}))
    body = forms.CharField(label='Body: ', widget=forms.Textarea(attrs={'class':'form_input'}))

class ArticleModelForm(ModelForm):
    class Meta:
        model = Article
        exclude = []