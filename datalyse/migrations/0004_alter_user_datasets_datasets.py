# Generated by Django 5.0 on 2024-01-12 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalyse', '0003_alter_user_datasets_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_datasets',
            name='datasets',
            field=models.FileField(max_length=500, upload_to=''),
        ),
    ]
