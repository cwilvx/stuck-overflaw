from django import forms
from .views import mode
from .models import Profile,Comment
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from django_summernote.widgets import SummernoteInplaceWidget, SummernoteWidget

class NewArticleForm(forms.ModelForm):
    class Meta:
        model = mode
        exclude = ['editor', 'created_on','slug']
        # widgets = {
        #     'post': SummernoteWidget(),
        # }
        
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2',)    
         
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','location','birth_date','bio']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        
