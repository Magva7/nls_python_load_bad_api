# Generated by Django 4.2.5 on 2023-09-16 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_key_field', models.CharField(max_length=255, unique=True)),
                ('field1', models.CharField(max_length=255)),
                ('field2', models.CharField(max_length=255)),
            ],
        ),
    ]
