from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record

class RegisterForm(UserCreationForm):
    class Mate:
        model=User
        fields=['username','password1', 'password2',]

    def __init__(self, *args, **kwargs) :
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder']='Username'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Paasword'

class RecordForm(ModelForm):
    class Meta:
        model=Record
        fields=['name','email','phone','address','city','state','zipcode']

    def __init__(self, *args, **kwargs) :
        super(RecordForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='Enter the name'
        self.fields['email'].widget.attrs['placeholder']='Enter the email'
        self.fields['phone'].widget.attrs['placeholder']='Enter the phone number'
        self.fields['address'].widget.attrs['placeholder']='Enter the address'
        self.fields['city'].widget.attrs['placeholder']='Enter the city'
        self.fields['state'].widget.attrs['placeholder']='Enter the state'
        self.fields['zipcode'].widget.attrs['placeholder']='Enter the zipcode'