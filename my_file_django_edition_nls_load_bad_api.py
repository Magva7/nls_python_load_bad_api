from django.db import models
import requests
from myapp.models import MyModel

class MyModel(models.Model):
    primary_key_field = models.CharField(max_length=100, unique=True)
    string_field_1 = models.CharField(max_length=255)
    string_field_2 = models.CharField(max_length=255)

    def __str__(self):
        return self.primary_key_field
    


def sync_data_with_api():
    # Загрузка данных из "плохого" API
    response = requests.get('URL_API')
    data_from_api = response.json()

    for item in data_from_api:
        primary_key = item['primary_key_field']
        string_field_1 = item['string_field_1']
        string_field_2 = item['string_field_2']

        # Попытка найти запись в базе данных по primary_key
        try:
            obj = MyModel.objects.get(primary_key_field=primary_key)
        except MyModel.DoesNotExist:
            # Если запись не найдена, создаем новую
            MyModel.objects.create(primary_key_field=primary_key, string_field_1=string_field_1, string_field_2=string_field_2)
        else:
            # Если запись найдена, обновляем данные
            if obj.string_field_1 != string_field_1:
                obj.string_field_1 = string_field_1
            if obj.string_field_2 != string_field_2:
                obj.string_field_2 = string_field_2
            obj.save()

    # Помечаем удаленные записи
    existing_primary_keys = set(item['primary_key_field'] for item in data_from_api)
    MyModel.objects.exclude(primary_key_field__in=existing_primary_keys).update(is_deleted=True)
