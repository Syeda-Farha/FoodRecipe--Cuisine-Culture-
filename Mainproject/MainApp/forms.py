from .models import Comment,Maindishes
from django.forms import ModelForm, Textarea
from .models import Addrecipe
from django import forms




# create a ModelForm
class RecipeForm(forms.ModelForm):

    class Meta:
        model = Maindishes
        fields = ('name' , 'img' , 'level' , 'category', 'ingred' , 'steps' ,'tim' )

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name' , 'body','email')









