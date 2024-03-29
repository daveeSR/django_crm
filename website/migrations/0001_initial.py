# Generated by Django 4.2 on 2023-04-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address_line', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('county', models.CharField(max_length=50)),
            ],
        ),
    ]
