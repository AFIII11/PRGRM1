# Generated by Django 4.2.3 on 2023-08-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotelname', models.CharField(max_length=30)),
                ('Rating', models.CharField(max_length=30)),
                ('Item', models.CharField(max_length=30)),
                ('Price', models.CharField(max_length=10)),
                ('Contact', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=30)),
            ],
        ),
    ]