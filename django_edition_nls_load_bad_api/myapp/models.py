from django.db import models

class MyModel(models.Model):
    primary_key_field = models.CharField(max_length=100, unique=True)
    string_field_1 = models.CharField(max_length=255)
    string_field_2 = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.primary_key_field
