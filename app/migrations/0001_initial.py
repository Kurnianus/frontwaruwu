# Generated by Django 4.1.7 on 2023-03-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('idNama', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('Nama', models.CharField(max_length=10)),
                ('NoTelp', models.CharField(max_length=10)),
                ('IdKamar', models.CharField(max_length=10)),
            ],
        ),
    ]