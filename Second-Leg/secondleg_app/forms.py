from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from secondleg_app.models import Advertisement
from .models import RecommendedShoe


class RecommendedShoeForm(forms.ModelForm):
    class Meta:
        model = RecommendedShoe
        fields = ['name', 'description', 'photo', 'shoe_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'shoe_url': forms.URLInput(attrs={'class': 'form-control'}),
        }


class AdvertisementListHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'GET'  # Important for GET requests
        self.layout = Layout(
            Submit('edit', 'Edit', css_class='btn btn-primary'),
            Submit('delete', 'Delete', css_class='btn btn-danger'),
        )


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['brand', 'contact_name', 'description', 'image']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
