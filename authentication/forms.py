from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core import validators
from django.contrib.auth.validators import ASCIIUsernameValidator
class LoginForm(forms.Form):
    username=forms.CharField(max_length=20 ,help_text="Enter Username",
                             widget=forms.TextInput(attrs={'placeholder':'Enter Username','style':'color:whitesmoke;','class':'center-align'}),required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','style':'color:whitesmoke;','class':'center-align'}),max_length=16,label="Enter Password",required=True)

class SignupForm(forms.Form):
    username=forms.CharField(max_length=20,help_text="Enter a Username",
                             widget=forms.TextInput(attrs={'placeholder':"Enter a Username",'style':'color:whitesmoke;','class':'center-align'}),validators=[ASCIIUsernameValidator],required=True)
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','style':'color:whitesmoke;','class':'center-align'}),validators=[validate_password],required=True)

    cnf_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password','style':'color:whitesmoke;','class':'center-align'}),validators=[validate_password],required=True)