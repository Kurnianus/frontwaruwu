# Generated by Django 4.1.7 on 2023-04-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_admin_idkamar'),
    ]

    operations = [
        migrations.AddField(
            model_name='kamarkost',
            name='nama',
            field=models.CharField(max_length=100, null=True),
        ),
    ]