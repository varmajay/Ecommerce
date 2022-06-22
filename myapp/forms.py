import email
from faulthandler import disable
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center','placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center','placeholder': 'Confirm Password'}),
    )
    class Meta:
        model = User 
        fields = ['name','email','phone','gender','address','role']
        widgets = { 
            "name":forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}),
            "email":forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Email'}),
            "phone":forms.TextInput(attrs={'class':'form-control','placeholder': 'Phone'}),
            "gender":forms.Select(attrs={'class':'form-control','placeholder': 'Gender'}),
            "role":forms.Select(attrs={'class':'form-control','placeholder': 'role'}),
            "address":forms.TextInput(attrs={'class':'form-control','placeholder': 'Address'}),
        }


class LoginForm(forms.Form):
    email =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}))
    password= forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','category','quantity','price','description','pic']
        widgets = { 
            "product_name":forms.TextInput(attrs={'class':'form-control'}),
            "category":forms.Select(attrs={'class':'form-control'}),
            "quantity":forms.NumberInput(attrs={'class':'form-control'}),
            "price":forms.NumberInput(attrs={'class':'form-control'}),
            "description":forms.Textarea(attrs={'class':'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    role = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), disabled=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), disabled=True)
    class Meta:
        model = User
        fields = ['role','name','email','phone','gender','address','profile']
        widgets = { 
            "name":forms.TextInput(attrs={'class':'form-control'}),
            "phone":forms.TextInput(attrs={'class':'form-control'}),
            "gender":forms.Select(attrs={'class':'form-control'}),
            "role":forms.Select(attrs={'class':'form-control'}),
            "address":forms.TextInput(attrs={'class':'form-control'}),
        }

class MycartForm(forms.ModelForm):
    class Meta:
        model = Mycart
        fields = ['quantity']



class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Buyproduct
        fields = ['address','payment_method']
        widgets = { 
            "address":forms.TextInput(attrs={'class':'form-control'}),
            "payment_method":forms.Select(attrs={'class':'form-control'}),

        }


class ChangePassword(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),    
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'align':'center'}),    
    )
    