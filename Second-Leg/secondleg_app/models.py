from django.db import models
from django.db.models import TextField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.contrib.auth.models import User

class StrippingTextField(TextField):
    def formfield(self, **kwargs):
        kwargs['strip'] = True
        return super(StrippingTextField, self).formfield(**kwargs)
    
class Advertisement(models.Model):
    advertisement = models.CharField(max_length=30, null=True, blank=True)
    composites = models.TextField()  # Keep as TextField for now, consider JSONField later
    instructions = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)  # Add this field
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements', default=1)
    
class RecommendedShoe(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='restaurant_photos/', blank=True, null=True)
    description = models.TextField()
    shoe_url=models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name