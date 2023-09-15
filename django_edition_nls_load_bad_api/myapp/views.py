from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel
import json

@csrf_exempt
def sync_data_with_api(request):
    if request.method == 'POST':
        try:
            data_from_api = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        for item in data_from_api:
            primary_key = item.get('primary_key_field')
            string_field_1 = item.get('string_field_1')
            string_field_2 = item.get('string_field_2')

            if primary_key:
                try:
                    obj = MyModel.objects.get(primary_key_field=primary_key)
                except MyModel.DoesNotExist:
                    obj = MyModel(primary_key_field=primary_key)

                obj.string_field_1 = string_field_1
                obj.string_field_2 = string_field_2
                obj.save()

        # Помечаем удаленные записи
        existing_primary_keys = {item.get('primary_key_field') for item in data_from_api if item.get('primary_key_field')}
        MyModel.objects.exclude(primary_key_field__in=existing_primary_keys).update(is_deleted=True)

        return JsonResponse({'message': 'Data synchronized successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
