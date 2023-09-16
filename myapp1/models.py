from django.db import models

class MyData(models.Model):
    # Поле, в котором храним primary key
    primary_key_field = models.CharField(max_length=255, unique=True)
    # Поля, в которых храним строковые данные
    field1 = models.CharField(max_length=255)
    field2 = models.CharField(max_length=255)

    def __str__(self):
        return self.primary_key_field
