from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField


class StrippingTextField(TextField):
    def formfield(self, **kwargs):
        kwargs['strip'] = True
        return super(StrippingTextField, self).formfield(**kwargs)


def get_upload_path(instance, filename):
    # This function constructs the upload path
    return f'advertisements/{filename}'  # Ensure images are saved in advertisements/


class Advertisement(models.Model):
    brand = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='advertisements/', blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.brand


class RecommendedShoe(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='shoe_photos/', blank=True, null=True)
    description = models.TextField()
    shoe_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
