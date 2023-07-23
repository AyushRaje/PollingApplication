from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=20 ,help_text="Enter Username",
                             widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}),max_length=16,label="Enter Password")

class SignupForm(forms.Form):
    username=forms.CharField(max_length=20,help_text="Enter a Username",
                             widget=forms.TextInput(attrs={'placeholder':"Enter a Username"}))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}),max_length=16)

    cnf_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}),max_length=16)