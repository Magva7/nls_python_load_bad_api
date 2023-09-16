from django.shortcuts import render
import requests
from .models import MyData
from django.http import HttpResponse
import json

def index_page(request):
    return render(request, 'index.html')

def synchronize_data():
    """Функция для синхронизации данных с API."""
    api_url = 'https://example.com/api/data'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data_from_api = response.json()

        existing_data = MyData.objects.all()
        existing_primary_keys = set(obj.primary_key_field for obj in existing_data)
        api_primary_keys = set(obj['primary_key_field'] for obj in data_from_api)

        new_objects = [MyData(**obj) for obj in data_from_api if obj['primary_key_field'] not in existing_primary_keys]
        MyData.objects.bulk_create(new_objects)

        for obj in data_from_api:
            if obj['primary_key_field'] in existing_primary_keys:
                existing_obj = MyData.objects.get(primary_key_field=obj['primary_key_field'])
                for key, value in obj.items():
                    if key != 'primary_key_field' and getattr(existing_obj, key) != value:
                        setattr(existing_obj, key, value)
                        existing_obj.save()

        for obj in existing_data:
            if obj.primary_key_field not in api_primary_keys:
                obj.delete()

        return HttpResponse("Data synchronization completed")
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error: {e}")
    except json.JSONDecodeError as e:
        return HttpResponse(f"Error decoding JSON: {e}")
