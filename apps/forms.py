from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from .models import ProfilePicture , user
#from django.forms.widgets import *

class ProfilePictureForm(forms.ModelForm):
    img = forms.ImageField(label="Change Picture" , required=True , )


    class Meta:
        model = ProfilePicture
        fields = ['img',]

class UserForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}),label='Date of Birth')
    sex=forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder' : 'Enter Sex'}), label='Sex', max_length=10 )
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'  , 'placeholder' : 'Enter Bio'} ),label='Bio' , required=False )
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder' : 'Enter Address'}),label='Full Address' )
    pincode= forms.CharField(widget=forms.NumberInput(attrs={'class': 'col-auto', 'placeholder' : 'Enter Pincode'}))


    
    class Meta:
        model = user
        fields = ('dob','sex','bio','address','pincode')
