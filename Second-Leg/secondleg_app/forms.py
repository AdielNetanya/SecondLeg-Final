from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from secondleg_app.models import Advertisement
from .models import RecommendedRestaurant


class RecommendedRestaurantForm(forms.ModelForm):
    class Meta:
        model = RecommendedRestaurant
        fields = ['name', 'photo', 'description', 'restaurant_url']


class RecipeListHelper(FormHelper):
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
        fields = ['username', 'email', 'password1', 'password2']


class advertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = '__all__'
