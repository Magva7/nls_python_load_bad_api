from django.shortcuts import render
import requests
from .models import MyData
from django.http import HttpResponse
import json

def index_page(request):
    return render(request, 'index.html')

def sync_data_with_api(request):  # принимает объект запроса
    """ 
    Функция, которая будет загружать данные из API, 
    сравнивать их с данными в базе данных и выполнять синхронизацию.
    URL надо поменять на нужный)
    """
    api_url = 'https://example.com/api/data'

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data_from_api = response.json()
        response = requests.get(api_url)
        data_from_api = response.json()

        # Получение данных из БД
        existing_data = MyData.objects.all()

        # Создаем набор primary key значений для сравнения
        existing_primary_keys = set(obj.primary_key_field for obj in existing_data)
        api_primary_keys = set(obj['primary_key_field'] for obj in data_from_api)

        # Ищем объекты, которые есть в JSON, но нет в базе БД, и создаем их
        new_objects = [MyData(**obj) for obj in data_from_api if obj['primary_key_field'] not in existing_primary_keys]
        MyData.objects.bulk_create(new_objects)

        # Обновляем строки данных там, где что-то поменялось
        for obj in data_from_api:
            if obj['primary_key_field'] in existing_primary_keys:
                existing_obj = MyData.objects.get(primary_key_field=obj['primary_key_field'])
                for key, value in obj.items():
                    if key != 'primary_key_field' and getattr(existing_obj, key) != value:
                        setattr(existing_obj, key, value)
                        existing_obj.save()

        # Помечаем записи на удаление
        for obj in existing_data:
            if obj.primary_key_field not in api_primary_keys:
                obj.delete()

            return HttpResponse("Data synchronization completed")
    except requests.exceptions.RequestException as e:
        # Ловим экспешены например, если API недоступно
        return HttpResponse(f"Error: {e}")
    except json.JSONDecodeError as e:
        # Обработка ошибок JSON-декодирования, например, если ответ не является JSON
        return HttpResponse(f"Error decoding JSON: {e}")
