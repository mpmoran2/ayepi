# Generated by Django 3.2.6 on 2021-08-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Googs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ethnicity', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=200)),
                ('From', models.CharField(max_length=100)),
            ],
        ),
    ]
