# Generated by Django 4.2.7 on 2023-12-02 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('nota', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
