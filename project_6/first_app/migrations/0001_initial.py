# Generated by Django 5.0.6 on 2024-05-27 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('std_name', models.CharField(max_length=20)),
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
            ],
        ),
    ]
